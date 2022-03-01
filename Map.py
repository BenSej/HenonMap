import matplotlib.pyplot as plt
import numpy as np
import math

e = 10**-8
x = [np.random.random()]
x_prime = [x[0] + e]
abs_difference = [abs(x_prime[0] - x[0])]
generations = [0]
n = 1


def f(a, x_n):
    return a * math.sin(math.pi * x_n)


while n < 100:
    generations.append(n)
    x.append(f(.9, x[n - 1]))
    x_prime.append(f(.9, x_prime[n-1]))
    abs_difference.append(abs(x_prime[n] - x[n]))
    n += 1


plt.plot(generations,x)
plt.plot(generations, x_prime)
#plt.plot(generations, abs_difference)
plt.xlabel('Generations')
plt.ylabel('x')
plt.title('Sinusoidal Map')
plt.yscale('log')
#print(np.interp(50, generations, abs_difference))
plt.show()
