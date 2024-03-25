# for testing purposes
# please run with an argument for the pkl file checked

import pickle
import numpy
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset')
    args = parser.parse_args()
    
    with open(args.dataset, 'rb') as f:
        data = pickle.load(f)

        # for viewing data directly
        #print(data)

        # for viewing variables of the trajectory
        print(data[0].keys())