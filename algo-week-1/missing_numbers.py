inp=input()
inp2=map(int,raw_input().split())
inp3=input()
inp4=map(int,raw_input().split())

L=[]

D={}
for i in inp4:
    if i not in D:D[i]=0
    D[i]+=1
F={}
for i in inp2:
    if i not in F:F[i]=0
    F[i]+=1

for i in D:
    if i not in F:F[i]=0
    if F[i]<D[i]:
        L.append(i)

L.sort()
for i in L:
    print i,
