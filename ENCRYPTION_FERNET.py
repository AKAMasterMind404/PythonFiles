from cryptography.fernet import Fernet
key = Fernet.generate_key() #this is your "password"
cipher_suite = Fernet(key)
encoded_text = cipher_suite.encrypt(b"Hey my name is")
decoded_text = cipher_suite.decrypt(encoded_text)

print(decoded_text)