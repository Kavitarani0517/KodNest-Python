s1="Hello"
print(s1)
print(id(s1))
s1=s1+"World"
print(s1)
print(id(s1))
s1="Hello"
s2=s1+"World"
print(id(s1),s1)
print(id(s2),s2)
s3="Python"
s4="Python"
print(id(s3),s3)
print(id(s4),s4)
print(s3==s4)
print(s3 is s4)
s5="Python"
s6="python"
print(id(s5),s5)
print(id(s6),s6)
print(s5==s6)
print(s5 is s6)

#--------------STRINg SLICING----------------
st1="Python"
print(st1)
print(st1[2])
print(st1[5])
print(st1[1:4])
print(st1[0:5])
print(st1[ : ])
print(st1[ :4])
print(st1[2: ])
print(st1[1: ])
print(st1[0::1])
print(st1[0::2])
print(st1[1:5:2])
print(st1[ ::3])
print(st1[ 2:3])
print(st1[2:5:2])
print(st1[ :3])
print(st1[ 4:])
print(st1[ ::4])

#---------INTERVIEW QUESTIONS AND ANSWERS---------------
# ============================================================

# STRING SLICING - POSITIVE SLICING PRACTICE

# ============================================================

#

# Syntax:

# string[start:stop:step]

#

# Rules:

# 1. start is included

# 2. stop is excluded

# 3. positive step moves from left to right

# 4. If step is not given, default step is 1

#

# Try to predict the output before running each question.

# ============================================================





# ------------------------------------------------------------

# LEVEL 1 - BASIC start:stop

# ------------------------------------------------------------



# 1. Extract the first 3 characters

text = "Python"

print(text[0:3])#pyt





# 2. Extract characters from index 1 to 4

text = "Programming"

print(text[1:5])#rogr





# 3. Extract characters from index 2 to 5

text = "Developer"

print(text[2:6])#velop





# 4. Extract characters from index 3 to 6

text = "Computer"

print(text[3:7])#pute





# 5. Extract the first 4 characters

text = "Artificial"

print(text[0:4])#Arti





# 6. Extract characters from index 2 to 6

text = "Education"

print(text[2:7])#ucatio





# 7. Extract characters from index 4 to 9

text = "JavaScript"

print(text[4:10])#scr





# 8. Extract characters from index 4 to 9

text = "DataScience"

print(text[4:10])#ence





# ------------------------------------------------------------

# LEVEL 2 - MISSING START OR STOP

# ------------------------------------------------------------



# 9. Extract from beginning to index 5

text = "PythonProgramming"

print(text[:6])#Python





# 10. Extract from index 6 to the end

text = "PythonProgramming"

print(text[6:])#Programming





# 11. Extract from beginning to index 8

text = "FullStackDeveloper"

print(text[:9])#FullStac






# 12. Extract from index 9 to the end

text = "FullStackDeveloper"

print(text[9:])#Developer





# 13. Extract from beginning to index 6

text = "MachineLearning"

print(text[:7])#machine





# 14. Extract from index 7 to the end

text = "MachineLearning"

print(text[7:])#learning





# ------------------------------------------------------------

# LEVEL 3 - POSITIVE STEP

# ------------------------------------------------------------



# 15. Take every second character

text = "ABCDEFGHIJ"

print(text[0:8:2])#acegi





# 16. Take every second character

text = "ABCDEFGHIJ"

print(text[1:9:2])#BDFHJ






# 17. Take every third character

text = "ABCDEFGHIJKL"

print(text[0:12:3])#adgjm





# 18. Take every second character

text = "ABCDEFGHIJKL"

print(text[2:10:2])#cegi





# 19. Take every second number

text = "1234567890"

print(text[0:10:2])#24680





# 20. Take every second number starting from index 1

text = "1234567890"

print(text[1:9:2])#24680






# ------------------------------------------------------------

# LEVEL 4 - TRICKY POSITIVE SLICING

# ------------------------------------------------------------



# 21. Take every third character

text = "Programming"

print(text[0:11:3])#Pormi





# 22. Take every third character starting from index 1

text = "Programming"

print(text[1:10:3])#roag





# 23. Take every second character

text = "PythonProgramming"

print(text[2:14:2])#thrgmir





# 24. Take every third character

text = "PythonProgramming"

print(text[1:15:3])#yhnrnm





# 25. Take every second character

text = "ABCDEFGHIJKLMNO"

print(text[3:13:2])#DFHJLN





# 26. Take every third character

text = "ABCDEFGHIJKLMNO"

print(text[2:14:3])#CFIL





# ------------------------------------------------------------

# LEVEL 5 - INTERVIEW STYLE

# ------------------------------------------------------------



# 27. Predict the output

text = "PythonProgramming"

print(text[0:16:4])#Pti





# 28. Predict the output

text = "ABCDEFGHIJKLM"

print(text[1:12:3])#BEHK





# 29. Predict the output

text = "DataScienceWithPython"

print(text[4:18:2])#SceWihv





# 30. Predict the output

text = "FullStackDevelopment"

print(text[2:19:3])#LtaDlv






# ------------------------------------------------------------

# CONCEPT QUESTIONS

# ------------------------------------------------------------



# 31. Compare the following

text = "Python"



print(text[1:5])#yth

print(text[1:5:1])#yth

print(text[1:5:2])#yh





# 32. What happens when start > stop?

text = "Python"

print(text[4:2])# 





# 33. What happens when start == stop?

text = "Python"

print(text[2:2])#





# 34. What happens when indexes are outside the string?

text = "Python"

print(text[10:20])#





# 35. What happens when stop is larger than the string length?

text = "Python"

print(text[0:100])#Python





# ------------------------------------------------------------

# BONUS CHALLENGES

# ------------------------------------------------------------



# 36. Predict the output

text = "ABCDEFGHIJKLM"

print(text[2:11:3])#CFI





# 37. Predict the output

text = "ProgrammingLanguage"

print(text[3:15:2])#gamnLn





# 38. Predict the output

text = "PythonDeveloper"

print(text[1:12:3])#yoel





# 39. Predict the output

text = "DataScience"

print(text[0:10:2])#DtSin





# 40. Predict the output

text = "FullStackDeveloper"

print(text[4:16:2])#Sakeeo