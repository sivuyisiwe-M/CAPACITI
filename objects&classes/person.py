# class

class Person:
    def __init__(self,name,lastname):
        self.name = name
        self.lastname = lastname
        self.fullname = f"{name} {lastname}"
       
# object
p= Person("siwe","cele")
print(f"name  = {p.name}")
        