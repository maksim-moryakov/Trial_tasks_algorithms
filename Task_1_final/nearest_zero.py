"""
ID 88422183

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


def get_distance(houses: List[int], n: int) -> List[int]:
    distanse = [n] * n
    zero = [i for i in range(n) if houses[i] == 0]
    first_zero = zero[0]
    last_zero = zero[-1]

    for i in range(first_zero, n):
        if houses[i] != 0:
            distanse[i] = distanse[i - 1] + 1
        else:
            distanse[i] = 0
    for i in range(last_zero, first_zero, -1):
        if houses[i] != 0:
            distanse[i] = min(distanse[i], distanse[i + 1] + 1)
        else:
            distanse[i] = 0
    for i in range(first_zero - 1, -1, -1):
        distanse[i] = distanse[i + 1] + 1
    return distanse


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    houses = list(map(int, input().strip().split()))
    return houses, n


def main():
    houses, n = read_input()
    print(" ".join(map(str, get_distance(houses, n))))


if __name__ == '__main__':
    main()
