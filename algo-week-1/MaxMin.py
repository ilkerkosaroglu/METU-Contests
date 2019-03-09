n=input()
k=input()
L=[]
for i in range(n):
    L.append(input())
L.sort()
best=100000000000
print L
"""
for i in range(0,n-k):
    mx=-5
    mn=10000000000
    for j in range(k):
        if mn>L[j+i]:mn=L[j+i]
        if mx<L[j+i]:mx=L[j+i]
    if best>mx-mn:best=mx-mn
"""
for i in range(0,n-k+1):
    mn=L[i]
    mx=L[i+k-1]
    print mn,mx
    if best>mx-mn:best=mx-mn
print best
