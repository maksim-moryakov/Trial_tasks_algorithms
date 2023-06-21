"""
Помогите Васе понять, будет ли фраза палиндромом. 
Учитываются только буквы и цифры, заглавные и строчные буквы считаются
одинаковыми.

Решение должно работать за O(N), где N — длина строки на входе.
"""
import re

def is_palindrome(line: str) -> bool:
    word = re.sub(r'\W', '', line.lower())
    return word == word[::-1]

print(is_palindrome(input().strip()))