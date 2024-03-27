# for testing purposes
# please run with an argument for the pkl file checked

import pickle
import numpy as np
import argparse

def check_format(data_struct, indent = 0):
    gap = "\t" * (indent)
    if isinstance(data_struct, list):
        print(gap + f'list length:{len(data_struct)}')
        if (len(data_struct) > 0):
            check_format(data_struct[0], indent + 1)
    elif isinstance(data_struct, dict):
        print(gap + f'dict keys:{data_struct.keys()}')
        for key in data_struct.keys():
            print(gap + f'{key}: {type(data_struct[key])}')
            check_format(data_struct[key], indent+1)
    elif isinstance(data_struct, np.ndarray):
        print(gap + f'np array: {data_struct.shape}')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    args = parser.parse_args()
    
    with open(args.dataset, 'rb') as f:
        data = pickle.load(f)
    
    # view the format of the pickle file
    check_format(data)

    # for viewing data directly
    #print(data)

    # for viewing parts of the data
    #print(data[0].get('next_observations'))

    #for env_name in ['ant', 'halfcheetah', 'hopper', 'walker2d']:
    #	for dataset_type in ['medium', 'medium-replay', 'expert']:
    #		name = f'{env_name}-{dataset_type}-v2'


