class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print(x.brand)
    print(x.model)
    print("Moved")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def __init__(self,brand,model,speciality):##overide
    self.brand=brand
    self.model=model
    self.speciality=speciality
  def move(self):##overload
     print(x.brand)
     print(x.model)
     print(x.speciality)

class Plane(Boat):
  pass

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20","Sail") #Create a Boat object
plane1 = Plane("Boeing", "747","Fly") #Create a Plane object

for x in (car1, boat1, plane1):
  
  x.move()