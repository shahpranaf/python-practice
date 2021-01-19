import sys
from random import randint

args = sys.argv

start = 0
end = 10
if(2 < len(args)):
    start = int(args[1])
    end = int(args[2])

number = randint(start, end+1)
print(number)
while True:
    try:
        guess = int(input(f"Please guess a number between {start} and {end} : "))
        
        if(number == guess):
            print("You are genius")
            break
    except ValueError:
        print("Please enter numbers only")
        continue
