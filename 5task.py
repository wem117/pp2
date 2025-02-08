from itertools import permutations

def print_permutation(s):
    for perm in permutations(s):
        print("".join(perm))

inputuser = input()
print_permutation(inputuser) 