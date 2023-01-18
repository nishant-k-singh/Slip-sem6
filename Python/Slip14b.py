with open("file1.txt",'r') as f:
    data=f.read()
rev_data=data[::-1]
print(rev_data)
with open("file4.txt",'w') as f:
    f.write(rev_data)
