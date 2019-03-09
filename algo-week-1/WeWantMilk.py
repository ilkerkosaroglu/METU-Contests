inp,M=map(int,raw_input().split())

bucketList=[]
for i in xrange(inp):
    cow=map(int,raw_input().split())
    bucketList.append(cow)
bucketList.sort()
sum=0
for i in bucketList:
    if i[1]<M:
        sum+=i[0]*i[1]
        M-=i[1]
        if M==0:break
    else:
        sum+=i[0]*M
        break
print sum

