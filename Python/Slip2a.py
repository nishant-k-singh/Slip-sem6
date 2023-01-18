def armstrong(num):
    no=0
    n=num
    while n!=0:
        rem=n%10
        no+=rem**3
        n//=10
    return f"{num} is an armstrong number" if no == num else f"{num} is not an armstrong number"
print(armstrong(153))
       