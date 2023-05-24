#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import threading

"""
Вычисление чисел Фибоначчи: Производитель генерирует числа Фибоначчи, а потребитель вычисляет и выводит 
в консоль сумму первых n чисел этой последовательности. Когда список будет заполнен, 
потребитель вычислит сумму первых n чисел и выведет ее в консоль.
"""

cv = threading.Condition()  # создание объекта условной переменной
buffer_full = False  # флаг заполнения списка


# Функция для производителя (генератора чисел Фибоначчи)
def fibonacci_producer(buffer, n):
    global buffer_full  # объявление глобальной переменной
    a, b = 0, 1
    with cv:
        for i in range(n):
            while buffer_full:
                cv.wait()  # ждем, когда потребитель уведомит о том, что список заполнен
            buffer.append(b)  # добавляем очередной элемент в список
            a, b = b, a + b  # вычисляем следующее число Фибоначчи
            if len(buffer) == n:
                buffer_full = True  # список заполнен, меняем значение флага
                cv.notify_all()  # уведомляем остальные потоки о том, что список заполнен


# Функция для потребителя (вычисления суммы первых n элементов последовательности Фибоначчи)
def fibonacci_consumer(buffer, n):
    with cv:
        while not buffer_full:
            cv.wait()  # ждем, пока производитель заполнит список
        print("The sum of the first", n, "numbers in the Fibonacci sequence is", sum(buffer))
        cv.notify_all()


buffer = []  # создание списка для хранения чисел
producer = threading.Thread(target=fibonacci_producer, args=(buffer, 12))  # создание производителя
consumer = threading.Thread(target=fibonacci_consumer, args=(buffer, 12))  # создание потребителя

# Запуск потоков
producer.start()
consumer.start()
