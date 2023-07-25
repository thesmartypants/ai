
class Student:
   def __init__(self, name):
     self.name = name

   def display_name(self):
     print(f'My name is {self.name}.')

student1 = Student('Alice')
student1.display_name()