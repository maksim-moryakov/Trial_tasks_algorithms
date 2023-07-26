"""
Вечером ребята решили поиграть в игру «Большое число».
Даны числа. Нужно определить, какое самое большое число можно из них составить.

Формат ввода
В первой строке записано n — количество чисел. Оно не превосходит 100.
Во второй строке через пробел записаны n неотрицательных чисел, 
каждое из которых не превосходит 1000.

Формат вывода
Нужно вывести самое большое число, которое можно составить из данных чисел.
"""

from typing import List


def comparator(number_1, number_2):
    if len(number_1) == len(number_2):
        return number_1 > number_2
    else:
        sum_1 = number_1 + number_2
        sum_2 = number_2 + number_1
        return sum_1 > sum_2


def bigger_number(numbers, comparator):
    for i in range(len(numbers)):
        item = numbers[i]
        while i > 0 and comparator(item, numbers[i - 1]):
            numbers[i] = numbers[i - 1]
            i -= 1
        numbers[i] = item
    return numbers


def read_input() -> List:
    _ = int(input())
    numbers = [x for x in input().split()]
    return numbers


def main():
    numbers = read_input()
    print(''.join(bigger_number(numbers, comparator)))


if __name__ == '__main__':
    main()