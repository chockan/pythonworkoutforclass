# for i in range(5):
#     for j in range(5):
#         if ((j==0 or j==4) or (i==0 or i==2)):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")

#     print()



for i in range(5):
    for j in range(4):
        if ((i==0 or i==2) or (j==0 or (j==3 and i<3))):
            print("*",end=" ")
        else:
            print(" ",end=" ")

    print()