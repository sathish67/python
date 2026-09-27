file = open("/Users/sathishg/Documents/python/filehandling/open.txt", "r")

content = file.read()

print(content)

file.close()


with open("/Users/sathishg/Documents/python/filehandling/open.txt", "r") as file:  # will import the file and close it automatically
    content = file.read()

print(content)