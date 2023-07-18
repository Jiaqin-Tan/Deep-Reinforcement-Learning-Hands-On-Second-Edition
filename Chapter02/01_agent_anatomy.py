import random
from typing import List


class Environment:
    def __init__(self):
        self.steps_left = 10

    def get_observation(self) -> List[float]:
        return [0.0, 0.0, 0.0]

    def get_actions(self) -> List[int]:
        return [0, 1]

    def is_done(self) -> bool:
        return self.steps_left == 0

    # the action() method is the central piece in the env's functionality.
    # it handles agent's action, and returns the reward for that action.
    def action(self, action: int) -> float: # typing hint, what is it? "->  ...action: int)float"? By running the code with mypy it will check if the return value is of the correct type, e.g. input expect to be int and output expect to be float.
        if self.is_done():
            raise Exception("Game is over")
            # raise statement: user-defined exception, raise an exception when a certain condition is met. 
            # the syntax is exactly as shown above.
        self.steps_left -= 1
        return random.random() #random() method returns a random float number between 0.0 and 1.0.

# in Agent class, two main component, the constructor and the step() method.
class Agent:
    def __init__(self):
        self.total_reward = 0.0 # build the counter for reward here

    # The step function accepts the environment instance as an argument and allows the agent to perform: Observe the env, make a decision based on the obs, submit the action to the env, get the reward for the current step.
    def step(self, env: Environment):
        current_obs = env.get_observation()
        actions = env.get_actions()
        reward = env.action(random.choice(actions))
        self.total_reward += reward

# this creates both classes and runs one episode.
# " if __name__ == "__main__": " -- 
if __name__ == "__main__":
    env = Environment()
    agent = Agent()

    while not env.is_done():
        agent.step(env)

    print("Total reward got: %.4f" % agent.total_reward)
