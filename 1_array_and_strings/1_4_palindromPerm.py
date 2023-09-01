# Given a stringm write a function to check if it is a permutation of a palindrome
from itertools import permutations

def checkPalPerm(string1 : str) -> bool:
    _str1 = string1.lower().replace(" ", "")
    perms = permutations(_str1)
    for perm in list(perms):
        if perm == perm[::-1]:
            return True
    return False
    
if __name__ == "__main__":
    string = "Tact coa"
    print(checkPalPerm(string))