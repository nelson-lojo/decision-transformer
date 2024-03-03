#!/bin/bash

install_conda() {
    mkdir -p ~/miniconda3
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    export PATH=~/miniconda3/bin/:$PATH
    rm -rf ~/miniconda3/miniconda.sh
}

install_mujoco() {
    wget https://mujoco.org/download/mujoco210-linux-x86_64.tar.gz
    tar -xf mujoco210-linux-x86_64.tar.gz 
    mkdir ~/.mujoco/
    mv mujoco210/ ~/.mujoco/mujoco210
    rm mujoco210-linux-x86_64.tar.gz 

    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$HOME/.mujoco/mujoco210/bin
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib/nvidia
}

prep_env() {
    conda env create -f conda_env.yml

    conda activate decision-transformer-gym
    $CONDA_PREFIX/bin/pip3 install git+https://github.com/Farama-Foundation/d4rl@master#egg=d4rl
    $CONDA_PREFIX/bin/pip install typing_extensions==4.4.0
}

download_data() {
    sudo chmod 777 -R $CONDA_PREFIX/lib/python3.8/site-packages/mujoco_py
    sudo apt update && sudo apt install -y libosmesa6-dev libglew-dev
    cd data/ && $CONDA_PREFIX/bin/python download_d4rl_datasets.py
    cd ../
}



run_experiment() {
    task=$1
    layer=$2
    embd=$3
    inner=$4
    heads=$5

    screen -S Training_L"$layers"_E"$embd"_I"$inner"_H"$heads" \
        -dm python experiment.py --env $task --dataset expert --model_type dt --embed_dim $embd --n_layer $layer --n_head $heads --n_inner $inner --max_iters 25
}

test_experiment() {
    task=$1
    python experiment.py --env $task --dataset expert --model_type dt --max_iters 2 --num_steps_per_iter 5 --num_eval_episodes 1
}

sweep() {
    command=$1
    layers=(4 5 6)
    embeds=(12 16 24 32 48)
    in_facs=(0.5 1 2 3 4)

    for layr in "${layers[@]}"; do
    for embd in "${embeds[@]}"; do
    for in_f in "${in_facs[@]}"; do
        inner_dim_intermediate=$(echo "scale=0; $in_f * $embd" | bc)
        innd=${inner_dim_intermediate%.*}
        $command halfcheetah $layr $embd $innd 1
    done; done; done
}


