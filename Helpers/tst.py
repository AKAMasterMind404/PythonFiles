o1: GenerateScripts = GenerateScripts(
    "Note",
    [
        ("name", STRING),
        ("age", INTEGER),
        ("isAdult", BOOLEAN),
        ("score", FLOAT),
        ("listIds", LIST),
        ("some1", DICT),
    ],
)

o1.runAllScripts()
