q=[]
def enque():
    for i in range(n):
        if len(q)==n:
            print("List is full")
        else:
            ele=int(input("Enter element in queue :"))
            q.append(ele)
            print("Element is added to queue")

def deque():
    if not q:
        print("Queue is empty")
    else:
        q.pop(0)
        print("Element removed")

def display():
    print(q)    
n=int(input("Enter size of queue :"))    
while True:
    print("Select the operation:\n1.Add\n2.Delete\n3.Display\n4.Quit")
    choice=int(input())
    if choice==1:
        enque()
    elif choice==2:
        deque()
    elif choice==3:
        display()
    elif choice==4:
        break
    else:
        print("Invalid option")