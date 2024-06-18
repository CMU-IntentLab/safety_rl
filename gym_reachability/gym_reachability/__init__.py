"""
Please contact the author(s) of this library if you have any questions.
Authors: Kai-Chieh Hsu ( kaichieh@princeton.edu )
         Vicenc Rubies Royo ( vrubies@berkeley.edu )
"""

from gym.envs.registration import register
import gym


register(
    id="dubins_car-v1",
    entry_point="gym_reachability.gym_reachability.envs:DubinsCarOneEnv"
)


