low=int()
upp=int()
str=input("Enter a string :")
for i in str:
    if i.islower():
        low+=1
    else:
        upp+=1

print(f"Number of lower case characters are{low}")
print(f"Number of upper case characters are{upp}")