def hello():
    print("This is my first function")
hello()

def calculate ():
    print("x*y")
calculate()

def majina(fname,lname):
    print(fname+" "+lname)
majina("Darius","koroine")
majina("Rayann","Darius")
majina("Dennis","koroine")
majina("silas","koroine")
majina("peter","koroine")


def greetings(name,greetings="hello"):
    print(greetings +" "+ name)

greetings("Daniel")

greetings("Niaje","Sylivia")
greetings("Sylivia","Niaje")

def arguments(name,argument="leo ulienda wapi mchana haukuwa kwa nyumba"):
    print(argument +" "+ name)
arguments("Solomon")
arguments("usijaribu tena","solomon")


#function to print max and min values

def maximumvalue(a, b, c,d, e, f):
    return max(a,b,c,d,e,f)
result=maximumvalue(7,9,1,17,8,45)
print(result)


def minivalue(a,b,c,d,e,f):

    return min(a,b,c,d,e,f)

result=minivalue(1,3,5,7,9,7)

print(result)

#function to sort lis
def sort_list(list):
    return sorted(list)
answer=sort_list([3,4,6,2,7,8,10,5,1,9])

print(answer)

#function to print_out numbera
def print_numbers(n):
    for i in range(n):
        print(i)
print_numbers(7)
