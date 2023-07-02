# Soft Actor Restrospective Critic
Source code and data of all experimental runs to accompany our RLDM 2022 paper: https://arxiv.org/abs/2306.16503

We propose a new algorithm, SARC that builds on top of SAC. We use the original SAC implementation made available by spinningup and modify it to implement SARC. The code can be found inside "spinningup" folder. The data for all DeepMind Control Experiments is within spinningup-data-deepmind-control-suite. The data for all PyBullet Experiments is within 2Mspinningup-data-pybullet. 

## Prerequisites
 * [Python 3.6+]

## Getting Started
 1. Inside a python >= 3.6 virtual environment, clone this repository <br>
 2. `cd spinningup`<br>
 3. `pip install -e .` to set up required libraries. <br>
 4. You may do `pip install pybullet` for PyBullet open-source continuous control environments. <br>
 5. You may install DeepMind Control suite environments as well. We used: https://github.com/denisyarats/dmc2gym
 6. To run SAC: `python -m spinup.run sac --env_name AntBulletEnv --hid [400,300] --exp_name sac_Ant_400300 --use_retro_loss False`. <br>
 7. To run SARC: `python -m spinup.run sac --env_name AntBulletEnv --hid [400,300] --exp_name sac_Ant_400300_retroloss`. <br>

 ## Hyperparams
 1. --hid specifies the hidden layer sizes for the critic neural network
 2. --env_name selects the environment. List of PyBullet environments: https://github.com/benelot/pybullet-gym. The code will also work with MuJoCo and DeepMind control environments after installing and importing them. For MuJoCo, it will run right away. For DeepMind Control, go into file run_utils and uncomment: `import dmc2gym`. Ensure that you specify the environment name like: dmCheetahRun, dmWalkerWalk etc.
 3. --exp_name will create a directory to log all experiment data
 4. --use_retro_loss is by default set of True. When set to False, SARC reduces to SAC.
 5. Like SAC controls updation of target, we also have --update_prev_after, --update_prev_every and polyak_prev for controlling updation of prev networks. You may leave these as default or play around with them

## Acknowledgements and References
1. https://spinningup.openai.com/en/latest/
2. https://github.com/benelot/pybullet-gym
3. https://github.com/deepmind/dm_control/blob/main/dm_control/suite/README.md
4. https://github.com/denisyarats/dmc2gym

