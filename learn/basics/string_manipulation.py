#Concatination
str1 = "Hello"
str2 = "World"
print(str1 + " " + str2)
#Repetition
print(str1*3)
#Slicing or Substring
str3 = "Hello World!"
print(str3[0:5]) #First 5 Characters
print(str3[-6:]) #Last 6 Characters
#Length of a String
print(len(str1))
#Case Conversion
print(str3.upper())
print(str3.lower())
#Replace a substring
print(str3.replace("World", "Python"))
#Split into a list
fruits = "apple,banana,cherry"
fruitList = fruits.split(",")
print(fruitList)
#Join list into a string
lotsOfFruits = ["apple", "banana", "cherry"]
joinIntoString = ", ".join(lotsOfFruits)
print(joinIntoString)
#String formatting
name = "Alice"
age = 35
print("My name is {} and I am {} years old.".format(name, age))
print(f"MY name is {name} and I am {age} years old.")