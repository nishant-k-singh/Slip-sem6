#Write a python program to print the contents of file in reverse order
a=input("")
with open("abc.txt","w") as f:
    f.write("this is my file of python programming")
with open("abc.txt","r") as f:   
    a=f.read()
    print(a)
    print(a[::-1])

'''
filename=input("enter file name")
for line in reversed(list(open(filename))):
    print(line.rstrip())
'''     
                                    1