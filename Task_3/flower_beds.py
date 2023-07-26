"""
Алла захотела, чтобы у неё под окном были узкие клумбы с тюльпанам. 
На схеме земельного участка клумбы обозначаются просто горизонтальными
отрезками, лежащими на одной прямой. Для ландшафтных работ было нанято
n садовников. Каждый из них обрабатывал какой-то отрезок на схеме.
Процесс был организован не очень хорошо, иногда один и тот же отрезок или
его часть могли быть обработаны сразу несколькими садовниками. 
Таким образом, отрезки, обрабатываемые двумя разными садовниками,
сливаются в один. Непрерывный обработанный отрезок затем станет клумбой.
Нужно определить границы будущих клумб.

Формат ввода
В первой строке задано количество садовников n. Число садовников не превосходит 
100000. В следующих n строках через пробел записаны координаты клумб в формате:
start end, где start —– координата начала, end —– координата конца.
Оба числа целые, неотрицательные и не превосходят 107. start строго меньше, чем end.

Формат вывода
Нужно вывести координаты каждой из получившихся клумб в отдельных строках.
Данные должны выводиться в отсортированном порядке —– сначала клумбы
с меньшими координатами, затем —– с бОльшими.
"""

n = int(input())
s = []
for i in range(n):
    seq = [int(x) for x in input().split()]
    s.append(seq)
s.sort()
for i in range(len(s)-1):
    if s[i+1][0] <= s[i][1]:
        tmp = s[i][1] < s[i+1][1]
        s[i+1][0] = s[i][0]
        s[i+1][1] = s[i+tmp][1]
        s[i] = []
for j in range(len(s)):
    if s[j]:
        print(*s[j])