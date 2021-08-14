with open("aRough4.py","r") as file:
    for s in file:
        unit = s.strip().split(":")[0]
        print(f"tripSummaryResult.{unit[1:-1:]} = data[\"{unit[1:-1:]}\"];")
        # print(f"\"{unit[1:-2:]}\"")

'''
"firstName"
"lastName"
"email"
"phoneCountryCode"
"phoneNumber"
'''