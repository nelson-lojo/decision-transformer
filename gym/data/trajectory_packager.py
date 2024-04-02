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

# take in two file_names for trajectories/training
# combines the trajectories in both into a combined file with the given name
def merge_trajectories(name, files):
    trajectories = []
    for file_name in files:
        with open(f'{file_name}.pkl', 'rb') as f:
            temp = pickle.load(f)
        
        if isinstance(temp, list):
            for trajectory in temp:
                trajectories.append(trajectory)
        elif isinstance(temp, dict):
            trajectories.append(temp)
        else:
            raise TypeError("received file is neither list nor dict")
    
    with open(f'{name}.pkl', 'wb') as f:
        pickle.dump(trajectories, f)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('file_name', type=str, default='test1')
    parser.add_argument('traj_files', nargs='*')
    args = parser.parse_args()
    merge_trajectories(args.file_name, args.traj_files)
