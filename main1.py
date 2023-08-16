import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f_1(x, A, B, alpha, beta):
    return beta * B ** alpha / (x + A) ** (alpha + 1)


def plot():
    plt.figure()

    x0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    y0 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    plt.scatter(x0[:], y0[:], 25, "red")

    A1, B1, alpha1, beta1 = optimize.curve_fit(f_1, x0, y0)[0]
    print("A     = {:.14f}".format(A1))
    print("B     = {:.14f}".format(B1))
    print("alpha = {:.14f}".format(alpha1))
    print("beta  = {:.14f}".format(beta1))
    x1 = np.arange(0.01, 11, 0.01)
    y1 = f_1(x1, A1, B1, alpha1, beta1)
    print(x1)
    print(y1)
    plt.plot(x1, y1, "blue")

    plt.title("curve")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()


if __name__ == '__main__':
    plot()
