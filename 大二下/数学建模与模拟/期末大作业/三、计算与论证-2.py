import matplotlib.pyplot as plt
import math


def calculate_sums(x, y, x0, y0, p1, p2):
    sum1 = 0.0
    p1_y = p1 ** y
    for k in range(x0, x + 1):
        comb = math.comb(x, k)
        term = comb * (p1_y ** k) * ((1 - p1_y) ** (x - k))
        sum1 += term
    sum2 = 0.0
    p2_x = p2 ** x
    for k in range(y0, y + 1):
        comb = math.comb(y, k)
        term = comb * (p2_x ** k) * ((1 - p2_x) ** (y - k))
        sum2 += term
    return sum1, sum2

if __name__ == "__main__":
    def plot(x0, y0, p1, p2):
        results = list()
        for x in range(x0, x_max + 1):
            for y in range(y0, y_max + 1):
                sum1, sum2 = calculate_sums(x, y, x0, y0, p1, p2)
                if sum1 >= 0.9 and sum2 >= 0.9:
                    results.append((x, y))
        x_list = [result[0] for result in results]
        y_list = [result[1] for result in results]
        plt.xlim((0,x_max))
        plt.ylim((0,y_max))
        plt.scatter(x_list, y_list, label="Safe")
        plt.title(f'p₁={p1}    p₂={p2}\nx₀={x0}    y₀={y0}')
        plt.xlabel("x")
        plt.ylabel("y")
        plt.legend()
    x_max = y_max = 100

    plt.figure(figsize=(25,10))
    for i in range(1, 6):
        x0, y0 = 1, 1
        p1 = p2 = round(0.7 + 0.05 * i, 2)
        plt.subplot(2, 5, i)
        plot(x0, y0, p1, p2)
    for i in range(1, 6):
        x0, y0 = 5, 5
        p1 = p2 = round(0.7 + 0.05 * i, 2)
        plt.subplot(2, 5, 5 + i)
        plot(x0, y0, p1, p2)
    plt.tight_layout()
    plt.show()
    plt.close()

    x_max = y_max = 200
    plt.figure(figsize=(25,15))
    for i in range(1, 6):
        x0, y0 = 1, 1
        p1 = p2 = (0.95 + 0.01 * (i - 1))
        plt.subplot(3, 5, i)
        plot(x0, y0, p1, p2)
    for i in range(1, 6):
        x0, y0 = 5, 5
        p1 = p2 = (0.95 + 0.01 * (i - 1))
        plt.subplot(3, 5, 5 + i)
        plot(x0, y0, p1, p2)
    for i in range(1, 6):
        x0, y0 = 10, 10
        p1 = p2 = (0.95 + 0.01 * (i - 1))
        plt.subplot(3, 5, 10 + i)
        plot(x0, y0, p1, p2)
    plt.tight_layout()
    plt.show()
    plt.close()

    plt.figure(figsize=(25,10))
    for i in range(1, 6):
        x0, y0 = 1, 1
        p1 = 0.97
        p2 = (0.95 + 0.01 * (i - 1))
        plt.subplot(2, 5, i)
        plot(x0, y0, p1, p2)
    for i in range(1, 6):
        x0, y0 = 1, 1
        p1 = (0.95 + 0.01 * (i - 1))
        p2 = 0.97
        plt.subplot(2, 5, 5 + i)
        plot(x0, y0, p1, p2)
    plt.tight_layout()
    plt.show()
    plt.close()

    x_max = y_max = 100
    plt.figure(figsize=(25,10))
    for i in range(1, 6):
        x0 = 5
        y0 = 2 * i - 1
        p1 = p2 = 0.97
        plt.subplot(2, 5, i)
        plot(x0, y0, p1, p2)
    for i in range(1, 6):
        x0 = 2 * i - 1
        y0 = 5
        p1 = p2 = 0.97
        plt.subplot(2, 5, 5 + i)
        plot(x0, y0, p1, p2)
    plt.tight_layout()
    plt.show()