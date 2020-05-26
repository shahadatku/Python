string=input("Enter a string: ")
a=len(string)
for i in range(0,a):
    for j in range(0,i+1):
        print(string[i],end=" ")
    print()