#Normal assignment
original=[[10,20],[30,40]]
copy=original
copy[0][0]=100
print(copy)
print(original)

#Shallow copy
original=[[10,20],[30,40]]
copy=original.copy()
copy[0][0]=100
print(copy)
print(original)

#Deep copy
import copy
original=[[10,20],[30,40]]
copy_li=copy.deepcopy(original)
copy_li[0][0]=100
print(copy_li)
print(original)

#Comprehension
original=[[10,20],[30,40]]
copy_li=[x.copy() for x in original]
copy_li[0][0]=100
print(copy_li)  
print(original)