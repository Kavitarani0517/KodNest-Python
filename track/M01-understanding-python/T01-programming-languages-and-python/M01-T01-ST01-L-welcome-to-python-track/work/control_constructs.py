# Selection statements
# if statement
# Write a Python program to check whether a person is eligible to vote. If the age is 18 or above,print "Eligible to vote".
age=int(input("Enter the age: "))
if age >= 18:
    print("Eligible to vote")
print("Thank You")

# if-else statement
age=int(input("Enter the age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")

# Write a Python program to check whether a person is eligible to vote or not. If the age is 18 or above, print "Eligible to vote", otherwise print "Not eligible to vote".
# if-elif-else ladder
# Write a Python program to accept marks and print the grade using the following conditions: 90+ -> A, 70+ -> B,50+ -> C,35+ -> D, otherwise -> Fail.
marks=int(input("Enter the marks: "))
if marks>90:
    print("Grade A")
elif marks>70:
    print("Grade B")
elif marks>50:
    print("Grade C")
elif marks>35:
    print("Grade D")
else:
    print("Fail")

# Nested if statement
# Write a Python program to check whether you are free tonight. If you are free, check whether your friends are available. Print "Go out for party" if both are true; otherwise print the appropriate message.
free_tonight=True
friends_available=True
if(free_tonight):
    if(friends_available):
        print("Go out for party")
    else:
        print("Sit and watch the movie at home")
else:
    print("Not available for party")
    
# Match-case statement
# Write a Python program that accepts a number from  1 to 7 uses match-case to print the corresponding day of the week.
day=int(input("Enter a number between 1 to 7: "))
match day:
    case 1: print("Monday")
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Invalid")

# Match-case with multiple cases
# Write a Python program that accepts a month number and uses match-case to print the season: 3,4,5 -> Summer,6,7,8 -> Rainy, 9,10,11,12 -> Winter, and 1,2 -> Autumn.
month=int(input("Enter month number(1-12): "))
match month:
    case 3|4|5:
        print("Summer")
    case 6|7|8:
        print("Rainy")
    case 9|10|11|12:
        print("Winter")
    case 1|2:
        print("Autumn")
    case _:
        print("Invalid")

# Looping statements
# for loop with range
# Write a Python program to print numbers from 1 to 5 using a for loop.
for i in range(1,6):
    print(i)
# for loop - first 5 numbers
# Write a Python program to print the first five numbers starting from 0 using a for loop.
for i in range(5):
    print(i)
# for loop with if condition
# Write a Python program to print all even numbers from 1 to 10 using a for loop.
for i in range(1,11):
    if i%2==0:
        print(i)
# While loop
# Write a Python program to print numbers from 0 to 4 using a while loop.
i=0
while i<=4:
    print(i)
    i+=1


# Jumping statements
# break statement
# Write a Python program to print numbers from 1 to 5, but stop the loop when the nymber reaches 4.
for i in range(1,6):
    if i==4:
        break
    print(i)
print()
# Continue statement
# Write a Python program to print numbers from 1 to 5, but skip the number 4 using continue.
for i in range(1,6):
    if i ==4:
        continue
    print(i)
print()
# pass statement
# Write a Python program using a for loop from 1 to 9 and use pass as a placeholder inside the loop.
for i in range(1,10):
    pass
print()
# Write a Python program to create a function called add() without function definition.
def add():
    pass

# Return statement
# Write a Python program to function called square(n) that accepts a number and perform the square() function.
def square(n):
    return n*n
print(square(3))