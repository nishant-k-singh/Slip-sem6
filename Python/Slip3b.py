str=input("Enter key to be searched: ")
d={
    "fruit": "banana",
    "vegetables": "potato",
    "cars": "supra",
    "Bike": "Ninja"
    }

if str in d:
    d[str]="Guava"
    d.pop(str)
    print(d)
else:
    print("The key does not exist")