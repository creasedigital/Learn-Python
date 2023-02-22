class User:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        
    def __repr__(self):
        return f"Nomenclature is {self.first} {self.last}"

    def fullname(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, like):
        return f"{self.first} likes {like}"

        
    
        

user1 = User("Punk", "Manewe", 31)
print(user1)
print(user1.fullname())
print(user1.likes("eating"))



