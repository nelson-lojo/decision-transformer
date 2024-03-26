import gym
import numpy as np
import torch
import wandb

import argparse
import pickle
import random
import sys
import os

from tqdm import tqdm

from decision_transformer.evaluation.evaluate_episodes import evaluate_episode, evaluate_episode_rtg
from decision_transformer.models.decision_transformer import DecisionTransformer
from decision_transformer.models.mlp_bc import MLPBCModel
from decision_transformer.training.act_trainer import ActTrainer
from decision_transformer.training.seq_trainer import SequenceTrainer

# file_name is a pickle file containing a list of tuples (reward, observation, action) that are assumed sequential
# data_to_trajectory will convert the file of tuples to a pickle file with a trajectory
def data_to_trajectory(file_name):
    
    output = {}
    
    with open(f'{file_name}.pkl', 'rb') as f:
        data = pickle.load(f)
        # trajectories have: observations, next_observations, actions, rewards, terminals
        observations = []
        next_observations = []
        actions = []
        rewards = []
        terminals = []

        for i in range(len(data)-1):
            observations.append(data[i][1])
            next_observations.append(data[i + 1][1])
            actions.append(data[i][2])
            rewards.append(data[i][0])

            # need to figure out how to get terminals
            terminals.append(False)

        output['observations'] = observations
        output['next_observations'] = next_observations
        output['actions'] = actions
        output['rewards'] = rewards
        output['terminals'] = terminals


    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(output, f)

        
    
        

        
    
    
    



