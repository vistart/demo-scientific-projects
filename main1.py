import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def f_1(x, A, B, alpha, beta):
    return beta * B ** alpha / (x + A) ** (alpha + 1)


def plot():
    plt.figure()

    // 函数参数（x）值列表。
    x0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    // 函数结果（y）值列表，数量必须与参数值列表一致，否则会无法计算。另，请自行保证参数和结果合理性，curve_fit() 不保证计算出正确结果。
    y0 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

    // 把参数列表和结果列表作为坐标画在图上。前两个参数表示坐标x和y序列，第三个参数表示点大小，第四个参数表示点颜色。
    plt.scatter(x0[:], y0[:], 25, "red")

    // curve_fit() 返回值第0维即为我们想要的拟合参数。
    A1, B1, alpha1, beta1 = optimize.curve_fit(f_1, x0, y0)[0]
    // 输出这四个参数，小数点后保留14位。
    print("A     = {:.14f}".format(A1))
    print("B     = {:.14f}".format(B1))
    print("alpha = {:.14f}".format(alpha1))
    print("beta  = {:.14f}".format(beta1))

    // 将求出的四个参数代回函数中，并画出指定区间的散点图，由于点较为密集，可以视作是曲线图。
    x1 = np.arange(0.01, 13, 0.01)
    y1 = f_1(x1, A1, B1, alpha1, beta1)

    // 输出参数和代回函数后得出的结果
    print(x1)
    print(y1)

    // 在同一幅图中画出带入函数得出的坐标散点图，颜色为蓝色。
    plt.plot(x1, y1, "blue")

    // 图片标题
    plt.title("curve")

    // x 轴名称
    plt.xlabel("x")

    // y 轴名称
    plt.ylabel("y")

    // 展示图片
    plt.show()


if __name__ == '__main__':
    plot()
