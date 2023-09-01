# Write a method to replace all the spaces in a string with '%20'. You may assume that the string has sufficient space at the end to 
# hold the additional characters, and that you are given the "true" length of the string

def URLify(string : str) -> str:
    _str = string.replace(" ", "%20")
    return _str

if __name__ == "__main__":
    string = "A test String lmao    "
    print(URLify(string))