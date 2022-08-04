import random

string = "".join(str(random.randbytes(28))[2:-1:].split("\\"))

print(string, len(string))