"""
Реализуйте класс StackMaxEffective, поддерживающий операцию определения
максимума среди элементов в стеке. Сложность операции должна быть O(1).
Для пустого стека операция должна возвращать None. При этом push(x) и pop()
также должны выполняться за константное время.

Формат ввода:
В первой строке записано одно число — количество команд,
оно не превосходит 100000. Далее идут команды по одной в строке.
Команды могут быть следующих видов:
- push(x) — добавить число x в стек;
- pop() — удалить число с вершины стека;
- get_max() — напечатать максимальное число в стеке;
Если стек пуст, при вызове команды get_max нужно напечатать «None»,
для команды pop — «error».

Формат вывода:
Для каждой команды get_max() напечатайте результат её выполнения.
Если стек пустой, для команды get_max() напечатайте «None».
Если происходит удаление из пустого стека — напечатайте «error».
"""

class StackMaxEffective:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return "error"
        x = self.stack.pop()
        if x == self.max_stack[-1]:
            self.max_stack.pop()

    def get_max(self):
        if not self.max_stack:
            return None
        return self.max_stack[-1]


def main():
    n = int(input())
    stack = StackMaxEffective()
    result = []

    for _ in range(n):
        command = input().split()
        if command[0] == "push":
            stack.push(int(command[1]))
        elif command[0] == 'pop':
            if stack.pop() == 'error':
                result.append('error')
        elif command[0] == 'get_max':
            result.append(stack.get_max())
    for i in result:
        print(i)

if __name__ == '__main__':
    main()
        