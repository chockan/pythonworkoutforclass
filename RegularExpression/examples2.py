import re

def abc(email):
    a=r"^[a-zA-Z0-9._%+-]+@[a-z]{5}\.[a-zA-Z]{2,3}$"
    print(bool(re.match(a,email)))
    return bool(re.match(a,email))

email="abc@gmail.com"
if abc(email):
    print(f"{email} is a valid")
else:
    print(f"{email} is not valid")