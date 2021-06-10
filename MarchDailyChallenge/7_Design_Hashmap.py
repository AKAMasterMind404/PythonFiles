class MyHashMap:
    def __init__(self, default=None):
        self.d = dict()
        self.default = default

    def put(self, key, value):  # SETTER FUNCTION
        self.d[key] = value

    def remove(self, key):
        try:
            self.d.pop(key)
        except KeyError:
            pass

    def get(self, key: int):
        try:
            return self.d[key]
        except KeyError:
            return -1

    def __call__(self, ele):  # GETTER FUNCTION
        try:
            return self.d[ele]
        except KeyError:
            return self.default

    def __str__(self):
        return str(self.d)


if __name__ == '__main__':
    h1 = MyHashMap()
    ip = ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
    operands = [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
    ans = []
    for ind, i in enumerate(ip):
        if i == 'put':
            op = operands[ind]
            a = h1.put(op[0], op[1])
            ans.append(a)
        elif i == 'get':
            op = operands[ind]
            a = h1.get(op[0])
            ans.append(a)
        elif i == 'remove':
            a = h1.remove(operands[ind][0])
            ans.append(a)
        else:
            ans.append(None)
    print(ans)
