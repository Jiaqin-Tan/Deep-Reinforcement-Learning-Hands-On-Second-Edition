import gym
from typing import TypeVar
import random

Action = TypeVar('Action')


class RandomActionWrapper(gym.ActionWrapper):
    def __init__(self, env, epsilon=0.1):
        super(RandomActionWrapper, self).__init__(env)
        # super() function: give access to the methods of a parent class. returns a temporary object of a parent class when used.
        # super().__init__(env) is equivalent to gym.ActionWrapper.__init__(env)
        #__init__ is the "def __init__" method... you are just not good at coding... these concepts...
        # def = creating method
        # __init__ is a method is called, when the class' obj is created. 
        # as you know, if you don't keep doing one thing, thing you will forgot. 
        # inside super() is call argument/parameter
        # super() can take two, first is the subclass, second is the object of that subclass
            # the two parameter seems not necessary in this case, could be this code is to work with python2
        self.epsilon = epsilon

    # override parent's agent action
    def action(self, action: Action) -> Action:
        if random.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
            # this returns an action, so it replaces the action obj passed in in the parameter
            # and then the action is returned below
        return action


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1"))
    # our Wrapper becomes the Env
    # what we modified is the action space. to just one and force the agent to take it.
    
    # below code is the same as the code in 02_cartpole_random.py
    # meaning all you need to do is modify the Env. 

    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, done, _, xz = env.step(0)
        total_reward += reward
        if done:
            break

    print("Reward got: %.2f" % total_reward)
