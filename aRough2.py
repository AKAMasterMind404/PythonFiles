with open("aRough4.py","r") as file:
    states = file.readline().split(',')
    for s in states:
        print("\""+s.strip()+"\"", end=",")