import random

a=random.random()
print(a)

b=random.uniform(1,5)

print(b)

c=random.randint(2,6)
print(c)
d=random.randrange(2,6)
print(d)



x=[2,4,6,8,10]
e=random.choice(x)
print(e)


y=[2,4,6,8,10]
f=random.sample(y,4)
print(f)

z=[3,6,9,10]
random.shuffle(z)
print(z)