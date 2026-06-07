fruits = []
for i in range(5):
    name = input("Enter a fruit name: ")
    fruits.append(name)
print(fruits)
print("first fruit:",fruits[0])
print("last fruit:",fruits[-1])

numbers = []
sum = 0
for i in range(5):
    integer = int(input("Enter a number: "))
    numbers.append(integer)
    sum += integer
    
print(numbers)
print("Sum of integers:",sum)
numbers = []
countE = 0
countO = 0
for i in range(6):
    digit = int(input("enter a number: "))
    numbers.append(digit)
    if(digit % 2 == 0):
        countE+=1
    else:
        countO+=1    
print(numbers)
print("Even Numbers:",countE)
# print("Odd Numbers:",countO)
numbers = []
for i in range(7):
    digit = int(input("Enter a Number: "))
    numbers.append(digit)
    
max = numbers[0]
min = numbers[0]
for j in range(7):
    if (numbers[j]>max):
        maximum = numbers[j]
    elif( numbers[j]<min):
        minimum = numbers[j]        
print(numbers)            
print("Maximum Number:",max)
print("Minimum Number:",min)
names = []
found = False
for i in range(5):
    name = input("Enter Name: ")
    names.append(name)
inputName = input("Enter name to find: ")
for i in range(5):
    if(inputName == names[i]):
        found = True
        break
if (found):
     print("Found")
else:
    print("Not found")
numbers = []
found = False
for i in range(8):
    digit = int(input("Enter a Number: "))
    numbers.append(digit)
countNumber =int(input("Enter a number to find its occurence: "))
for i in numbers:
    if(countNumber == i):
        found = True    
        break
if(found):
    x = numbers.count(countNumber)
    print(x)
else:
    print("Entered number is not in the list")
numbers =[]
for i in range(5):
    digit = int(input("Enter a number: "))
    numbers.append(digit)
numbers.reverse()
print(numbers)
reverse = numbers[::-1]
print("reverse of list:",reverse)
numbers = []
sum = 0
for i in range(5):
    digit = int(input("Enter a Numnber: "))
    numbers.append(digit)
    sum += digit
print("Sum:",sum)
print("Average:",sum/len(numbers))
shopping = []
for i in range(5):
    item = input("Enter the shopping items: ")
    shopping.append(item)
removedItem = input("Enter Item to remove from list: ")
shopping.remove(removedItem)
print(shopping)
names = []
print("Enter 5 names: ")
for i in range(5):
    name = input()
    names.append(name)
insertname = input("enter a name to insert into list: ")
nameIndex = int(input("Enter a position: "))
names.insert(nameIndex,insertname)
print(names)    
names = input("Enter 5 names separated by space: ").split()
count = 0
for element in names:
    for ch in element:
        if(ch.lower() in "aeiou"):
            count +=1
print("Total vowels:",count)            









    



