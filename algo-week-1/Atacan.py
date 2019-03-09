n,m=map(int,raw_input().split())
ni=map(int,raw_input().split())
mi=map(int,raw_input().split())
"""
import time
ni.sort()
mi.sort()
def b(arr,val):
    l=0
    r=len(arr)-1
    while l<=r:
        # time.sleep(0.1)
        mid=(l+r)/2
        # print mid,arr[mid]
        # print "lr:",l,r
        if arr[mid]<val:
            l=mid+1;
        elif arr[mid]>val:
            r=mid-1;
        else:
            return mid
    return -1
"""
d={}
dpos={}
for x,i in enumerate(ni):
    if i not in d:d[i]=0
    dpos[i]=x+1
    d[i]+=1
for i in mi:
    if i in d:
        if d[i]==1:print dpos[i]
        else:print -1
    else:print -1
