grade=float(input("Enter Your Grade"))
if grade>=80:
    print("You got an A")
elif grade>=75 and grade<=79:
    print("You got A-")
elif grade>=70 and grade<=74:
    print("You got B+")
elif grade>=65 and grade<69:
    print("You got B")
elif grade>=60 and grade<=64:
    print("You got B-")
elif grade>=55 and grade<=59:
    print("You got C+")
elif grade>=50 and grade<=54:
    print("You got C")
elif grade>=45 and grade<=49:
    print("You got C-")
elif grade>=40 and grade<=44:
    print("You got D+")
elif grade>=35 and grade<=39:
    print("You got D")
elif grade>=30 and grade<=34:
    print("D-")
elif grade>=0 and grade<=29:
    print("E")
else:
    print("Marks not awarded")
