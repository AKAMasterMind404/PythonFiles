import os

path = os.path.abspath('')

tab = "    "

with open(path + '\\sample_input.txt') as file:
    dtoname = "SentEmailInput"

    print(f"export interface I{dtoname}DTO ", "{")
    print(f"subject: string;")
    for i in file:
        line = i.strip()
        key, val = line.split(":")
        key, val = str(key).replace('"', ""), str(val).replace('"', "")
        key, val = str(key).replace("'", "'"), str(val).replace("'", "'")
        print(f"{tab}{key} : string;")
    print("}")

with open(path + '\\sample_input.txt') as file:
    print(f"private getI{dtoname}(reqBody) : I{dtoname}DTO", "{\n" + "return {")
    print(f"subject: {dtoname}Template.SUBJECT,")
    for i in file:
        line = i.strip()
        key, val = line.split(":")
        key, val = str(key).replace('"', ""), str(val).replace('"', "")
        key, val = str(key).replace("'", "'"), str(val).replace("'", "'")

        print(f"{tab}{key} : reqBody.{key},")
    print("}};")
