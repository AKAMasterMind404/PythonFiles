numOf = int(input())
for i in range(numOf):
    ip=input()
    if ' ' in ip:
        print("Invalid")
        continue
    if '-' in ip and '---------------' not in ip:
        ip=ip.split('-')
        x=[len(j) for j in ip]
        if x.count(4)==4:
            ip=''.join(ip)
        else:
            print("Invalid")
            continue
    # print('IP[0] IS:',ip[0] in ['4','5','6'])
    # print(ip)
    if ip[0] in ['4','5','6'] and len(ip)==16 and ip.isdigit():
        res = "Valid"
        for i in range(len(ip)):
            if i+4<=len(ip):
                s=ip[i:i+4]
                if s.count(s[0])==4:
                    # print("NO")
                    res="Invalid"
                    break
        print(res)
    else:
        print('Invalid')