def derangedIP(ip):
    z = 0
    while z < len(ip):
        char = ip[z]
        if char == '.':
            ip.insert(z, '[')
            ip.insert(z + 2, ']')
            z += 2
        z += 1
    ''.join(ip)

if __name__=='__main__':
    ip = list(input())
    # print(derangedIP(ip))
    derangedIP(ip)
    print(''.join(ip))