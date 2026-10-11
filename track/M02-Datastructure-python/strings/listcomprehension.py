# List comprehension to create aand append the values to list
#square of number
square=[]
for i in range(1,6):
    square.append(i*i)
print(square)

square=[i*i for i in range(1,6)]
print(square)

numbers=[i for i in range(1,11) if i%2==0]
print(numbers)

numbers=[10,3,12,43,7]
new_list=[i for i in numbers if i>=10]
print(new_list)

names=["ravi","abhi","sita","geeta"]
new_list=[n.upper() for n in names]
print(new_list)

# Cube of Numbers: 
cube=[]
for i in range(1,6):
    cube.append(i*i*i)
print(cube)

# Create a list of cubes of numbers from 1 to 10 using list comprehension.
n=int(input("Enter the number: "))
cube=[i*i*i for i in range(1,n+1)]
print(cube)
# Positive Numbers: 
pos=[]
for i in range(1,11):
    if i>0:
        pos.append(i)
print(pos)
# Extract all positive numbers from a given list.
# nums = [-5, 10, -2, 20, 0, 15, -8]
nums=[-5,-10,-2,-20,0,15,-8]
pos=[num for num in nums if num>0]
print(pos)
# Words Starting with a Vowel: 
words=["Apple","Banana","Orange","Grapes","Umbrella"]
vowels="aeiou"
for i in words:
    if i[0].lower() in vowels:
        print(i,"starts with vowel")
    else:
        print(i,"does not starts with vowel")
# Extract all words that start with a vowel.
# words = ["Apple", "Banana", "Orange", "Grapes", "Umbrella"]
word=["Apple", "Banana", "Orange", "Grapes", "Umbrella"]
vowels="aeiou"
vowel=["vowel" if i[0].lower() in vowels else "Not vowel" for i in word]
print(vowel)
# Even or Odd: 
num=[]
for i in num:
    if i%2==0:
        print("Even")
    else:
        print("Odd")
# Create a list that labels each number as "Even" or "Odd" for numbers from 1 to 10.
num=["Even" if i%2==0 else "Odd" for i in range(1,11)]
print(num)
# Extract Vowels:
#  Extract all vowels from a given string using list comprehension.
# text = "programming"
text="programming"
vowels="aeiou"
word=[i for i in text if i.lower() in vowels]
print(word)
# Word Lengths: 
# Create a list containing the length of each word.
# words = ["Python", "Java", "React", "Django"]
word=["Python", "Java", "React", "Django"]
new=[len(i) for i in word]
print(new)
# Remove Duplicates:
#  Remove duplicate elements from a list while preserving the original order.
# nums = [1, 2, 3, 2, 4, 1, 5]
nums = [1, 2, 3, 2, 4, 1, 5]
numbers=[i for i in nums if i not in nums[i+1:]]
print(numbers)
# Flatten a Nested List: Convert a nested list into a single list.
# matrix = [[1, 2], [3, 4], [5, 6]]
matrix = [[1, 2], [3, 4], [5, 6]]
n=[i for i in matrix for j in i]
print(n)
# Find Common Elements: Find elements present in both lists using list comprehension.
# a = [1, 2, 3, 4, 5]
# b = [3, 4, 5, 6, 7]
a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
common=[i for i in a if i in b]
print(common)
# Find Prime Numbers: Generate all prime numbers between 1 and 100 using list comprehensions
prime=["prime" if i>1 and all(i%n!=0 for n in range(2,i)) else "Not prime"  for i in range(1,101)]
print("Prime numbers between 1 to 100:",prime)



