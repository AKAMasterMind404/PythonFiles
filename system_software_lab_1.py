class SymbolTable:
    symbols = dict()

    @staticmethod
    def add_symbol(name, value):
        for key in SymbolTable.symbols:
            if key == name:
                SymbolTable.symbols[key] = value
                return
        SymbolTable.symbols[name] = value

    @staticmethod
    def find_symbol(name):
        for key in SymbolTable.symbols:
            if key == name:
                return SymbolTable.symbols[key]
        raise Exception("Symbol not Defined")


SymbolTable.add_symbol("s1", 1)
SymbolTable.add_symbol("s2", 2)
SymbolTable.add_symbol("s3", 3)
SymbolTable.add_symbol("s4", 4)
SymbolTable.add_symbol("name1", "Atharv")
print(SymbolTable.symbols)
