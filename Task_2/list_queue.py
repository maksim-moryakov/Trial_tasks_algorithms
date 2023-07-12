"""
Реализацией класс Stack. 
Любимый вариант очереди Тимофея — очередь, написанная с использованием
связного списка. Помогите ему с реализацией. Очередь должна поддерживать
выполнение трёх команд:
- get() — вывести элемент, находящийся в голове очереди, и удалить его.
Если очередь пуста, то вывести «error».
- put(x) — добавить число x в очередь
- size() — вывести текущий размер очереди

Формат ввода:
В первой строке записано количество команд n — целое число,
не превосходящее 1000. В каждой из следующих n строк записаны команды
по одной строке.

Формат вывода:
Выведите ответ на каждый запрос по одному в строке.
"""


class Queue:
    def __init__(self):
        self.queue = []
    
    def get(self):
        if self.is_empty():
            return 'error'
        else:
            return self.queue.pop(0)

    def put(self, item):
        self.queue.append(item)
        return self.queue[-1]

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0


def main():
    n = int(input())
    queue = Queue()
    result = []

    for _ in range(n):
        command = input().split()
        if command[0] == "get":
            result.append(queue.get())
        elif command[0] == "put":
            queue.put(int(command[1]))
        elif command[0] == "size":
            result.append(queue.size())
    for i in result:
        print(i)


if __name__ == "__main__":
    main()