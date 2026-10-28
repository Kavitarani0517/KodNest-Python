# Example for creating class and objects
class Student:
    name = "Rahul"
    age = 22
    marks = 75

    def study(self): # Zero parameterized Constructor
        print(f"{self.name} is studing {self.age} years old")
    
    def play(self): # Zero parameterized Constructor
        print(f"{self.name} is playing {self.age} years old")
s = Student()
print(s.name)
print(s.age)
print(s.marks)

s.study() 
s.play()
 
# Example for creating class and objects using constructors
class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def study(self):
        print(f"{self.name} is studing {self.age} years old")
    
    def play(self):
        print(f"{self.name} is playing {self.age} years old")
s1 = Student("Rahul", 23, 78.5) # Parameterized Constructors
print(f"Name:{s1.name}\nAge:{s1.age}\nMarks:{s1.marks}")
s2 = Student("Shakthi", 24, 85.5) # Parameterized Constructors
print(f"Name:{s2.name}\nAge:{s2.age}\nMarks:{s2.marks}")

s1.study() 
s1.play()

s2.study()
s2.play()
 
