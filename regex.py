# 1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

# import re

# with open('row.txt', 'r') as file:
#     text = file.read()

# def find_line(text, max_match = 5):
#     line = r'^.*a[b]+.*$'     #r'ab*'
#     matches = re.findall(line, text, re.MULTILINE)
#     print("Matches found:", matches)
#     for match in matches[:max_match]:
#         print(match)

# find_line(text)

""" Matches found: ['aaabbethrdbbb hrthrhbgbabbb']
aaabbethrdbbb hrthrhbgbabbb 
"""

# import re

# with open('row.txt', 'r') as file:
#     text = file.read()

# def find_str(text, max_match = 5):
#     line = r'^.*ab{2,3}.*$'
#     matches = re.findall(line, text, re.MULTILINE)
#     print("Matches found:", matches)
#     for match in matches[:max_match]:
#         print(match)

# find_str (text)

# Write a Python program to find sequences of lowercase letters joined with a underscore.

# import re

# def find_sequences(text):
#     pattern = r'\b[a-z]+_[a-z]+\b'
#     return re.findall(pattern, text)

# choice = input().strip().lower()
# if choice == "file":
#     with open('row.txt', 'r') as file:
#         text = file.read()
# else:
#     text = choice

# print(find_sequences(text))

# Write a Python program to find the sequences of one upper case letter followed by lower case letters.

# import re

# def find_sequences(text):
#     pattern = r'\b[A-Z][a-z]+\b'
#     return re.findall(pattern, text)

# with open('row.txt', 'r') as file:
#     text = file.read()

# print(find_sequences(text))

# Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

# import re

# def match_pattern(text):
#     pattern = r'a.*b$'
#     return bool(re.fullmatch(pattern, text))

# with open('row.txt', 'r') as file:
#     text = file.read()

# print(match_pattern(text))

# Write a Python program to replace all occurrences of space, comma, or dot with a colon.

# import re

# def replace_chars(text):
#     return re.sub(r'[ ,.]', ':', text)

# with open('row.txt', 'r') as file:
#     text = file.read()

# print(replace_chars(text))

# Write a python program to convert snake case string to camel case string.

# import re

# def snake_to_camel(text):
#     words = text.split('_')
#     return words[0] + ''.join(word.capitalize() for word in words[1:])

# with open('row.txt', 'r') as file:
#     text = file.read().strip()

# print(snake_to_camel(text))

# Write a Python program to split a string at uppercase letters.

import re

def split_at_uppercase(text):
    return re.findall(r'[A-Z][a-z]*', text)

with open('row.txt', 'r') as file:
    text = file.read().strip()

print(split_at_uppercase(text))

# Write a Python program to insert spaces between words starting with capital letters.

import re

def insert_spaces(text):
    return ' '.join(re.findall(r'[A-Z][a-z]*', text))

with open('row.txt', 'r') as file:
    text = file.read().strip()

print(insert_spaces(text))

# Write a Python program to convert a given camel case string to snake case.

import re

def camel_to_snake(text):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', text).lower()

with open('row.txt', 'r') as file:
    text = file.read().strip()

print(camel_to_snake(text))
