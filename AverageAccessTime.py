def accessTime(h,tc,tm):
    tav= tc + (1-h) * tm
    return tav
def probAccessTime(pr, tavr,tm):
    if pr>1 or pr<0:
        return None
    time = pr*tavr +(1-pr) * tm
    return time
tavr=accessTime(0.9,50,500)

pat=probAccessTime(0.8,tavr,500)
print(pat)