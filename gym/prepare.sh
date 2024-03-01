#!/bin/bash

install_conda() {
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    bash Miniconda3-latest-Linux-x86_64.sh
    rm Miniconda3-latest-Linux-x86_64.sh
}

wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
tar -xf mujoco210-linux-x86_64.tar.gz 
mkdir ~/.mujoco/
mv mujoco210/ ~/.mujoco/mujoco210
rm mujoco210-linux-x86_64.tar.gz 
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin

/opt/conda/bin/conda env create -f conda_env.yml
conda init
echo "conda activate decision-transformer-gym" > ~/.bashrc

cd data/ && python download_d4rl_datasets.python
cd ../

