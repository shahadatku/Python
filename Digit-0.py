for i in range(7):
    for j in range(6):
        if ((i==0 or i==6) and (j>0 and j<5)) or ((j==0 or j==5) and (i>0 and i<6)):
            print("#",end="")
        else:
            print(end=" ")
    print()