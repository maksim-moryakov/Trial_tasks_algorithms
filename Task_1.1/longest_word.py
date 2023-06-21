"""
Чтобы подготовиться к семинару, Гоше надо прочитать статью по эффективному
менеджменту. Так как Гоша хочет спланировать день заранее, ему необходимо
оценить сложность статьи.

Он придумал такой метод оценки: берётся случайное предложение из текста и
в нём ищется самое длинное слово. Его длина и будет условной сложностью статьи.
"""


def get_longest_word(line: str) -> str:
    word = line.split()
    return max(word, key=len)

def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))

def main():
    print_result(get_longest_word(read_input()))


if __name__ == '__main__':
    main()