def underScores(n: int, s: str) -> str:
    return str(n) + '_' + '_'.join(s.split())


if __name__ == '__main__':
    s = 'find Largest sum contiguous Subarray [V. IMP]'
    print(underScores(7, s))
