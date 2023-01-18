str="thequickbrownfoxjumpsoverthelazydog"
mydict={}
for i in str:
    if str.count(i)>1:
        counter=str.count(i)
        mydict[i]=counter

print(mydict)