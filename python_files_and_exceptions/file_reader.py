with open('C:/Users/karen/Desktop/python_tutorial/python_files_and_exceptions/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())

# rstrip method removes, or strips, any whitespace characters from the right side of a string.


filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))