"""
Помогите Васе написать код функции, вычисляющей y = ax2 + bx + c.
Напишите программу, которая будет по коэффициентам a, b, c и числу x выводить
значение функции в точке x.
"""

def evaluate_function(a: int, b: int, c: int, x: int) -> int:
    return (a * x ** 2) + (b * x) + c


def main():
    a, x, b, c = map(int, input().strip().split())
    print(evaluate_function(a, b, c, x))


if __name__ == '__main__':
    main()