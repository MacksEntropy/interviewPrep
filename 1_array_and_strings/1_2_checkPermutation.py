# Given two strings, write a method to decide if one is a permutation the other
from itertools import permutations

def checkPerm(string1 : str, string2 : str) -> bool:
    _str1 = string1.lower()
    _str2 = string2.lower()
    perms = permutations(_str1)
    if tuple(_str2) in list(perms):
        return True
    return False
if __name__ == "__main__":
    str1 = "ayeLmao"
    str2 = "lmaooaye"
    print(checkPerm(str1,str2))
