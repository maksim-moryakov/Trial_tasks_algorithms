"""
Гоша любит играть в игру «Подпоследовательность»: даны 2 строки,
и нужно понять, является ли первая из них подпоследовательностью второй.
Когда строки достаточно длинные, очень трудно получить ответ на этот вопрос,
просто посмотрев на них. Помогите Гоше написать функцию, которая решает эту задачу.

Формат ввода
В первой строке записана строка s.
Во второй —- строка t.
Обе строки состоят из маленьких латинских букв, длины строк не
превосходят 150000. Строки не могут быть пустыми.

Формат вывода
Выведите True, если s является подпоследовательностью t, иначе —– False.
"""

sequence_1 = list(input())
sequence_2 = list(input())


def is_subsequence(subsequence, sequence):
    if len(subsequence) > len(sequence):
        return False
    left = 0
    for character in subsequence:
        try:
            right = sequence.index(character, left)
        except:
            return False
        left = right + 1
    return True


print(is_subsequence(sequence_1, sequence_2))
