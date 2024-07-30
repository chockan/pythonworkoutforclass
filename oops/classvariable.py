class abc:
    name="sachin"
    year_of_birth=1985

    def met(self,current_year):
        return f"Name {self.name} Age is {current_year - self.year_of_birth}"
    
a1=abc()
print(a1.met(2024))
a2=abc()
a2.name="dhoni"
a2.year_of_birth=1987
print(a2.met(2024))
