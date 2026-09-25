print("----Arithmetic operator----")
x=15
y=4
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)
print(x//y)

print("----Assignment operators----")
x=10
print("starting value: x=",x)
x=10
print("\nAfter =:",x)
x+=5
print("\nAfter +=5:",x)
x-=3
print("\nAfter -=3:",x)
x*=2
print("\nAfter *=2:",x)
x/=4
print("\nAfter /=4:",x)
x//=2
print("\nAfter //=2:",x)
x%=3
print("\nAfter %=3:",x)
x=6
print("\nReset x=:",x)
x**=2
print("\nAfter **=2:",x)

print("----Logical operator----")
x=6
print("\nReset x=",x)
x&=3
print("\nAfter &=3:",x)
x|=2
print("\nAfter |=2:",x)
x^=5
print("\nAfter ^=5:",x)
x=4
print("\nReset x=:",x)
x<<=2
print("\nAfter <<=2:",x)
x>>=1
print("\nAfter >>=1:",x)

print("----Relational/Comparision operator----")
x=5
y=3
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

print("----Logical operstor----")
a=True
b=False
print("a and b=",a and b)
print("a or b=",a or b)
print("not a=",not a)
print("not b=",not b)

x=10
y=5
print("\n(x>5)and(y<10)=",(x>5) and (y<10))
print("\n(x<5)and(y<10)=",(x<5) and (y<10))
print("\n(x>5)or(y<10)=",(x>5) or (y<10))
print("\n(x<5)and(y<10)=",(x<5) or (y<10))
print("\nnot(x==10)=",not(x==10))
print("\nnot(y==3)=",not (y==3))

print("----Identity operator----")
x=["apple","banana"]
y=["apple","banana"]
z=x
print(x is y)
print(x==y)
print(x is z)

x=[1,2,3]
y=[1,2,3]
print(x==y)
print(x is y)

print("-----Membership operator-----")
fruits=["apple","banana","cherry"]
print("banana" in fruits)

fruits=["apple","banana","cherry"]
print("pineapple" not in fruits)
print("pineapple" in fruits)

text="Hello world"
print("h" in text)
print("hello" in text)
print("z" not in text)

print("----Bitwise operator----")
a=4
b=3
print("a & b =",a & b)
print("a | b ",a | b)
print("a ^ b =",a ^ b)
print("~ a =",~ a)
print("a << 1 =",a << 1)
print("a >> 1 =",a >> 1)

print("----Ternary operator----")
num=15
res="Even" if num % 2 == 0 else "odd"
print(res)

#WAP to find largest of 3 numbers using ternary operator
a=20
b=15
c=25
largest= a if a>b else b if b>c else c
print(largest)

#WAP to find the given number is positive or negative
a=-5
result="positive" if a > 0 else "negative"
print(result)
