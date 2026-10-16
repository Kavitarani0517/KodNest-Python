cities=["Bengaluru","Pune","chennai","Pune"]
unique_cities=set()
for n in cities:
    unique_cities.add(n.lower())
print(unique_cities)

new_cities={n.lower() for n in cities}
print(new_cities)

numbers=[2,3,2,4,3]
unique_squares=set()
for number in numbers:
    unique_squares.add(number*number)
print(unique_squares)

unique_squares_1={number*number for number in numbers}
print(unique_squares_1)

num=[5,12,18,7,12,20,5]
for number in num:
    if number%2==0:
        unique_even_={number}
print(unique_even_)

numbers=[5,12,18,7,12,20,5]
unique_even={number for number in numbers if number%2==0}
print(unique_even)

number=[2,3,4,5]
cube={}
for num in number:
    cube[num]=num**3
print(cube)

number=[2,3,4,5]
cube1={num:num**3 for num in number}
print(cube1)