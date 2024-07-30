import re
def abc(phone_number):
    a="[789]\d{9}$"
    if re.match(a,phone_number):
        return True
    else:
        False

numbers=["9895965425","1254568585","9596655858"]
for i in numbers:
    if abc(i):
        print(f"{i} is a valid number")
    else:
        print(f"{i} is not valid number")