class Person:
    def __init__(self, name):
        self.name = name
    
    def say_hello(self):
        print("Hello, " + self.name)

class Student(Person):
    def __init__(self, name, school):
        super().__init__(name)
        self.school = school
    
    def sing_school_song(self):
        print("Ode to " + self.school)

    def say_hello(self):
        #let the parent to the code
        super().say_hello()
        #add custom code
        print("I am rather tired")
    
    def __str__(self):
        return f'{self.name} attends {self.school}'

student = Student("Ahmed", "EOSL")
print(student)
#student.say_hello()
#student.sing_school_song()
#what are you?
# print(isinstance(student, Student))
# print(isinstance(student, Person))
# print(isinstance(Student, Person))