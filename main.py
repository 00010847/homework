# name = input("Enter your name?")
# print("hello {}".format(name))
#

# Example 1 >
# this is the declaration of the function
def add_numbers(num1, num2):
    return num1 + num2

# this two numbers are arguments
print(add_numbers(2,2))


# Example 2
# this argument is value
add_numbers(1, 12)


number1 = 23
number2 = 45
# this argument is parametr
add_numbers(number1, number2)

# this argument is expression
add_numbers(12 + 23, 45 - 34)


# Example 3
# if we define local variable inside the function we cannot access it outside that function
# if w do that it throws an NameError
def my_function():
    name = "John"
    print(name)

# print(name)

# Example 4
# again function parametr is only visible inside that function we cannot access it outside anywhere
def show_name(name):
    print(name)

# print (name)

# Example 5
# varible defined outside the function is the global and functions can use it unless thier own local variable is named the same as global variable
# in such case function ignores the global varible and focuses on its own local variables!
category = "Food"
def cook_food():
    category = "Desert"
    print(category)
# for above reasons both variables global and local are treated differently by variable to the python interpreter
print(category)
cook_food()
