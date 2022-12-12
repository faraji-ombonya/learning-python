username = input("Username: ")
password = input("Password: ")

pass_length = len(password)
pass_hidden = '*' * pass_length

print(f"{username}, your password {pass_hidden}, is {pass_length} characters long.")