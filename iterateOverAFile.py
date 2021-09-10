with open("aRough4.py","r") as file:
    for s in file:
        unit = s.strip().split(":")[0][1:-1:]
        vn = "_".join(unit.split()).upper()
        print(f"\"{unit}\":\"{unit}\",")
        # print(f"String {vn} = \"{unit}\";")
