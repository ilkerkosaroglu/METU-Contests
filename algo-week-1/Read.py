let=raw_input()
name=raw_input()
count=0
for i in xrange(len(let)-len(name)+1):
    flag=1
    for k in xrange(len(name)):
        if let[i+k]!=name[k]:flag=0
    if flag:count+=1
print count
