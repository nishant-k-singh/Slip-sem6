    n=int(input("Enter a number :"))
    if n>1:
        for i in range(2, n+1):
            if n%i==0:
                print("It is not a prime number")
                break
            else:
                print("It is a prime number")
                break
    elif n==1:
        print("1 is neither prime not composite")
    else:
        print("Enter non-zero positive numbers")    
    
    
    def fact(n):
        factorial=1
        for i in range(1, n+1):
            factorial=factorial*i
        print(f"Factorial of {n} is", factorial)
        
    fact(n)