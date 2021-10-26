input_binary = int(input("Binary input:"), 2)
key = int(input("Key:"), 2)
if len(str(input_binary)) != len(str(key)):
    print("Length of key doesn't match the length of input")
else:
    cipher = input_binary ^ key
    print("The Encrypted Binary message:", bin(cipher))
    decrypted_text = cipher ^ key
    print("The Decrypted Text in Binary:",
          bin(decrypted_text))

# Sample input: 110011101
# Sample key: 111100001