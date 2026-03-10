# ============================================================
# Python Strings - Foundations
# ============================================================

s = "Hello, World!"

# Access
print(s[0])             # 'H'
print(s[-1])            # '!'
print(s[0:5])           # 'Hello'
print(s[::-1])          # reversed string

# Common methods
print(s.lower())
print(s.upper())
print(s.strip())                    # strip whitespace
print(s.split(', '))                # ['Hello', 'World!']
print(', '.join(['a', 'b', 'c']))   # 'a, b, c'
print(s.replace('World', 'Python'))
print(s.startswith('Hello'))
print(s.endswith('!'))
print(s.count('l'))     # 3
print(s.find('o'))      # 4 (index), -1 if not found
print(len(s))

# Char checks
print('a'.isalpha())
print('3'.isdigit())
print('a3'.isalnum())

# ASCII
print(ord('a'))         # 97
print(chr(97))          # 'a'

# Build strings - use join, not +=
chars = ['a', 'b', 'c']
result = ''.join(chars)         # efficient

# Iterate over chars
for ch in s:
    pass

# Iterate with index
for i, ch in enumerate(s):
    pass

# f-strings
name = "Alice"
print(f"Hello, {name}!")
print(f"{3.14159:.2f}")         # '3.14'

# Check if string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# Count char frequencies
from collections import Counter
freq = Counter("aababc")
print(freq)  # Counter({'a': 3, 'b': 2, 'c': 1})
