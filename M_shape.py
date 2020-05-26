for row in range(7):
    for col in range(7):
        if col==0 or col==6 or ((row==col and (col>0 and col<4 ))) or (row+col==6 and (col==4 or col==5)):
            print("*",end="")
        else:
            print(end=" ")
    print()