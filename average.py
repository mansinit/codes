def average():
    list1=list()
    n=int(input("Enter the length"))
    print("Enter elements of the list")
    for i in range(0,n):
        x=input()
        list1.append(x)
    print(list1)
    t=sum(list1)/n
    print(t)


average()
