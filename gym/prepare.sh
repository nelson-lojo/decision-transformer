#!/bin/bash

# cd gym/
conda env create -f conda_env.yml

cd data/ && python download_d4rl_datasets.python
cd ../
bash

