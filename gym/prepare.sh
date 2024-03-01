#!/bin/bash

install_conda() {
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
}

wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
tar -xf mujoco210-linux-x86_64.tar.gz 
mkdir ~/.mujoco/
mv mujoco210/ ~/.mujoco/mujoco210
rm mujoco210-linux-x86_64.tar.gz 
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin

conda env create -f conda_env.yml

cd data/ && python download_d4rl_datasets.python
cd ../

