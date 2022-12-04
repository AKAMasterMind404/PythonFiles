import os

BOOLEAN = "bool"
INTEGER = "int"
FLOAT = "double"
DOUBLE = "double"
STRING = "str"
LIST = "list"
DICT = "dict"
DATETIME = "datetime"


class ModelGenerator:
    def __init__(self, name: str, params: list[tuple]):
        self.name = name
        self.params = params

    def generateFieldsCode(self):
        file = open(os.path.join(os.path.dirname(__file__), f'{self.name}Fields.dart'), 'w')
        file.write(f'''class {self.name}Fields ''' + '{\n')

        self._writeParamList(file)
        self._initializeNamedFields(file)

        file.write('''}\n''')

    def generateObjectCode(self):
        file = open(os.path.join(os.path.dirname(__file__), f'{self.name}.dart'), 'w')
        file.write(f'''class {self.name} ''' + '{\n')

        self._writeAttributes(file)
        self._writeConstructor(file)
        self._writeCopyFunction(file)
        self._writefromJSON(file)
        self._writeToJSON(file)

        file.write('''}\n''')

    def _writefromJSON(self, file):
        file.write(f'''  static {self.name} fromJson(Map<String, Object?> json) => {self.name}(\n''')
        for i, j in self.params:
            type = self._getDataType(j)
            file.write(f'''        {i}: json[{self.name}Fields.local_id] as {type},\n''')
        file.write('''      );\n\n''')

    def _writeToJSON(self, file):
        file.write('''  Map<String, Object?> toJson() => {\n''')
        for i, j in self.params:
            field = i
            if j == DATETIME:
                field = i + ".toIso8601String()"
            file.write(f'''        {self.name}Fields.{i}: {field},\n''')
        file.write('''      };\n''')

    def _writeCopyFunction(self, file):
        file.write(f'''  {self.name} copy(''' + '{\n')
        for i, j in self.params:
            type = self._getDataType(j)
            file.write(f'''          {type}? {i}, \n''')
        file.write("          }) => \n" + f'''      {self.name}(\n''')
        for i, j in self.params:
            file.write(f'''        {i}: {i} ?? this.{i}, \n''')
        file.write("      ); \n\n")

    def _writeAttributes(self, file):
        for i, j in self.params:
            type = self._getDataType(j)
            file.write(f'''  final {type} {i}; \n''')
        file.write("\n")

    def _writeConstructor(self, file):
        file.write(f'''  const {self.name}(''' + '{\n')
        for i, j in self.params:
            file.write(f'''      required this.{i}, \n''')
        file.write("  });\n\n")

    def _getDataType(self, data_type: str):
        _map = {
            BOOLEAN: "bool",
            FLOAT: "double",
            DOUBLE: "double",
            INTEGER: "int",
            STRING: "String",
            LIST: "List",
            DATETIME: "DateTime",
            DICT: "Map<dynamic,dynamic>",
        }

        return _map[data_type]

    def _writeParamList(self, file):
        file.write('''  static final List<String> attributes = [\n''')

        c = 0
        for i, j in self.params:
            file.write(f'       {i}, ')
            if c % 3 == 0:
                file.write('\n')
            c += 1
        file.write('''  ];\n''')

    def _initializeNamedFields(self, file):
        for i, j in self.params:
            file.write(f"   static const String {i} = '{i}';\n")


o1: ModelGenerator = ModelGenerator(
    "Note",
    [
        ("name", STRING),
        ("age", INTEGER),
        ("isAdult", BOOLEAN),
        ("score", FLOAT),
        ("listIds", LIST),
        ("some1", DATETIME),
        ("some2", DATETIME),
    ],
)

o1.generateFieldsCode()
o1.generateObjectCode()
