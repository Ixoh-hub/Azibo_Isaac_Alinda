import numpy as np
import random

# Environment settings
road_length = 11  # 0 to 10
actions = [0, 1, 2]  # 0=left, 1=stay, 2=right
goal = 10

# Q-table: state x actions
Q = np.zeros((road_length, len(actions)))

# Hyperparameters
episodes = 1000
learning_rate = 0.1
discount = 0.9
epsilon = 0.2  # exploration rate

# Training loop
for episode in range(episodes):
    state = 0  # start position
    steps = 0  # training progress
    
    while state != goal:
        # Epsilon-greedy action selection
        if random.uniform(0, 1) < epsilon:
            action = random.choice(actions)
        else:
            action = np.argmax(Q[state])
        
        # Environment response
        if action == 0:
            next_state = max(0, state - 1)
        elif action == 2:
            next_state = min(road_length - 1, state + 1)
        else:
            next_state = state

        # Reward system
        reward = 100 if next_state == goal else -1

        # Q-learning update
        Q[state, action] = Q[state, action] + learning_rate * (
            reward + discount * np.max(Q[next_state]) - Q[state, action]
        )

        state = next_state
        steps += 1
        
        # episode summary
        if episode % 100 == 0 or episode == episodes -1:
            print(f"Episode {episode + 1}/{episodes} finished in {steps} steps.")

# Test the trained agent
state = 0
steps = [state]

while state != goal:
    action = np.argmax(Q[state])
    
    if action == 0:
        state = max(0, state - 1)
    elif action == 2:
        state = min(road_length - 1, state + 1)
    # If action is 1 (stay), state doesn't change
    
    steps.append(state)

print("Agent Path to Goal:", steps)
print("\nFinal Q-table:")
print(np.round(Q,2))