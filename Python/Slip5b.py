
with open("file1.txt",'w') as f:
    f.write("This is content of File 1")
with open("file2.txt",'w') as f:
    f.write("This is content of File 2")
    
def mergefile(file1,file2):
    with open(file1) as f:
        data1=f.read()
    with open(file2) as f:
        data2=f.read()
    with open("file3.txt",'w') as f:
        f.write(data1)
        f.write("\n")
        f.write(data2)
    print('Files merged successfully')

mergefile("file1.txt", "file2.txt")
