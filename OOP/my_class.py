class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def whoami(self):
        return f"I am {self.name}. {self.age} years old."

student1 = Student('Faraji', 22)
print(student1.whoami())

student2 = Student("Mike", 47)
print(student2.whoami())