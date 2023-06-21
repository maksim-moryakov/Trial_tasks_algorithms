"""
Вася реализовал функцию, которая переводит целое число из десятичной системы
в двоичную. Но, кажется, она получилась не очень оптимальной.

Попробуйте написать более эффективную программу.
"""


def to_binary(number: int) -> str:
    binary = ''
    if number == 0:
        binary = '0'
    while number > 0:
        binary = str(number % 2) + binary
        number //= 2
    return binary

def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))