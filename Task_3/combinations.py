"""
На клавиатуре старых мобильных телефонов каждой цифре соответствовало
несколько букв. Примерно так:
2:'abc',
3:'def',
4:'ghi',
5:'jkl',
6:'mno',
7:'pqrs',
8:'tuv',
9:'wxyz'

Вам известно в каком порядке были нажаты кнопки телефона, без учета повторов.
Напечатайте все комбинации букв, которые можно набрать такой
последовательностью нажатий.

Формат ввода
На вход подается строка, состоящая из цифр 2-9 включительно. 
Длина строки не превосходит 10 символов.

Формат вывода
Выведите все возможные комбинации букв через пробел.
"""

def read_input():
    s = input()
    code = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    arr = []
    for item in s:
        arr.append(code[item])
    return arr


def combinations(arr):
    res = []
    if len(arr) == 0:
        return ['']
    else:
        word = arr.pop()
        for combination in combinations(arr):
            for char in word:
                res.append(combination + char)
    return res


def main() -> None:
    arr = read_input()
    print(*combinations(arr))


if __name__ == '__main__':
    main()
