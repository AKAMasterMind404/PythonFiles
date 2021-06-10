class HashMap:
    def __init__(self, default=None):
        self.d = dict()
        self.default = default

    def add(self, key, value):  # SETTER FUNCTION
        self.d[key] = value

    def remove(self, key):
        try:
            self.d.pop(key)
        except KeyError:
            pass

    def __call__(self, ele):  # GETTER FUNCTION
        try:
            return self.d[ele]
        except KeyError:
            return self.default

    def __str__(self):
        return str(self.d)


if __name__ == '__main__':
    h1 = HashMap()
    h1.add(1, 1)
    h1.add(2, 2)
    h1.add(3, 3)
    print(h1(2))
