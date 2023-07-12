"""
Напишите функцию solution, определяющую индекс первого вхождения передаваемого
ей на вход значения в связном списке, если значение присутствует.
Формат ввода:
Функция на вход принимает голову односвязного списка и элемент,
который нужно найти. Длина списка не превосходит 10000 элементов.
Список не бывает пустым.
"""

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item

def solution(node, elem):
    current = node
    idx = 0
    
    while current is not None:
        if current.value == elem:
            return idx
        current = current.next_item
        idx += 1
    
    return -1

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    idx = solution(node0, "node2")
    assert idx == 2

if __name__ == '__main__':
    test()