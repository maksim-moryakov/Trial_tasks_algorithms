"""
Напишите функцию solution, которая принимает на вход голову списка и номер
удаляемого дела и возвращает голову обновлённого списка.

Формат ввода
Функция принимает голову списка и индекс элемента, который надо удалить
(нумерация с нуля). Список содержит не более 5000  элементов.
Список не бывает пустым.

Формат вывода
Верните голову списка, в котором удален нужный элемент.
"""

LOCAL = True

if LOCAL:
    class Node:  
        def __init__(self, value, next_item=None):  
            self.value = value  
            self.next_item = next_item


def solution(node, idx):
    if idx == 0:
        return node.next_item
    
    current = node
    for i in range(idx-1):
        if current.next_item is None:
            return node
        current = current.next_item
    
    if current.next_item is not None:
        current.next_item = current.next_item.next_item
    
    return node

def test():
    node3 = Node("node3", None)
    node2 = Node("node2", node3)
    node1 = Node("node1", node2)
    node0 = Node("node0", node1)
    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None

if __name__ == '__main__':
    test()