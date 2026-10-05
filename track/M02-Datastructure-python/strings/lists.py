numbers=[1,2,3,4,5,3]
print(numbers)
print(numbers[3])#4

number=[1,3,2,5,4]
print(number)
print(len(number))#5
print(type(number))

li=list(['Kavi',45.7,True,23])
print(li,type(li))
print(number[1:4])#3,2,5
print(number[3:5])#5,4
print(number[-4:-1])#3,2,5

num=[1,2,3,4,5]
print(num)
num.append(6)
num.insert(0,3)
num.extend([6,7,8])
num.pop()
num.pop(1)
print(num.remove(2))
print(num)
print(num.clear())
print(num)
del num

num=[1,2,3,4,6]
num[4]=5
num[1:4]=[20,30,40]
print(num)

a=[1,2,3]
b=a.copy()
print(b.index(3))
print(b)

lis=[1,3,2]
lis.sort(reverse=True)
print(lis)

liss=['a','b','d','c']
liss.sort(reverse=True)
print(liss)

