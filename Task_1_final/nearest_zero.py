"""
ID 88630784

Тимофей ищет место, чтобы построить себе дом. 
Улица, на которой он хочет жить, имеет длину n, то есть состоит из n
одинаковых идущих подряд участков. Каждый участок либо пустой, либо на
нём уже построен дом.

Общительный Тимофей не хочет жить далеко от других людей на этой улице.
Поэтому ему важно для каждого участка знать расстояние до ближайшего пустого
участка. Если участок пустой, эта величина будет равна нулю — расстояние
до самого себя.

Пустые участки обозначены нулями.
"""

from typing import List, Tuple


def get_distance(houses: List[int]) -> List[int]:
    n = len(houses)
    distance = [n] * n
    zero = [i for i in range(n) if houses[i] == 0]
    first_zero = zero[0]
    last_zero = zero[-1]

    for i in range(first_zero, n):
        if houses[i] != 0:
            distance[i] = distance[i - 1] + 1
        else:
            distance[i] = 0
    for i in range(last_zero, first_zero, -1):
        if houses[i] != 0:
            distance[i] = min(distance[i], distance[i + 1] + 1)
        else:
            distance[i] = 0
    for i in range(first_zero - 1, -1, -1):
        distance[i] = distance[i + 1] + 1
    return distance


def main() -> Tuple[List[int], int]:
    input() 
    houses = [int(x) for x in input().strip().split() if x != 0]
    return get_distance(houses)


if __name__ == '__main__':
    result = main()
    print(" ".join(map(str, result)))
