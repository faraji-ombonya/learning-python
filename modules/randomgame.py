from sys import argv
from random import randint

try:
    first_num = int(argv[1])
    last_num = int(argv[2])
except ValueError:
    print("Please enter a number")
    exit()
except IndexError:
    print("Please enter a valid Range, example 1 10")
    exit()
    
try:
    lucky_num = randint(first_num, last_num)
except:
    print("oops")
    exit()

while True:
    user_num = int(input(f"Select Your Lucky Number from {first_num} to {last_num}: "))
    if lucky_num == user_num:
        print("You won the lotto. Congratulations genious")
        break
    else:
        print("Keep trying")