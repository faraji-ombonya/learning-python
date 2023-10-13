#Exercise 
#Check for duplicates in a list

some_list = ['a','b','c','b','d','m','n','n']

new_list = []

for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in new_list:
            new_list.append(letter)

print(new_list)
