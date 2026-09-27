age = 25
count = -100
print(type(age))  # Output: <class 'int'>


price = 99.9
temperature = -5.5

print(type(price))  # Output: <class 'float'>


is_active = True
is_admin = False

print(type(is_active))  # Output: <class 'bool'>

name = "Python"
print(name[0])
print(name[-2])
print(name)
print(name[0:-2]);

print(type(name))  # Output: <class 'str'>


result = None

print(type(result))  # Output: <class 'NoneType'>


# Using literals
z1 = 3 + 4j
print(type(z1))  # Output: <class 'complex'>

# Using the constructor
z2 = complex(2.5, -3.7) 
print(z2)        # Output: (2.5-3.7j)

# Missing arguments default to 0
z3 = complex(5)  # Output: (5+0j)
z = 5 + 2j

print(z.real)       # Output: 5.0
print(z.imag)       # Output: 2.0
print(z.conjugate())# Output: (5-2j)

# Arithmetic
print(z * 2)        # Output: (10+4j)


# An empty list
empty_list = []

# A list of integers
numbers = [1, 2, 3, 4]

# A list with mixed data types
mixed_list = ["Python", 3.14, True, 42]

# Creating a list using the list() constructor
built_in_list = list((1, 2, 3))  # Converts a tuple to a list


print(empty_list)      # Output: []
empty_list.append(10)
empty_list.insert(0,89)
empty_list.extend([89, 30, 40])
empty_list.remove(89)
print(empty_list.pop(0))
print(empty_list)      # Output: [10, 89, 30, 40]
empty_list.sort()
print(empty_list)      # Output: [10, 30, 40, 89]
empty_list.reverse()
print(empty_list)      # Output: [89, 40, 30, 10

my_list = ["apple", "banana", "cherry"]

print(len(my_list))          # Output: 3
print("banana" in my_list)   # Output: True
combined = my_list + [1, 2]  # Output: ['apple', 'banana', 'cherry', 1, 2]


# Empty tuple
empty_tuple = ()

# Tuple with mixed data types
coordinates = (4, 12)
user_profile = ("Alice", 28, "Engineer")

# Implicit packing (parentheses are optional but recommended)
numbers = 1, 2, 3 

# CRITICAL: A single-item tuple REQUIRES a trailing comma
wrong_tuple = ("apple")  # This is just a string!
right_tuple = ("apple",) # This is a tuple
print(type(wrong_tuple))  # Output: <class 'str'>
print(type(right_tuple))  # Output: <class 'tuple'>

fruits = ("apple", "banana", "cherry", "date")

print(fruits[0])    # Output: 'apple' (First item)
print(fruits[-1])   # Output: 'date'  (Last item)
print(fruits[1:3])  # Output: ('banana', 'cherry') (Slicing)

point = (10, 20, 30)
x, y, z = point

print(x)  # Output: 10
print(y)  # Output: 20
print(z)  # Output: 30

print(point.count(20))
print(point.index(30))# Using curly braces

fruits = {"apple", "banana", "cherry"}

# Using the set() constructor (e.g., converting a list to a set)
numbers_list = [1, 2, 2, 3, 4, 4]
unique_numbers = set(numbers_list)  # Automatically removes duplicates
print(unique_numbers)  # Output: {1, 2, 3, 4}

# CRITICAL: To create an empty set, you MUST use set(). 
# Using {} creates an empty dictionary.
empty_set = set()

empty_set.add(10)
empty_set.add(20)
empty_set.update([30, 40, 50])
empty_set.remove(20) # if not matches error thrown
empty_set.discard(100)  # Does not raise an error if the element is not found
print(empty_set)  # Output: {10, 30, 40, 50
empty_set.clear()  # Removes all elements from the set

setA = {1, 2, 3}
setB = {3, 4, 5}

# Union (combines all unique elements)
print(setA | setB)          # Output: {1, 2, 3, 4, 5}
print(setA.union(setB))     # Alternative method syntax

# Intersection (items present in both)
print(setA & setB)          # Output: {3}
print(setA.intersection(setB))

# Difference (items in setA but not in setB)
print(setA - setB)          # Output: {1, 2}
print(setA.difference(setB))


# Using curly braces (most common)
user_profile = {
    "username": "coder123",
    "followers": 2500,
    "is_active": True
}

# Using the dict() constructor
empty_dict = dict()# Using square brackets
print(user_profile["username"])  # Output: coder123

# Using .get() (Returns None or a default value instead of a KeyError if the key doesn't exist)
print(user_profile.get("location", "Unknown"))  # Output: Unknown


user_profile["followers"] = 2501  # Updates the existing key
user_profile["location"] = "New York"  # Adds a new key-value pair


del user_profile["is_active"]  # Removes "is_active" key
removed_val = user_profile.pop("followers")  # Removes "followers" and returns its value

inventory = {"apples": 10, "bananas": 5, "oranges": 8}

# 1. Loop through keys
for fruit in inventory.keys():
    print(fruit)

# 2. Loop through values
for count in inventory.values():
    print(count)

# 3. Loop through both (items)
for fruit, count in inventory.items():
    print(f"We have {count} {fruit}.")

inventory.update({"bananas": 7, "grapes": 15})  # Updates existing and adds new key-value pairs
inventory.clear()
