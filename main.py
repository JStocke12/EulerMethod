import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import root


def forward_euler(x_0,dt,f=lambda x: -x):
    xs = [x_0]
    for i in range(10000):
        xs.append(xs[-1] + dt * f(xs[-1]))
    return xs

def backward_euler(x_0,dt,f=lambda x: -x):
    xs = [x_0]
    for i in range(10000):
        xs.append(root(lambda x:list(xs[-1]+dt*f(x)-x), xs[-1]).x)
    return xs

def mixed_euler(x_0,dt,f=lambda x: -x):
    xs = [x_0]
    for i in range(1000):
        xs.append((xs[-1] + dt * f(xs[-1]) + root(lambda x: list(xs[-1] + dt * f(x) - x), xs[-1]).x)/2)
    return xs

def main():
    #plt.plot(forward_euler(1,0.01,-1))
    #plt.plot(mixed_euler([0,1], 0.01, lambda x: np.array([np.sin(x[1]),x[0]])))
    plt.plot(backward_euler([3, 3], 0.01, lambda x: np.array([(2/3)*x[0]-(3/4)*x[0]*x[1], x[0]*x[1]-x[1]])))

    plt.show()

if __name__ == '__main__':
    main()
