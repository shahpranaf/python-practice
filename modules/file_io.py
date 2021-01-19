my_file = open("test.txt")

print(my_file)
print(my_file.read())

print("===============\n")
my_file.seek(0) # to move cursor back to first letter of first line
print(my_file.read())
my_file.seek(0)
print("===============\n")

print(my_file.readline())
print(my_file.readline())
my_file.seek(0)
print("===============\n")

print(my_file.readlines()) # for list of lines

my_file.close()