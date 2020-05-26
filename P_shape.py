for row in range(7):
    for col in range(7):
        if col==0 or ((row==0 or row==3) and col!=6) or (col==6 and (row==1 or row==2)):
            print("*",end="")
        else:
            print(end=" ")
    print()