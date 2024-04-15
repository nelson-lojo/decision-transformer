import numpy as np
import torch
import os

import time

from tqdm import tqdm

class Trainer:

    def __init__(self, model, optimizer, batch_size, get_batch, loss_fn, scheduler=None, eval_fns=None, save_steps=1000):
        self.model = model
        self.optimizer = optimizer
        self.batch_size = batch_size
        self.get_batch = get_batch
        self.loss_fn = loss_fn
        self.scheduler = scheduler
        self.eval_fns = [] if eval_fns is None else eval_fns
        self.diagnostics = dict()
        self.save_steps = save_steps

        self.start_time = time.time()

    def train_iteration(self, num_steps, iter_num=0, print_logs=False, prog_bar=None):

        train_losses = []
        logs = dict()
        if prog_bar is None:
            prog_bar = tqdm(total=num_steps)

        train_start = time.time()

        model_type = type(self.model).__name__
        model_type = model_type.lower()

        state_path = os.path.join(f'gym/checkpoints/{model_type}', "state.pt")
        start_step = 0
        if os.path.exists(state_path):
            checkpoint = torch.load(state_path) #Will break on iter load
            self.model.load_state_dict(checkpoint["state_dict"])
            self.optimizer.load_state_dict(checkpoint["optimizer"])
            start_step = checkpoint["step"]
        
        num_steps = num_steps - start_step

        self.model.train()
        for i in range(num_steps):
            train_loss = self.train_step()
            train_losses.append(train_loss)
            if self.scheduler is not None:
                self.scheduler.step()
            prog_bar.update(1)

            if i % self.save_steps == 0:
                training_state = {
                    "state_dict": self.model.state_dict(),
                    "optimizer": self.optimizer.state_dict(),
                    "step": i,
                }

                if not os.path.exists('gym/checkpoints'):
                    os.makedirs('gym/checkpoints')
                if not os.path.exists(f'gym/checkpoints/{model_type}'):
                    os.makedirs(f'gym/checkpoints/{model_type}')
                
                #state_path = os.path.join(f'gym/checkpoints/{model_type}', "state.pt")
                state_path_iter = os.path.join(f'gym/checkpoints/{model_type}', 'state_{i}_steps.pt')

                torch.save(training_state, state_path)
                torch.save(training_state, state_path_iter)

        logs['time/training'] = time.time() - train_start

        eval_start = time.time()

        self.model.eval()
        for eval_fn in self.eval_fns:
            outputs = eval_fn(self.model)
            for k, v in outputs.items():
                logs[f'evaluation/{k}'] = v

        logs['time/total'] = time.time() - self.start_time
        logs['time/evaluation'] = time.time() - eval_start
        logs['training/train_loss_mean'] = np.mean(train_losses)
        logs['training/train_loss_std'] = np.std(train_losses)

        for k in self.diagnostics:
            logs[k] = self.diagnostics[k]

        if print_logs:
            print('=' * 80)
            print(f'Iteration {iter_num}')
            for k, v in logs.items():
                print(f'{k}: {v}')

        return logs

    def train_step(self):
        states, actions, rewards, dones, attention_mask, returns = self.get_batch(self.batch_size)
        state_target, action_target, reward_target = torch.clone(states), torch.clone(actions), torch.clone(rewards)

        state_preds, action_preds, reward_preds = self.model.forward(
            states, actions, rewards, masks=None, attention_mask=attention_mask, target_return=returns,
        )

        # note: currently indexing & masking is not fully correct
        loss = self.loss_fn(
            state_preds, action_preds, reward_preds,
            state_target[:,1:], action_target, reward_target[:,1:],
        )
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        return loss.detach().cpu().item()
