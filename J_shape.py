for row in range(7):
    for col in range(5):
        if col==3 or (row==0 and (col==2 or col==4)) or (row==6 and (col==1 or col==2)) or (row==5 and col==0):
            print("*",end="")
        else:
            print(end=" ")
    print()