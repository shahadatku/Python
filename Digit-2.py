for i in range(7):
    for j in range(5):
        if i==6 or (i+j)==6 or (i==0 and (j>0 and j<4)) or (i==1 and (j<1 or j>3)):
            print("#",end="")
        else: 
            print(end=" ")
    print()