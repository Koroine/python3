x=1
marks=76
grades=90
#if statement
if x>0:
   print("The number is positive")

#if..else statement
if marks>=75:
    print("you have passed")
else:print("fail")
#if ..elif..else
if grades<=30 and grades>0:
    print("failed")
elif grades<=50 and grades>=30:
    print("passed")
elif grades<=80 and grades>=50:
    print("credit")
elif grades<=100 and grades>80:
    print("distinction")
else:
    print("wrong input")

# voting process
votes=10000
if votes<=5000:

    print("you are not allowed to fiy for any seat ")

elif votes<=6000 and votes:

    print("you can fiy for the seat")

elif votes>=10000 and votes>=600:

    print("you have won the election")

