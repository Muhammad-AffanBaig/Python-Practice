# Practice Question 1 (Even Odd Checking)
num1 = int(input("Enter a Number: "))
if(num1%2 == 0):
    print("Number is Even")
else:
    print("Number is Odd")    

# Practice Question 2 (Positive , Negative or Zero Checking)
num2 = int(input("Enter a Number: "))
if(num2>0):
    print("Number is Positive ")
elif(num2<0):
    print("Number is Negative")
else:
    print("Number is Zero")        

# Practice Question 3 (Pass or Fail)
marks = int(input("Enter Marks: "))
if(marks>=50):
    print("Pass")
else:
    print("Fail")

# Practice Question 4 (Largest of Two Numbers)
a = int(input("Enter First Numbers: "))
b = int(input("Enter Second Number: "))
if(a>b):
    print(a,"is the Largest")
elif(a<b):
    print(b,"is the Largest")    

# Practice Question 5 (Voting Eligibility)
age = int(input("Enter your age: "))
if(age>=18):
    print("Eligible to Vote")
else:
    print("Not Eligible")

# Practice Question 6 (Simple Grading System)
Marks = int(input("Enter Your Makrs: "))
if(Marks>=90):
    print("A+")
elif(Marks>=75 and Marks<90):
    print("A")
elif(Marks>=60 and Marks<75):
    print("B")
elif(Marks>=50 and Marks<60):
    print("C")           
else:
    print("Fail")

# Practice Question 7 (Positve , Negative Number Checking Using Ternary Operator)
Number = int(input("Enter a Number: "))
result = "Positive Number " if(Number>0) else "Negative Number"
print(result)
                 