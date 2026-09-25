# add 2 unmbers
# No arguements + No return value
def add1():
    a,b=10,10
    c=a+b
    print(c)
add1()

# No arguements + return values
def add2():
    a,b=10,10
    c=a+b
    return c
print(add2())

# Arguements + No return values
def add3(a,b):
    c=a+b
    print(c)
add3(10,20)

# Arguements + return values
def add4(a,b):
    c=a+b
    return c

res=add4(10,20)
print(res)

# return type
def calc(a,b):
    return a+b,a-b,a*b,a/b,a%b,a**b
sum,diff,prod,quo,rem,pow=calc(100,50)
print(sum)
print(diff)
print(prod)
print(quo)
print(rem)
print(pow)



