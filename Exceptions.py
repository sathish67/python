try:
    number = int(input("Enter number: "))
    result = 10 / number
    print("Result:", result)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")


try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Finished")

age = -10

if age < 0:
    raise ValueError("Age cannot be negative")