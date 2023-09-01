# There are three types of edits that can be preformed on strings: Instert a character, remove a character, and replace a character. 
# Given two strings, write a function to check if these two strings are one edit away from each other 

def oneAway(str1 : str, str2 : str) -> bool:

    l1 = list(str1)
    l2 = list(str2)

    # Check if replace character
    if len(str1) == len(str2):
        d1 = 0
        for i in range(len(str1)): 
            if l1[i] != l2[i]:
                d1 += 1
                if d1 > 1:
                    return False
        return True

    # Check if add / remove chracter
    if len(str1) == (len(str2)+1) or len(str1) == (len(str2)-1):
        d2 = [x for x in l1 if x not in l2]
        if len(d2) > 1:
            return False
        return True
    return False




if __name__ == "__main__":
    string1 = "g"
    string2 = "ate"
    print(oneAway(string1,string2))