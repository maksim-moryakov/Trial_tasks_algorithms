"""
Рита по поручению Тимофея наводит порядок в правильных скобочных
последовательностях (ПСП), состоящих только из круглых скобок ().
Для этого ей надо сгенерировать все ПСП длины 2n в алфавитном порядке —–
алфавит состоит из ( и ) и открывающая скобка идёт раньше закрывающей.

Помогите Рите —– напишите программу, которая по заданному n выведет все
ПСП в нужном порядке.

Формат ввода
На вход функция принимает n — целое число от 0 до 10.

Формат вывода
Функция должна напечатать все возможные скобочные последовательности
заданной длины в алфавитном (лексикографическом) порядке.
"""

def generate_bracket_sequences(n):
    result = []
    generate_sequences("", 0, 0, n, result)
    return result

def generate_sequences(sequence, open_count, close_count, n, result):
    if len(sequence) == 2 * n:
        result.append(sequence)
        return
    
    if open_count < n:
        generate_sequences(sequence + "(", open_count + 1, close_count, n, result)
    
    if close_count < open_count:
        generate_sequences(sequence + ")", open_count, close_count + 1, n, result)


n = int(input())
sequences = generate_bracket_sequences(n)
sequences.sort()
for sequence in sequences:
	print(sequence)