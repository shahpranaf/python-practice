# r, r+, a, w

with open("test.txt", mode='r+') as my_file: 
    text = my_file.write('Hi this is PRanav')

    print(text)

with open("test1.txt", mode='w') as my_file:
    text = my_file.write(" 'w' mode creates file if not exists and replace old data")
