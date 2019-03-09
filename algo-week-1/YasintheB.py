inp=input()
inp2=map(int,raw_input().split())

def cal(b):
    sum=0
    for i in range(1,len(inp2)+1):
        sum+=abs(inp2[i-1]-(b+i))
    return sum
"""
print cal(-2)
print cal(-1)
print cal(0)
print cal(1)
print cal(2)
"""
l=int(-(1e9+5))
r=-l

def ternary(l,r):
    mn=100000000000000 #14 sifir var
    while l<=r:
        mid1=l+(r-l)/3
        mid2=r-(r-l)/3
        # print l,r,mid1,mid2
        x1=cal(mid1)
        x2=cal(mid2)
        mn=min(x1,x2,mn)
        # print mn
        if x1>x2:
            l=mid1+1
        else:
            r=mid2-1
    return mn
print ternary(l,r)
