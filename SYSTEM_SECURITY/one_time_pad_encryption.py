def getNum(character: str) -> int:
    return ord(character.lower()) - 97


if __name__ == '__main__':
    message = "HELLO"
    [print(getNum(i), end=" ") for i in message]

    key = "XMCKL"

    print()

    cipherText = ""

    for i in range(len(message)):
        cipherNum = getNum(message[i]) + getNum(key[i])
        cipherNum = cipherNum % 26
        cipherText += chr(cipherNum + 97)

        print(cipherNum, end=" ")
    print()

    print(f"Cipher text: {cipherText}")
