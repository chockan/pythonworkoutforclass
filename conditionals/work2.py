for i in range(6):
    for j in range(4):
        if (i==0 or i==2 or j==0 or (j==3 and i>3)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print() 