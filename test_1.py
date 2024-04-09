from math import sqrt


def is_prime(num: int)-> bool:
    """Функция для проверки, является ли число простым"""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def prime_numbers_in_range(minimum:int, maximum:int)-> list:
    """Функция для получения списка всех простых чисел в заданном диапазоне"""
    prime_numbers = []
    for num in range(minimum, maximum + 1):
        if is_prime(num):
            prime_numbers.append(num)
    return prime_numbers


class Point:
    """ Класс для работы с координатами """

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance_point(self, other_point):
        dx = self.x - other_point.x
        dy = self.y - other_point.y
        return sqrt(dx ** 2 + dy ** 2)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return self.x, self.y


def custom_sort(strings):
    """ Функция сортировкии строк """
    return sorted(strings, key=len) + sorted(strings, key=len, reverse=True)
