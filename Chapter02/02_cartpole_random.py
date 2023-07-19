import gym


if __name__ == "__main__":
    env = gym.make("CartPole-v1") # Create the environment

    total_reward = 0.0  
    total_steps = 0
    obs = env.reset()   # Reset the environment before starting
    ddd3 = env.action_space
    ddd4 = env.observation_space
    

    while True:
        action = env.action_space.sample()  # Sample random action
        obs, reward, done, _, x = env.step(action)  # Take action and store the outcomes
        # the code got updated now it return 5 items
        total_reward += reward
        total_steps += 1
        
        if done:
            break

    print("Episode done in %d steps, total reward %.2f" % (
        total_steps, total_reward))
    print(ddd3, ddd4)





