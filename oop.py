class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Name:", self.name)
        print("Age:", self.age)

student1 = Student("John", 20)
print(student1.name)  # Output: John
print(student1.age)   # Output: 20 