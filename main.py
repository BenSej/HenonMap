import math

import numpy as np
import matplotlib.pyplot as plt


def g(x, y, z):
    return -.1*z - 4*y + math.cos(x)

def f(x, t, v):
    k1 = g(0, 0, 0)*t
    k2 = g()*t
    k3 = g()*t
    k4 = g()*t
    y_next = x + 1/6(k1 + 2*k2 + 2*k3 + k4)


def henonMap(x, y, a, b):
    x_next = y + 1 - a * x**2
    y_next = b * x
    return x_next, y_next


iterations = 10000
X = np.zeros(iterations + 1)
Y = np.zeros(iterations + 1)

X[0], Y[0] = 0, 0

for i in range(iterations):
    x_next, y_next = henonMap(X[i], Y[i], 1.4, 0.3)
    X[i + 1] = x_next
    Y[i + 1] = y_next

plt.plot(X, Y, '^', markersize=0.1, color='black')
plt.axis('off')
plt.show()

X = np.zeros(iterations + 1)
Y = np.zeros(iterations + 1)
X[0], Y[0] = 0.1, 0.1
for i in range(iterations):
    x_next, y_next = henonMap(X[i], Y[i], 1.4, 0.3)
    X[i + 1] = x_next
    Y[i + 1] = y_next

plt.plot(X, Y, '^', markersize=0.1, color='black')
plt.axis('off')
plt.show()
plt.close()


def g(x, y, z):
    return -.1*z - 4*y + math.cos(x)
def f(x, y, z):
    return z
def rungeKutta(x0, y0, z0, h):
    for i in range(1, 10):
        k0 = h * f(x0, y0, z0)
        l0 = h * g(x0, y0, z0)
        k1 = h * f(x0 + h/2, y0 + k0/2, z0 + l0/2)
        l1 = h * g(x0 + h/2, y0 + k0/2, z0 + l0/2)
        k2 = h * f(x0 + h/2, y0 + k1/2, z0 + l1/2)
        l2 = h * g(x0 + h/2, y0 + k1 / 2, z0 + l1/2)
        k3 = h * f(x0 + h / 2, y0 + k2 / 2, z0 + l2 / 2)
        l3 = h * g(x0 + h / 2, y0 + k2 / 2, z0 + l2 / 2)

        y_next = y0 + (1.0 / 6.0) * (k0 + 2*k1 + 2*k2 + k3)
        z_next = z0 + (1.0 / 6.0) * (l0 + 2*l1 + l3)
    return y_next, z_next


X = np.zeros(iterations + 1)
Y = np.zeros(iterations + 1)
Z = np.zeros(iterations + 1)
X[0], Y[0], Z[0] = 0, 0, 0
for i in range(iterations):
    y_next, z_next = rungeKutta(X[i], Y[i], Z[i], 0.1)
    Y[i + 1] = y_next
    Z[i + 1] = z_next

plt.plot(Y, Z, '^', markersize=0.1, color='black')
plt.show()
