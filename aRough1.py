for i, j in [
    # ('a', 'a'),
    ('a', 'b'),
    ('a', 'c'),
    ('a', 'z'),
    ('a', 'y'),
]:
    c1val = ord(i) - 96
    c2val = ord(j) - 96

    print(26%abs(c1val - c2val))
