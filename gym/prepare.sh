#!/bin/bash

install_conda() {
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm -rf ~/miniconda3/miniconda.sh
}

download_mujoco() {
    wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
    tar -xf mujoco210-linux-x86_64.tar.gz 
    mkdir ~/.mujoco/
    mv mujoco210/ ~/.mujoco/mujoco210
    rm mujoco210-linux-x86_64.tar.gz 
}

prep_env() {
    conda env create -f conda_env.yml

    conda activate decision-transformer-gym
    $CONDA_PREFIX/bin/pip3 install git+https://github.com/Farama-Foundation/d4rl@master#egg=d4rl
}

download_data() {
    sudo chmod 777 -R $CONDA_PREFIX/lib/python3.8/site-packages/mujoco_py
    sudo apt update && sudo apt install libosmesa6-dev
    cd data/ && $CONDA_PREFIX/bin/python download_d4rl_datasets.py
    cd ../
}


download_mujoco
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
