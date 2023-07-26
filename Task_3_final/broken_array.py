"""
ID 89256545

Алла ошиблась при копировании из одной структуры данных в другую.
Она хранила массив чисел в кольцевом буфере. Массив был отсортирован по возрастанию,
и в нём можно было найти элемент за логарифмическое время.
Алла скопировала данные из кольцевого буфера в обычный массив, но сдвинула
данные исходной отсортированной последовательности. Теперь массив не является
отсортированным. Тем не менее, нужно обеспечить возможность находить в нем элемент за 
O(logn).
Можно предполагать, что в массиве только уникальные элементы.

Формат ввода
Функция принимает массив натуральных чисел и искомое число k.
Длина массива не превосходит 10000. Элементы массива и число k не превосходят
по значению 10000.

Формат вывода
Функция должна вернуть индекс элемента, равного k, если такой есть в массиве
(нумерация с нуля). Если элемент не найден, функция должна вернуть −1.
Изменять массив нельзя.
Для отсечения неэффективных решений ваша функция будет запускаться от 100000 до 
1000000 раз.
"""
from typing import Tuple, List


def broken_search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1


def main() -> Tuple[int, List[int]]:
    input()
    desired_element = int(input())
    nums = [int(number) for number in input().split()]
    return desired_element, nums


if __name__ == '__main__':
    desired_element, nums = main()
    print(broken_search(nums, desired_element))
