#my class
class Students:
    def __init__(stude, name, age):
        stude.name=name
        stude.age=age
    def say_Hello(stude):
        print(f"Hello, my name is {stude.name} and my age is {stude.age}")
# creating my object
Student1=Students("Darius", 21)
Student1.say_Hello()
Student2=Students("Rayann", 12)
Student2.say_Hello()
Student3=Students("Silas", 11)
Student3.say_Hello()
