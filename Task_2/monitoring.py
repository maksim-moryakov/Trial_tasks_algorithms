"""
Есть матрица размера m × n. Нужно написать функцию, которая её транспонирует.
Транспонированная матрица получается из исходной заменой строк на столбцы.

Формат ввода
В первой строке задано число n — количество строк матрицы.
Во второй строке задано m — число столбцов, m и n не превосходят 1000. 
В следующих n строках задана матрица. Числа в ней не превосходят по модулю 1000.

Формат вывода
Напечатайте транспонированную матрицу в том же формате, который задан во
входных данных. Каждая строка матрицы выводится на отдельной строке,
элементы разделяются пробелами.
"""

from typing import List

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix

n = int(input())
m = int(input())

matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

transposed_matrix = transpose_matrix(matrix)

for row in transposed_matrix:
    print(' '.join(map(str, row)))
