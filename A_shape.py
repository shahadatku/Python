for row in range(6):
    for col in range(5):
        if ((col==0 or col==4) and row>1) or row==3 or (row+col==2 and row<3) or (col-row==2 and row<3):
            print("*",end="")
        else:
            print(end=" ")
    print()