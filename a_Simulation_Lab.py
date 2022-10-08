import matplotlib.pyplot as plt
import numpy as np
from scipy.special import i0
from scipy.stats import norm
import statistics


def drawTriangle():
    plt.hist(np.random.triangular(-3, 0, 8, 100000), bins=200, density=True)
    plt.show()


def drawPlot():
    s = np.random.uniform(-1, 0, 1000)
    count, bins, ignored = plt.hist(s, 15, density=True)
    plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
    plt.show()


def drawHistogram():
    mu, kappa = 0.0, 4.0  # mean and dispersion
    s = np.random.vonmises(mu, kappa, 1000)

    plt.hist(s, 50, density=True)
    x = np.linspace(-np.pi, np.pi, num=51)
    y = np.exp(kappa * np.cos(x - mu)) / (2 * np.pi * i0(kappa))
    plt.plot(x, y, linewidth=2, color='r')
    plt.show()


def drawWald():
    plt.hist(np.random.wald(3, 2, 100000), bins=200, density=True)
    plt.show()


def drawWeibul():
    def weib(x, n, a):
        return (a / n) * (x / n) ** (a - 1) * np.exp(-(x / n) ** a)

    a = 5.  # shape
    s = np.random.weibull(a, 1000)
    x = np.arange(1, 100.) / 50.

    count, bins, ignored = plt.hist(np.random.weibull(5., 1000))
    x = np.arange(1, 100.) / 50.
    scale = count.max() / weib(x, 1., 5.).max()
    plt.plot(x, weib(x, 1., 5.) * scale)
    plt.show()


def drawNormalDistribution():
    x_axis = np.arange(-20, 20, 0.01)

    mean = statistics.mean(x_axis)
    sd = statistics.stdev(x_axis)

    plt.plot(x_axis, norm.pdf(x_axis, mean, sd))
    plt.show()


if __name__ == '__main__':
    # drawTriangle()
    # drawPlot()
    # drawHistogram()
    # drawWald()
    # drawWeibul()
    drawNormalDistribution()
