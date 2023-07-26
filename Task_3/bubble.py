"""
Чтобы выбрать самый лучший алгоритм для решения задачи, Гоша продолжил изучать
разные сортировки. 
На очереди сортировка пузырьком — https://ru.wikipedia.org/wiki/Сортировка_пузырьком

Её алгоритм следующий (сортируем по неубыванию):

1. На каждой итерации проходим по массиву, поочередно сравнивая пары соседних 
    элементов. Если элемент на позиции i больше элемента на позиции i + 1,
    меняем их местами. После первой итерации самый большой элемент всплывёт
    в конце массива. 
2. Проходим по массиву, выполняя указанные действия до тех пор,
    пока на очередной итерации не окажется, что обмены больше не нужны,
    то есть массив уже отсортирован.
3. После не более чем n – 1 итераций выполнение алгоритма заканчивается,
    так как на каждой итерации хотя бы один элемент оказывается на правильной позиции.

Формат ввода
В первой строке на вход подаётся натуральное число n — длина массива, 2 ≤ n ≤ 1000.
Во второй строке через пробел записано n целых чисел.
Каждое из чисел по модулю не превосходит 1000.

Обратите внимание, что считывать нужно только 2 строки: значение n и входной массив.

Формат вывода
После каждого прохода по массиву, на котором какие-то элементы меняются местами,
выводите его промежуточное состояние.
Таким образом, если сортировка завершена за k меняющих массив итераций,
то надо вывести k строк по n чисел в каждой — элементы массива после каждой из итераций.
Если массив был изначально отсортирован, то просто выведите его.
"""

def bubble_sort(seq):
    flag_1 = True
    n = len(seq) - 1
    for j in range(n):
        flag_2 = False
        for i in range(n - j):
            if seq[i] > seq[i + 1]:
                flag_1 = False
                flag_2 = True
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
        if flag_2:
            print(*seq)
    if flag_1:
        print(*seq)


_ = input()
seq = [int(x) for x in input().split()]

bubble_sort(seq)