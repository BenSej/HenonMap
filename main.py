import matplotlib.pyplot as plt
import numpy as np


def plot(a):
    x_1 = [.2]
    generations = [0]
    n = 0
    while n < 19:
        generations.append(n + 1)

        if 0 < x_1[n] < 0.5:
            x_1.append(2 * a * x_1[n])
        elif .5 < x_1[n] < 1:
            x_1.append(2 * a * (1 - x_1[n]))
        n += 1

    plt.plot(generations, x_1)
    plt.xlabel('Generations')
    plt.ylabel('x')
    plt.title('Tent Map')
    plt.show()

# plot(.7)
# plot(.4)


def bifurcation():
    X = []
    alpha = []
    n = 0
    while n < 10000:
        a = 1.5 / 10000 * n
        alpha.append(a)
        x = np.random.random()
        i = 0
        while i < 1000:
            if 0 < x < .5:
                x = 2 * a * x
            elif .5 < x < 1:
                x = 2 * a * (1 - x)
            i += 1
        X.append(x)
        n += 1

    plt.scatter(alpha, X, s=.5)
    plt.xlabel('alpha')
    plt.ylabel('x')
    plt.title('Tent Map')
    plt.show()

bifurcation()
