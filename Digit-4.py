for i in range(8):
    for j in range(6):
        if i==4 or j==4 or i+j==4:
            print("#",end="")
        else: 
            print(end=" ")
    print()