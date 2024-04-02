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


# file_name is a pickle file containing a list of tuples (reward, observation, action, terminals) that are assumed sequential
# data_to_trajectory will convert the file of tuples to a pickle file with a trajectory
def datafile_to_trajectory(file_name, name):
    
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
            terminals.append(data[i][3])

        output['observations'] = np.array(observations)
        output['next_observations'] = np.array(next_observations)
        output['actions'] = np.array(actions)
        output['rewards'] = np.array(rewards)
        output['terminals'] = np.array(terminals)


    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(output, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, default='test1')
    parser.add_argument('name', type=str, default="test2")
    args = parser.parse_args()
    datafile_to_trajectory(args.file_name, args.name)
    

        
    
        

        
    
    
    



