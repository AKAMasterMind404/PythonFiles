with open('trial.txt', 'r') as file:
    with open('customData.py', 'a+') as f:
        f.write('{')
        dictionary = {}
        for index, iterable_ in file:
            i = iterable_
            print(i)
            splitter = '='
            if index in [0, 1]:
                splitter = ':'
            i = i.split(splitter)
            key_ = i[0].strip()
            val_ = i[1].strip()
            print(key_, ':', val_)

            f.write(f"'{key_}':")
            f.write(f"'{val_}',")

            dictionary[key_] = val_
        print(dictionary)
        f.write('}\n\n')
