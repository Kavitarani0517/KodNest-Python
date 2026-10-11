#Sets are unorderd,unindexed,and immutable,unchangeable
#Sets doesnot allow duplicate values

s={1,2,3,4,5}
print(s)
print(type(s),s)
#we canot aaccess the elements usng index values print(s,s[1])Not possible
#we cannot perform any oerations on set using index values s[2]=300 Not possible
s.add(6)
s.update({7,8,9})
#s.remove(10) it removes the element and if element is not found it throws an error
s.discard(10)#it removes the element and if element is not found it excutes without any output and error message
s.pop()#it removes a random elementin set
s.clear()
del s

s1={1,2,3,"Hello",1.2,True,0,1.2345,1,2,False}
print(s1)

#Constructors os set
s2=set()#It creates an empty set
print(s2,type(s2))#It return the empty set and type of set
s3=set([1,2,3,4])
print(s3,type(s3))
#We can access the elements inthe sets using the for loop 
for n in s3:
    print(n)

#Frozenset
fs=frozenset([1,2,3])
print(fs,type(fs))
#fs.add(6) it shows error and it is not possible to add an element to frozenset.

#Mathametical operations in set
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))
print(set1 | set2)#it combines both the sets together by eliminating the duplicate values
print(set1.intersection(set2))
print(set1 & set2)#it gives common elements from both the sets
print(set1.isdisjoint(set2))#it return true if all the elments of set a are not present in set b
print(set1.issuperset(set2))#it returns true if all the elements of set b are present in set a
print(set1.issubset(set2))#it returns true if all the elements of set b are present in set a

print(set1.union(set2))
print(set1.difference(set2))#it gives the elements of set a which are not present in set b
print(set1-set2)
print(set2.difference(set1))
print(set2-set1)
print(set1.symmetric_difference(set2))#it gives the elements of set a and set b which are not present in both
print(set1^set2)

#set methods
set1.add(6) 
print(set1)#{1,2,3,4,5,6}
set1.update(set2)
print(set1)#{1,2,3,4,5,6,7,8}
set1.remove(6)
print(set1)#{1,2,3,4,5,7,8}
set1.discard(6)
print(set1)#{1,2,3,4,5,7,8}
set1.pop()
print(set1)#{2,3,4,7,8}
set1.clear()
print(set1,len(set1))#{}
