for i in range(7):
    for j in range(6):
        if i==0 or ((i==3 or i==6) and (j>0 and j<5)) or (j==0 and i<4) or (i-j)==5 or (i==5 and (j<1 and j>4)) or ((i>3 and i<6) and j==5):
            print("#",end="")
        else:
            print(end=" ")
    print()