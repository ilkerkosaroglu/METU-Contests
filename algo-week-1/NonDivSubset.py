n,k=map(int,raw_input().split())
inp2=map(int,raw_input().split())
"""
for k=5
1 2 3 4 5 6 7 8 9
m={0:1, 1:2, 2:2, 3:2, 4:2}
#1 tane 0
max(1 or 4)
max(2 or 3)
#
for k=4
1 2 3 4 5 6 7 8 9 10
m={0:2, 1:3, 2:3, 3:2}
#1 tane 0
max(1 or 3)
#1 tane 2
"""
m={}
for i in range(k):
    m[i]=0
for i in inp2:
    x=i%k
    m[x]+=1
sum=0
if k%2:
    if m[0]:sum+=1
    for i in range((k-1)/2):
        sum+=max(m[i+1],m[k-i-1])
else:
    if m[0]:sum+=1
    if m[k/2]:sum+=1
    for i in range((k-2)/2):
        sum+=max(m[i+1],m[k-i-1])
print sum
