# Soft Actor Restrospective Critic
Source code and data of all experimental runs to accompany our ICML 2021 submission

TD;DR: We propose a new algorithm, SARC that builds on top of SAC. We use the original SAC implementation made available by spinningup and modify it to implement SARC. The code can be found inside "spinningup" folder. The data for all DeepMind Control Experiments is within spinningup-data-deepmind-control-suite. The data for all PyBullet Experiments is within 2Mspinningup-data-pybullet. 

## Prerequisites
 * [Python 3.6+]

## Getting Started
 1. Inside a python >= 3.6 virtual environment, clone this repository <br>
 2. `cd spinningup`<br>
 3. `pip install -e .` to set up required libraries. <br>
 4. `pip install pybullet` for open-source continuous control environments. <br>
 5. To run SAC: 'python -m spinup.run sac --env_name AntBulletEnv --hid [400,300] --exp_name sac_Ant_400300 --use_retro_loss False'. <br>
 6. To run SARC: 'python -m spinup.run sac --env_name AntBulletEnv --hid [400,300] --exp_name sac_Ant_400300_retroloss'. <br>
