"""
ID 88987635

Гоша реализовал структуру данных Дек, максимальный размер которого определяется
заданным числом. Методы push_back(x), push_front(x), pop_back(), pop_front()
работали корректно. Но, если в деке было много элементов, программа работала
очень долго. Дело в том, что не все операции выполнялись за O(1).
Помогите Гоше! Напишите эффективную реализацию.
Внимание: при реализации используйте кольцевой буфер.
"""

from typing import Tuple


class StackOverflowError(Exception):
    def __init__(self):
        pass


class NoItemsError(Exception):
    def __init__(self):
        pass


class Desk:
    def __init__(self, max_size):
        self.__buffer = [None] * max_size
        self.__start = 0
        self.__end = 0
        self.__size = 0
        self.__max_size = max_size

    def is_empty(self):
        return self.__size == 0

    def is_full(self):
        return self.__size == self.__max_size

    def push_back(self, item):
        if self.is_full():
            raise StackOverflowError
        
        self.__buffer[self.__end] = item
        self.__end = (self.__end + 1) % self.__max_size
        self.__size += 1


    def push_front(self, item):
        if self.is_full():
            raise StackOverflowError
        self.__start = (self.__start - 1) % self.__max_size
        self.__buffer[self.__start] = item
        self.__size += 1


    def pop_back(self):
        if self.is_empty():
            raise NoItemsError
        self.__end = (self.__end - 1) % self.__max_size
        item = self.__buffer[self.__end]
        self.__size -= 1
        return item


    def pop_front(self):
        if self.is_empty():
            raise NoItemsError
        item = self.__buffer[self.__start]
        self.__start = (self.__start + 1) % self.__max_size
        self.__size -= 1
        return item


def main() -> Tuple[int, int]:
    n = int(input())
    max_size = int(input())
    deque = Desk(max_size)

    for _ in range(n):
        try:
            item = input().split()
            if len(item) == 1:
                print(getattr(deque, item[0])())
            else:
                getattr(deque, item[0])(item[1])
        except (StackOverflowError, NoItemsError):
            print("error")


if __name__ == '__main__':
    main()
