"""
ID 88457274

«Тренажёр для скоростной печати» представляет собой квадратную клавиатуру
из шестнадцати клавиш размером 4x4. На каждой клавише может быть изображена
либо точка, либо цифра от 1 до 9.

Занятие на тренажёре делится на раунды :
- каждый раунд состоит из нескольких игр;
- в разных раундах число игр может быть разным;
- номер каждой игры в раунде обозначается счётчиком t.

Для каждого раунда на клавишах устанавливаются определённые значения,
которые остаются неизменными в течение всех игр раунда.
"""


from typing import List, Tuple


def get_max_points(matrix: List[str], k: int) -> int:
    points = 0
    count = [0] * 16
    for number in matrix:
        if number != '.':
            count[int(number)] += 1
    points = sum(1 for number in count if 0 < number <= k * 2)
    return points


def main() -> Tuple[List[str], int]:
    k = int(input())
    matrix = [i for i in range(4) for i in input().strip()]
    print(get_max_points(matrix, k))


if __name__ == '__main__':
    main()