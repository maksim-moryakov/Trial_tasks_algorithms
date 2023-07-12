"""
Нужно реализовать класс StackMax, который поддерживает операцию определения
максимума среди всех элементов в стеке. Класс должен поддерживать операции
push(x), где x – целое число, pop() и get_max().

Формат ввода
В первой строке записано одно число n — количество команд,
которое не превосходит 10000. В следующих n строках идут команды.
Команды могут быть следующих видов:
- push(x) — добавить число x в стек;
- pop() — удалить число с вершины стека;
- get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max() нужно напечатать «None»,
для команды pop() — «error».

Формат вывода
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""

class StackMax:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        if len(self.max_stack) == 0:
            self.max_stack.append(x)
        elif x > self.max_stack[-1]:
            self.max_stack.append(x)
        else:
            self.max_stack.append(self.max_stack[-1])
        self.stack.append(x)            

    def pop(self):
        if self.is_empty():
            return "error"
        self.max_stack.pop()
        return self.stack.pop()

    def get_max(self):
        if self.is_empty():
            return "None"
        return self.max_stack[-1]
    
    def is_empty(self):
        return self.stack == []


def main():
    n = int(input())
    stack = StackMax()
    result = []

    for _ in range(n):
        command = input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == "pop":
            if stack.pop() == "error":
                result.append("error")
        elif command[0] == "get_max":
            result.append(stack.get_max())
    for i in result:
        print(i)


if __name__ == '__main__':
    main()