l=0
u=0
d=0
with open("file1.txt","r") as f:
    str=f.read()
for i in str:
        if i.islower():
            l+=1
        elif i.isupper():
            u+=1
        elif i.isdigit():
            d+=1
print("lower cases :",l)
print("upper cases :",u)
print("digits :",d)