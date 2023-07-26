"""
ID 89256759

Формат ввода
В первой строке задано число участников n, 1 ≤ n ≤ 100 000.
В каждой из следующих n строк задана информация про одного из участников.
i-й участник описывается тремя параметрами:
- уникальным логином (строкой из маленьких латинских букв длиной не более 20)
- числом решённых задач Pi
- штрафом Fi
Fi и Pi — целые числа, лежащие в диапазоне от 0 до 109.

Формат вывода
Для отсортированного списка участников выведите по порядку их логины по одному в строке.

"""

class Competitor:
    """Класс для отображения участника."""
    def __init__(self, login: str, solved: str, penalty: str):
        self.login = login
        self.solved = int(solved)
        self.penalty = int(penalty)
    
 
    def __lt__(self, other):
        return ((-self.solved, self.penalty, self.login) <
                (-other.solved, other.penalty, other.login))

    def __str__(self):
        return self.login


def quick_sort(arr: list) -> None:
    def partition(arr: list, low: int, high: int) -> int:
        turn = arr[high]
        i_index = low - 1
        for index in range(low, high):
            if arr[index] < turn:
                i_index += 1
                arr[i_index], arr[index] = arr[index], arr[i_index]
        arr[i_index+1], arr[high] = arr[high], arr[i_index+1]
        return i_index+1

    def quick_sort_helper(arr: list, low: int, high: int) -> None:
        if low < high:
            pi = partition(arr, low, high)
            quick_sort_helper(arr, low, pi-1)
            quick_sort_helper(arr, pi+1, high)
    quick_sort_helper(arr, 0, len(arr)-1)


def main() -> None:
    num_users = int(input())
    users = [Competitor(*input().split()) for _ in range(num_users)]
    quick_sort(users)
    print(*users, sep='\n')


if __name__ == '__main__':
    main()
