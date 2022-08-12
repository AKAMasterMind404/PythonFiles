import os

path = os.path.abspath('')

tab = "    "

with open(path + '\\sample_input.txt') as file:
    for i in file:
        line = i.strip()

        try:
            key, value = line.split(":")[0], "".join(line.split(":")[1::])
            key, value = str(key).replace("'", ""), str(value).replace("'", "")
            key, value = str(key).replace('"', '"'), str(value).replace('"', '"')
            value = value.replace(",","")
            key, value = key.strip(), value.strip()
            if value.strip() == "[":
                print(f'"{key}":{value}')
            else:
                print(f'"{key}":"{value}",')
        except ValueError:
            print(i)
