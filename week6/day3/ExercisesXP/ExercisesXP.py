# Exercises XP

# Exercise 1 : Hello World
x = ' hello world'
print(x*4)

# Exercise 2 : Some Math
result = (99**3) * 8
print(result)

# Exercise 3 : What Is The Output ?
#>>> 5 < 3  False
#>>> 3 == 3 True
#>>> 3 == "3" False
#>>> "3" > 3 typeError
#>>> "Hello" == "hello" False


# Exercise 4 : Your Computer Brand
computer_brand = 'self build'
print("I have a " + computer_brand + " computer")

# Exercise 5 : Your Information
name = "Ofir"
age = "32"
shoe_size = "46"
info = "my name is " + name + " I am " + age + " years old and my shoe size is " + shoe_size
print(info)

# Exercise 6 : A & B
a = 8
b = 4
if a > 4: print('Hello World')

# Exercise 7 : Odd Or Even
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))

# Exercise 8 : What’s Your Name ?
your_name = input("Enter your name: ")
if your_name.lower() == name.lower():
    print("we have the same name!!!!")
else:
    print("shame on you, your name is not ofir")

# Exercise 9 : Tall Enough To Ride A Roller Coaster
tall_enough = int(input("Enter your height in inches: "))
if (tall_enough * 2.54) > 145:
    print("You are tall enough to ride")
else:
    print("need to grow some more to ride")