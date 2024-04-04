x = "global"
def f3():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
f3()
##########################################

def f1():
    y = "local"
    print(y)
f1()

#######################################
x = "global"
def f():
    print("x inside :", x)
f()
print("x outside:", x)