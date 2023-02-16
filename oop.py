class EmobilisStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
     print(f"My Name is {self.name} and iam {self.age} years old")



#creating an object
myobj=EmobilisStudent("Darius",21)

myobj.hello_me()


class KimelokCghurch:
    def __init__(self,location,ward):
        self.location=location
        self.ward=ward
    def hello_me(self):
     print(f"kimelok Church is located at {self.location} in {self.ward} ward kajiado west.")
#creating an object
myobj=KimelokCghurch("Oloorkunono","mosiro")
myobj.hello_me()



#creating a class magari,it should have mode,make,year properties
class Magari:
    def __init__(self,model,made,year):
        self.model=model
        self.made=made
        self.year=year
    def hello_me(self):

     print(f"The car model is {self.model} made in {self.made} in the year is {self.year}")

#creating an object
myobj=Magari("Toyota","japan",2013)
myobj.hello_me()









