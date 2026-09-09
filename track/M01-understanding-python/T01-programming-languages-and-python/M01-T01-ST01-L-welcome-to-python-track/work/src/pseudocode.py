# To print Hello world

# To find whether the given number(n) is even or odd

# To find the number is positive,negative or zero

# To find the largest among 3 numbers a,b,c

'''START
SHOW "Hello World"
END

START
READ n
IF n%2==0 
  show "even"
otherwise
  show "odd"
END

START
READ n
IF n>0
  SHOW "Positive"
OTHERWISE IF n<0
  SHOW "Negative"
OTHERWISE
  SHOW "Neutral or Zero"
END

START
READ a,b,c
IF a>b and a>c
   SHOW "a is largest"
OTHERWISE IF b>a and b>c
   SHOW "b is largest"
OTHERWISE
   SHOW "c is largest"
END

a=int(input("Enter a value:"))
b=int(input("Enter b value:"))
c=int(input("Enter c value:"))
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")'''

a=10
b=20
c=30
if a>b and a>c:
    print("a is largest")
elif b>a and b>c:
    print("b is largest")
else:
    print("c is largest")

