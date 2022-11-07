# A IS 1 IE. INDEXING FROM 1

def getChar(num: int):
    return chr(96 + num)


def getNum(char: str):
    return abs(96 - ord(char.lower()))

