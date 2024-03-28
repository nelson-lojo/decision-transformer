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


# convert dict of data to a file of tuples
# or a list of tuples to a file of tuples
def data_to_file(data, file_name, isList = False):
    if isList:
        with open(f'{file_name}.pkl', 'wb') as f:
            pickle.dump(data,f)
        return
    keys = ["rewards", "observations", "actions"]
    result = []
    for i in range(len(data[keys[0]])):
        tup = []
        for key in keys:
            tup.append(data[key][i])
        result.append(tuple(tup))
    with open(f'{file_name}.pkl', 'wb') as f:
        pickle.dump(result,f)


if __name__ == '__main__':
    #parser = argparse.ArgumentParser()
    #parser.add_argument('file_name', type=str, default='ant-medium-v2')
    #args = parser.parse_args()
    # test data with same layout as ant-medium with 10 steps
    steps = 10
    data = {"rewards":[i for i in range(steps)],
           "observations":[[i for j in range(111)] for i in range(steps)],
           "actions":[[i for j in range(8)] for i in range(steps)]}
    data_to_file(data, "test1")
        

    
            
        
    
    
    
    