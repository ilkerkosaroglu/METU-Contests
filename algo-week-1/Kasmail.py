n,req=map(int,raw_input().split())
inp2=map(int,raw_input().split())


def count(h):
    sum=0
    for i in inp2:
        if i>h:sum+=i-h
    return sum
h=0
logs=0
maxh=int(1e+9+5)
flag=""
while h<=maxh:
    mid=(h+maxh)/2
    logs=count(mid)
    if logs>req:
        h=mid+1
    if logs<req:
        maxh=mid-1
    if logs==req:
        print mid
        flag="found"
        break
if not flag:
    print maxh
