def read_my_name(func):
  name = "Andy"
  name_thing = func(name)

  return name_thing

def make_a_phrase(name):
  return f"Hi.  My name is {name}"

print(read_my_name(make_a_phrase))

def add(num1, num2): return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def calculator(func):
  return func(3,4)

result = calculator(add)
print(result)

result = calculator(subtract)
print(result)

# ======================================

# this runs the top level function, which is to define not run add_curtains.  This is the decorator function
# def interior_decorator(func):
#     func()
#     print(f"Now my house has purple curtains")
#   return add_curtains

# Functions to pass in

# def move_in():
#   print("My house was empty, but...")

# def redecorate():
#   print("I used to have boring beige curtains")  

# storing a function in a variable that takes another function as a variable.  The variable is equal to the result of the function

# new_house = interior_decorator(move_in)
# redecorated_house = interior_decorator(redecorate)



# new_house()
# redecorated_house()

# or use the below

# ======================================

# shorter version of decorating, using less variables

def interior_decorator(func):
  def add_curtains(color):
    if color == "orange":
      color = "ugly-ass"
    func(color)
    print(f"Now my house has {color} curtains")

  return add_curtains
@interior_decorator
def move_in(color):
  print("My house is empty")

print("shorter version: ")
move_in("orange")