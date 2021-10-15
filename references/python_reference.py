## Python Refresher
# this is an integer
int_1 = 12

# this is a float
float_1 = 12.4444

# this is a string
str_1 = "test"

# let's make sure!
print(type(int_1))
print(type(float_1))
print(type(str_1))


# Lists
list_1 = [2, 3, 4, 5]
list_2 = ["apple", "orange", "pineapple"]

# print the second element of list_1
print(list_1[1])

# print the third element of list_2
print(list_2[2])


# Dictionaries
dict_1 = {
    "model": "Ford",
    "color": "red",
    "year": 1998
}

# print the color
print(dict_1["color"])


# Functions
def function_1():
    print("hello from a function!")

function_1()

# here is a function with a parameter
def function_2(x):
    return x+2

print(function_2(3))


# Loops and if/else
for i in list_1:
    if i > 3:
        print(i, " is greater than 3")
    elif i < 3:
        print(i, " is less than 3")
    else:
        print(i)


## Classes and Objects

# this is a class called Pet()
class Pet():

    # this is an attribute
    status = "adopted"

    # this is the constuctor function
    def __init__(self, species, name, age):
        self.species = species
        self.name = name
        self.age = age
    
    # this is a method
    def noise(self):
        return 'meow meow meow'

# this is an instance or object of the class Pet()
cat_1 = Pet("cat", "Toulouse", 11)

# print toulouse's species
print(cat_1.species)

# call the function noise()
print(cat_1.noise())
