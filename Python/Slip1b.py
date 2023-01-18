
str=input("Enter a string :")

def odd_index(str):
    result=""
    for i in range(len(str)):
        if(i%2==0):
            result=result+str[i]    
    return result


print(odd_index(str))