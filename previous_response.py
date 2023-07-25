
class Car:
   def __init__(self):
     self.brand = 'Toyota'
     self.model = 'Camry'

   def display_car_info(self):
     print(f'Brand: {self.brand}, Model: {self.model}')

car1 = Car()
car1.display_car_info()