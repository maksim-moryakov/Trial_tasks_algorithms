"""
ID 88986890

B. Калькулятор

"""

import operator
from typing import List


OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '/': operator.floordiv,
    '*': operator.mul
}


class NoItemsError(Exception):
    def __init__(self):
        pass


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(int(item))

    def pop(self):
        if self.is_empty():
            raise NoItemsError("error")
        else:
            return self.items.pop()


def main(command: List[str]) -> int:
    stack = Stack()
    for item in command:
        if item in OPERATORS:
            x, y = stack.pop(), stack.pop()
            stack.push(OPERATORS[item](y, x))
        else:
            stack.push(item)  
    return stack.pop()


if __name__ == '__main__':
    command = input().split()
    print(main(command))
