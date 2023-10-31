if __name__ == '__main__':
    s = input()

    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    for char in s:
        if char.isalnum():
            alnum = True
            break
    print(alnum)

    for char in s:
        if char.isalpha():
            alpha = True
            break
    print(alpha)

    for char in s:
        if char.isdigit():
            digit = True
            break
    print(digit)

    for char in s:
        if char.islower():
            lower = True
            break
    print(lower)

    for char in s:
        if char.isupper():
            upper = True
            break
    print(upper)
