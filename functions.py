def greet(name):
    print("Hello", name)

greet("Sathish")

def add(a, b):
    return a + b

result = add(10, 20)

print(result)


def greet(name="User"):
    print("Hello", name)

greet()
greet("Sathish")

def employee(name, age):
    print(name, age)

employee(age=25, name="Sathish")


def multiply_numbers(*args):
    # 'args' is treated as a tuple under the hood
    result = 1
    for num in args:
        result *= num
    return result

# You can pass 2, 3, or more numbers seamlessly
print(multiply_numbers(2, 3))        # Output: 6
print(multiply_numbers(2, 3, 4, 5))  # Output: 120


def print_profile(**kwargs):
    # 'kwargs' is treated as a dictionary under the hood
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_profile(username="dev_mindy", role="Admin", status="Active")
# Output:
# username: dev_mindy
# role: Admin
# status: Active


def master_function(required_arg, *args, **kwargs):
    print(f"Required: {required_arg}")
    print(f"Extra positional (args): {args}")
    print(f"Extra keyword (kwargs): {kwargs}")

master_function("Hello", 1, 2, 3, mode="dark", layout="grid")
# Output:
# Required: Hello
# Extra positional (args): (1, 2, 3)
# Extra keyword (kwargs): {'mode': 'dark', 'layout': 'grid'}


