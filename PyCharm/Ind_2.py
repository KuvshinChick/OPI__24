#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import math
from queue import Queue
from threading import Thread

eps = 10 ** (-7)


def inf_sum(x, queue_1):
    a = (x ** 2) / 20
    S = a
    n = 1

    while math.fabs(a) > eps:
        a *= (x ** 2) / ((2 * n + 2) * (2 * n + 3))
        S += a
        n += 1

    queue_1.put(S)


def check_sum(x, queue_1):
    summa = queue_1.get()
    result = (math.e ** x - math.e ** (-x)) / 2
    print(f"The check is: {result}")
    print(f"The sum is: {summa}")


if __name__ == '__main__':
    queue_1 = Queue()
    x = 2

    thread1 = Thread(target=inf_sum(x, queue_1))
    thread2 = Thread(target=check_sum(x, queue_1))

    thread1.start()
    thread2.start()
