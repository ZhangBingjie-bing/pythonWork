import matplotlib.pyplot as plt
import random


def create_random(func):
    def XYrandom(m, n, num):
        # 随机生成数，且在范围内
        x_lable = [random.uniform(m, n) for t in range(num)]
        y_lable = [random.uniform(m, n) for t in range(num)]
        func(x_lable, y_lable, num)
    return XYrandom

@create_random
def scatter(x, y, num):
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.scatter(x, y, c = '#DC143C')
    plt.grid(True)
    title = str(num) + ' Random Scatter by zbj'
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    scatter(20, 50, 100)
