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
        # as you know, if you don't keep doing one thing, thing you will forgot. 
        
        self.epsilon = epsilon

    def action(self, action: Action) -> Action:
        if random.random() < self.epsilon:
            print("Random!")
            return self.env.action_space.sample()
        return action


if __name__ == "__main__":
    env = RandomActionWrapper(gym.make("CartPole-v1"))

    obs = env.reset()
    total_reward = 0.0

    while True:
        obs, reward, done, _, xz = env.step(0)
        total_reward += reward
        if done:
            break

    print("Reward got: %.2f" % total_reward)
