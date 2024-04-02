
# OpenAI Gym

## Installation

#### MuJoCo

Experiments require MuJoCo.
Follow the code written in prepare.sh, running the corresponding shell functions. Shell functions can be run in lambda with:

```
bash prepare.sh function_name arg0 arg1 ...
```
For example, installing MuJoCo would be:
```
bash prepare.sh install_mujoco
```
Alternatively, run:
```
source prepare.sh
```
After this, you can call functions directly:
```
install_mujoco
```

#### Conda

We also need conda. Install it with the install_conda function in prepare.sh. You may need to add it to the path using:
```
nano ~/.bashrc
```
This will open .bashrc to edit. Add at the bottom:
```
export PATH=~/miniconda3/bin:$PATH
```
Save and exit with ctrl+x, then update changes in the terminal with:
```
source ~/.bashrc
```

## Downloading datasets

Datasets are stored in the `data` directory.
Follow the code written in prepare.sh, running the corresponding shell functions.

## Manipulating data

`pklopener.py` can be used to check the formatting of the pickle file. Use by calling:
```
python pklopener.py file_name
```
`datapkler.py` can be used to turn a list or tuple into a pkl file formatted for `file_to_trajectory.py`. `file_to_trajectory.py` takes in a pkl file of tuples and converts them into a trajectory file that a model can be run on. `trajectory_packager.py` takes in any number of trajectory or list-of-trajectory files and combines them into a list-of-trajectory file, which is what the model is trained on.

## Example usage

Experiments can be reproduced with the following:

```
python experiment.py --env hopper --dataset medium --model_type dt
```

Adding `-w True` will log results to Weights and Biases.

It's more straightforward to just use the prepare.sh functions for this. For example:

```
test_experiment hopper
```

If you are running into the error "fatal error: GL/glew.h: No such file or directory" run:
```
sudo apt-get install libglew-dev
```