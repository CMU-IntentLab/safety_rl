"""
Please contact the author(s) of this library if you have any questions.
Authors: Kai-Chieh Hsu ( kaichieh@princeton.edu )
         Vicenc Rubies Royo ( vrubies@berkeley.edu )
"""

from gym.envs.registration import register
import gym

env_dict = gym.envs.registration.registry.env_specs.copy()
for env in env_dict:
    if 'dubins_car-v1' in env:
        print("Remove {} from registry".format(env))
        del gym.envs.registration.registry.env_specs[env]

register(
    id="dubins_car-v1",
    entry_point="gym_reachability.gym_reachability.envs:DubinsCarOneEnv"
)


