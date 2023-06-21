"""
Метеорологическая служба вашего города решила исследовать погоду новым способом.

Под температурой воздуха в конкретный день будем понимать максимальную
температуру в этот день.

Под хаотичностью погоды за n дней служба понимает количество дней,
в которые температура строго больше, чем в день до (если такой существует)
и в день после текущего (если такой существует). Например, если за 5 дней
максимальная температура воздуха составляла [1, 2, 5, 4, 8] градусов,
то хаотичность за этот период равна 2: в 3-й и 5-й дни выполнялись
описанные условия.

Определите по ежедневным показаниям температуры хаотичность погоды за этот период.

Заметим, что если число показаний n=1, то единственный день будет хаотичным.
"""

from typing import List

def get_weather_randomness(temperatures: List[int]) -> int:
    count = 0
    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            count += 1
    try:
        if temperatures[1]:
            if temperatures[0] > temperatures[1]:
                count += 1
            if temperatures[-2] < temperatures[-1]:
                count += 1
    except Exception:
        count = 1
    return count


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


def main():
    temperatures = read_input()
    print(get_weather_randomness(temperatures))


if __name__ == '__main__':
    main()