import threading

"""
Вычисление чисел Фибоначчи: Производитель генерирует числа Фибоначчи, а потребитель вычисляет и выводит 
в консоль сумму первых n чисел этой последовательности. Когда список будет заполнен, 
потребитель вычислит сумму первых n чисел и выведет ее в консоль.
"""


# Класс для производителя (генератора чисел Фибоначчи)
class FibonacciProducer(threading.Thread):
    def __init__(self, buffer, n):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.n = n

    def run(self):
        a, b = 0, 1
        for i in range(self.n):
            self.buffer.append(b)
            a, b = b, a + b


# Класс для потребителя (вычисления суммы первых n элементов последовательности Фибоначчи)
class FibonacciConsumer(threading.Thread):
    def __init__(self, buffer, n):
        threading.Thread.__init__(self)
        self.buffer = buffer
        self.n = n

    def run(self):
        total = 0
        while True:
            if len(self.buffer) == self.n:
                for num in self.buffer:
                    total += num
                print("The sum of the first", self.n, "numbers in the Fibonacci sequence is", total)
                break


# Создание списка для хранения чисел
buffer = []

# Создание объектов производителя и потребителя
producer = FibonacciProducer(buffer, 10)
consumer = FibonacciConsumer(buffer, 10)

# Запуск потоков
producer.start()
consumer.start()
