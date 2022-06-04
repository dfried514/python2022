num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, number
boolean = True # variable declaration, boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # initialize tuple
print(type(fruit)) # log statement, type check
print(pizza_toppings[1]) # log statement, list access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # log statement, dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # log statement, tuple access value

if num1 > 45: # conditional if, primitive number
    print("It's greater") # log statement
else: # conditional else
    print("It's lower") # log statement

if len(string) < 5: # conditional if, primitive string length check
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if, primitive string length check
    print("It's a long word!")
else: # conditional else
    print("Just right!") # log statement

for x in range(5): # for loop, sequence, list access value
    print(x) # log statemnt, list access value
for x in range(2,5): # for loop, sequence, increment
    print(x) # log statement
for x in range(2,10,3): # for loop, increment
    print(x) # log statement
x = 0 # variable declaration, primitive number
while(x < 5): # while loop, stop
    print(x) # log statement
    x += 1 # increment

pizza_toppings.pop() # list delete value
pizza_toppings.pop(1) # list delete value
print(person) # log statement
person.pop('eye_color') # dictionary delete value
print(person) # log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # conditional if
        continue # continue
    print('After 1st if statement') # log statement
    if topping == 'Olives': # conditional if
        break # break

def print_hello_ten_times(): # function declaration
    for num in range(10): # for loop, sequence
        print('Hello') # log statement

print_hello_ten_times() # function invocation

def print_hello_x_times(x): # function declaration, parameter x
    for num in range(x): # for loop, sequence
        print('Hello') # log statement

print_hello_x_times(4) # function invocation, parameter 4

def print_hello_x_or_ten_times(x = 10): # function declaration, default parameter x = 10
    for num in range(x): # for loop, sequence
        print('Hello') # log statement

print_hello_x_or_ten_times() # function invocation
print_hello_x_or_ten_times(4) # function invocation, parameter 4



"""
Bonus section
"""

# print(num3) # log statement, primitive number, NameError: name <variable name> is not defined
# num3 = 72 # primitive number, change value
# fruit[0] = 'cranberry' # tuple change value, TypeError: 'tuple' object does not support item assignment
# print(person['favorite_team']) # dictionary access value, KeyError: 'favorite_team'
# print(pizza_toppings[7]) # list access value, IndexError: list index out of range
#  print(boolean) # log statement, IndentationError: unexpected indent
# fruit.append('raspberry') # tuple, AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) # tuple, AttributeError: 'tuple' object has no attribute 'pop'
