with open("ab.txt","r") as file:
    attr = []
    name = input("Name of blueprint:")
    brkt1 = "{"
    brkt2 = "}"
    print(f"class {name}{brkt1}")
    print("// INITIALIZE ATTRIBUTES")
    for s in file:
        item = s.strip()
        attribute = item.split(":")[0][1:-1:]
        attr.append(attribute)
        val = item.split()[1]
        type = "String"
        if val == "null":
            type = "dynamic"
        if val.count("\"")==2:
            type = "String"
        elif val.count("[")==1 and val.count("]")==1:
            type = "List"
        elif val.count("{")==1 and val.count("}")==1:
            type = "Map"
        elif val.count("\"")==0:
            type = "int"
        elif val.count(".")==1:
            type = "double"

        print(f"{type} {attribute};")

    ####
    print()
    print(f"{name}({brkt1}")
    for a in attr:
        print(f"this.{a},")
    print(f"{brkt2});")
    print()

    ####
    print()
    print(f"factory {name}.fromJSON(Map value){brkt1}")
    print(f"return {name}(")
    for a in attr:
        print(f"{a} : value[\"{a}\"],")
    print(");")
    print(f"{brkt2}")
    ####

    print(f"{brkt2}")
