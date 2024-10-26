def read_int(prompt, min, max):
    while True:
        try:
            number = int(input(prompt))
        except ValueError:
            print("Error: wrong input")
            continue

        if not min < number < max:
            print(f"The value is not within permitted range ({min}..{max})")
            continue

        return number

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)
    