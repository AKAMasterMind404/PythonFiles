with open("aRough4.py","r") as file:
    for s in file:
        name = s.strip()
        print(f"\"{name}\": coin.{name},")
