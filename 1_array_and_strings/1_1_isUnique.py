# Implement an algorithm to determine if a string has all unique chracters. 
# What if you cannot use additional data structures?



def checkUnique(string : str) -> bool:
    len1 = len(list(string))
    len2 = len(set(list(string)))
    return print(len1 == len2)

def noNewStructs(string : str) -> bool:
    pass

if __name__ == "__main__":
    string = "qwertyuiop"
    checkUnique(string)
    noNewStructs(string)
