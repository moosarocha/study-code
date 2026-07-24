import numpy as np
from matplotlib import pyplot as plt

def steepest_descent(initial_guess, learning_rate, iterations):
    x = [initial_guess[0]]*len(learning_rate)
    y = [initial_guess[1]]*len(learning_rate)

    # fx = [[]]*len(learning_rate)
    fx = [[] for _ in range(len(learning_rate))]
    print(fx)
    for i in range(iterations):
        for j , lr in enumerate(learning_rate):
            gradient = np.array([2 * (x[j] - 2), 2 * (y[j] + 1)])  # Gradient of the function
            update = -lr * gradient  # Update step
            x[j], y[j] = x[j] + update[0], y[j] + update[1]  # Update parameters

            _fx = (x[j] - 2)**2 + (y[j] + 1)**2
            # print(f"Iteration {i+1}: x = {x:.4f}, y = {y:.4f}, f(x, y) = {_fx:.4f}")
            fx[j].append(_fx)
    return x, y, fx

initial_guess = [0, 0]
learning_rate = [0.1, 0.01, 0.001]
iterations = 1000

lx, ly, fx = steepest_descent(initial_guess, learning_rate, iterations)
x = range(len(fx[0]))

colors = ['black','blue','red']
for i, lr in enumerate(learning_rate):
    plt.plot(x, fx[i], color=colors[i])
plt.show()