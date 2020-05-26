for i in range(7):
    for j in range(4):
        if j==2 or (i+j)==1 or (i==6 and j>0):
            print("#",end="")
        else: 
            print(end=" ")
    print()