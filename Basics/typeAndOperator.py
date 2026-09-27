x = "100"

x = int(x)

print(x)
print(type(x))

int("10")
float("10.5")
str(100)
bool(1)
list("hello")

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)

a = 10
b = 20

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

#logical operators
age = 25

print(age > 18 and age < 60)
print(age < 18 or age > 60)
print(not age > 18)


marks = 85

if marks >= 90:
    print("A")
elif marks >= 75:
    print("B")
elif marks >= 60:
    print("C")
else:
    print("Fail")

age = 20

result = "Adult" if age >= 18 else "Minor"

print(result)

for i in range(5):
    print(i)

for i in range(1, 10, 2):
    print(i)

names = ["John", "Bob", "Alice"]

for index, name in enumerate(names):
    print(index, name)

i = 0

while i < 5:
    print(i)
    i += 1

for i in range(10):

    if i == 5:
        break

    print(i)
for i in range(5):

    if i == 2:
        continue

    print(i)

for i in range(5):

    if i == 2:
        pass # do nothing

    print(i)