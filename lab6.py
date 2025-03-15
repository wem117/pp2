#Write a Python program with builtin function to multiply all the numbers in a list
""" 
def multip_numbers(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

numbers = [2, 5, 7, 14]
print(multip_numbers(numbers))
 """
#output: 980;

# Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters

# def calculate_let(text):
#     lowercase_count = sum(1 for letter in text if letter.islower())
#     capital_count = sum(1 for letter in text if letter.isupper())
#     return lowercase_count, capital_count

# text = "BeTTer fInd a maP IS get STICKY"
# lowercase, capital = calculate_let(text)
# print(f"capital : {capital}, lower : {lowercase}")

#capital : 13, lower : 11

#Write a Python program with builtin function that checks whether a passed string is palindrome or not.

# def find_palindrome(s):
#     if s.lower()[::-1] == s.lower():
#         return True
#     else:
#         return False

# user_input = input("smth: ")
# if find_palindrome(user_input):
#     print("is palindrome")
# else:
#     print("no")

# output : is palindrome

# Write a Python program that invoke square root function after specific milliseconds.

# true

# input : 64122 and 4323
# outpuut : 253.2232216839522

# def all_elements(tup):
#     return all(tup)

# num_tuples = int(input())

# tuples_list = [ ]

# for i in range(num_tuples):
#     user_input = input(f"Tuple {i+1}:")
#     tup = tuple(value.lower() in ["true", "1"] for value in user_input.split())
#     tuples_list.append(tup)

# for i, tup in enumerate(tuples_list, 1):
#     result = all_elements(tup)
#     print(f"Tuple {i} 1: {result}")

# input: 1 -> Tuple 1:true 1 true 
# output:  True


# Write a Python program to list only directories, files and all directories, files in a specified path.

# import os

# def list_content(path):
#     if not os.path.exists(path):
#         path = path.strip()
#         print(f"Error: The path '{path}' does not exist.")
#         return
        
#     all_items = os.listdir(path)

#     directories = [item for item in all_items if os.path.isdir(os.path.join(path, item))]
#     files = [item for item in all_items if os.path.isfile(os.path.join(path, item))]

#     print("Directories:")
#     print("\n".join(directories) if directories else "No directories found.")
    
#     print("\nFiles:")
#     print("\n".join(files) if files else "No files found.")
    
#     print("\nAll Contents:")
#     print("\n".join(os.listdir(path)) if os.listdir(path) else "Directory is empty.")

# path = input()
# list_content(path)

# input: /Users/miraszhumatayev/Desktop/izum ai  
# outpit: /Users/miraszhumatayev/Desktop/izum ai 
# Directories:
# No directories found.

# Files:
# Снимок экрана 2025-03-12 в 2.48.51 PM.png
# Снимок экрана 2025-03-12 в 11.45.43 PM.png
# Снимок экрана 2025-03-12 в 11.51.32 PM.png
# .DS_Store
# Снимок экрана 2025-03-12 в 11.53.23 PM.png
# Снимок экрана 2025-03-12 в 11.55.37 PM.png
# Снимок экрана 2025-03-12 в 11.53.27 PM.png
# Снимок экрана 2025-03-12 в 11.57.57 PM.png
# Снимок экрана 2025-03-12 в 11.44.53 PM.png
# Снимок экрана 2025-03-12 в 11.52.07 PM.png
# Снимок экрана 2025-03-12 в 11.51.28 PM.png
# Снимок экрана 2025-03-12 в 11.52.02 PM.png
# Снимок экрана 2025-03-12 в 11.57.54 PM.png
# Снимок экрана 2025-03-12 в 11.55.34 PM.png

# All Contents:
# Снимок экрана 2025-03-12 в 2.48.51 PM.png
# Снимок экрана 2025-03-12 в 11.45.43 PM.png
# Снимок экрана 2025-03-12 в 11.51.32 PM.png
# .DS_Store
# Снимок экрана 2025-03-12 в 11.53.23 PM.png
# Снимок экрана 2025-03-12 в 11.55.37 PM.png
# Снимок экрана 2025-03-12 в 11.53.27 PM.png
# Снимок экрана 2025-03-12 в 11.57.57 PM.png
# Снимок экрана 2025-03-12 в 11.44.53 PM.png
# Снимок экрана 2025-03-12 в 11.52.07 PM.png
# Снимок экрана 2025-03-12 в 11.51.28 PM.png
# Снимок экрана 2025-03-12 в 11.52.02 PM.png
# Снимок экрана 2025-03-12 в 11.57.54 PM.png
# Снимок экрана 2025-03-12 в 11.55.34 PM.png

# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

# import os

# def check_access(path):
#     path = path.strip()
    
#     if not os.path.exists(path):
#         print(f"Error: The path '{path}' does not exist.")
#         return
    
#     print(path)
#     print(f"Exists: {'Yes' if os.path.exists(path) else 'No'}")
#     print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
#     print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
#     print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")

# path = input().strip()
# check_access(path)

# Write a Python program to test whether a given path exists or not. If the path exist find the filename and directory portion of the given path.

# import os

# def check_path(path):
#     path = path.strip()
    
#     if not os.path.exists(path):
#         print(f"Error: The path '{path}' does not exist.")
#         return
    
#     print(f"Checking path: {path}")
#     print(f"Exists: {'Yes' if os.path.exists(path) else 'No'}")
#     print(f"Readable: {'Yes' if os.access(path, os.R_OK) else 'No'}")
#     print(f"Writable: {'Yes' if os.access(path, os.W_OK) else 'No'}")
#     print(f"Executable: {'Yes' if os.access(path, os.X_OK) else 'No'}")
    
#     directory = os.path.dirname(path)
#     filename = os.path.basename(path)
#     print(f"Directory portion: {directory if directory else 'N/A'}")
#     print(f"Filename portion: {filename if filename else 'N/A'}")

# path = input("Enter the path: ").strip()
# check_path(path)

# Write a Python program to count the number of lines in a text file.

# import os

# def count_lines(path):
#     if os.path.isfile(path):
#         with open(path, 'r', encoding='utf-8') as file:
#             return sum(1 for _ in file)
#     return None

# path = input().strip()
# if os.path.isfile(path):
#     lines = count_lines(path)
#     print(lines if lines is not None else "Error reading file.")
# else:
#     print("Invalid file path.")

#  Write a Python program to write a list to a file.

# def write_list_to_file():
#     file_path = input().strip()
#     data = input().split(',')
#     with open(file_path, 'w', encoding='utf-8') as file:
#         for item in data:
#             file.write(f"{item.strip()}\n")

# write_list_to_file()

# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt

# import string

# def generate_text_files():
#     for letter in string.ascii_uppercase:
#         with open(f"{letter}.txt", 'w', encoding='utf-8') as file:
#             file.write(f"This is {letter}.txt\n")

# generate_text_files()

# Write a Python program to copy the contents of a file to another file

# def copy_file(source, destination):
#     with open(source, 'r', encoding='utf-8') as src:
#         with open(destination, 'w', encoding='utf-8') as dest:
#             dest.write(src.read())

# source_file = input().strip()
# destination_file = input().strip()
# copy_file(source_file, destination_file)

# Write a Python program to delete file by specified path. Before deleting check for access and whether a given path exists or not.

# import os

# def delete_file(file_path):
#     if os.path.exists(file_path) and os.path.isfile(file_path):
#         try:
#             os.remove(file_path)
#             print("File deleted.")
#         except PermissionError:
#             print("Permission denied.")
#     else:
#         print("Invalid file path.")

# file_path = input().strip()
# delete_file(file_path)
