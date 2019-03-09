n,x,a=map(int,raw_input().split())

def cal(x,a,b):
    days=0
    cur=0
    while not cur>=x:
        days+=1
        cur+=a
        if cur>=x:return days
        cur-=b
        if cur<0:cur=0
    return days


minsleep=0
ns=minsleep

maxsleep=a-1
ms=maxsleep

while ns<=ms:
    mid=(ns+ms)/2
    res=cal(x,a,mid)
    if res>n:
        ms=mid-1
    if res<=n:
        ns=mid+1
print ms
