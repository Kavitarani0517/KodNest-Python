names=("Anjali","Kavya","Meenakshi")
print(names,type(names),len(names))
print(names.count("Anjali"))
print(names.index("Anjali"))
print(names[2])
print(names[-2])
d=names[0:3]
print(d,type(d))
#Looping the tuples
for n in names:
    print(n)
fruits=("Apple",)
print(fruits*3,type(fruits))
#Tuple constructor
stu_info=tuple(["kavya",15,23000,True])
print(stu_info,type(stu_info))

n=10
print(n,type(n))
numbers=1,2,3,4,5
print(numbers,type(numbers))
del numbers
fruits=("Apple","Banana","cherry")
(f1,*f2)=fruits
print(f1)
print(f2,type(f2))

a=10
b=20
c=30
numbers=(a,b,c)
print(numbers,type(numbers))
a=(1,2,3)
b=(4,5,6,7,8)
#print(a.extend(b)) is not possible on tuple
c=a+b
print(c,type(c))