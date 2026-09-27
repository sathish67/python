square = lambda x: x * x

print(square(5))


add = lambda a, b: a + b

print(add(10, 20))


employees = [
    ("John", 50000),
    ("Bob", 30000),
    ("Alice", 70000)
]

employees.sort(key=lambda employee: employee[1])

print(employees)



numbers = [1, 2, 3, 4, 5, 6]
# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6]


numbers = [1, 2, 3, 4]
# Double every number
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)  # Output: [2, 4, 6, 8]


pairs = [(1, 'one'), (3, 'three'), (2, 'two')]
# Sort the tuples by their second element (alphabetically by string)
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  # Output: [(1, 'one'), (3, 'three'), (2, 'two')]


# Procedural approach
squares = []
for n in range(5):
    if n % 2 == 0:
        squares.append(n ** 2)

print(squares) # Output: [0, 4, 16]


squares = [n ** 2 for n in range(5) if n % 2 == 0]
print(squares) # Output: [0, 4, 16]


pairs = [('a', 1), ('b', 2)]
my_dict = dict(pairs) # {'a': 1, 'b': 2}



even_squares = {x: x**2 for x in range(1, 6) if x % 2 == 0}
# Output: {2: 4, 4: 16}


# Set literal (hardcoded values)
digits = {1, 2, 3, 4, 5}

# Set constructor (converts a list into a set to eliminate duplicates)
numbers = [1, 2, 2, 3, 3, 3]
unique_numbers = set(numbers)  # Result: {1, 2, 3}



# Task: Take a list of numbers, double them, and keep only unique values
numbers = [1, 2, 2, 3, 4, 4]

# Set comprehension handles the loop, the operation (* 2), and deduplication
doubled_set = {x * 2 for x in numbers}  
# Result: {2, 4, 6, 8}

# Adding a filter condition (only process even numbers)
even_squares = {x ** 2 for x in numbers if x % 2 == 0}
# Result: {4, 16}

