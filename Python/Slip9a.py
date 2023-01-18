tup=(1,2,2,3,4,4)
l=list(tup)
for i in l:
    if l.count(i) > 1:
        l.remove(i)

tup=tuple(l)
print(tup)