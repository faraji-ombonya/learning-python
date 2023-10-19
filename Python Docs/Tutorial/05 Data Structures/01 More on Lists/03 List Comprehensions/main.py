# creating a list with a for loop
squares = []

for x in range(10):
    squares.append(x**2)
print(squares)

# creating the same list with a lambda function in a list comprehension
squares = list(map(lambda x: x**2, range(10)))
print(squares)

# creating the same list with a list comprehension
squares = [x**2 for x in range(10)]
print(squares)


# Example 2
combs = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            combs.append((x,y))

print(combs)

# Example 2 with a list comprehension
combs = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(combs)


# Example 3
vec = [-4, -2, 0, 2, 4]
print(vec)

# create a new list with the values doubled
vec_2 = [x * 2 for x in vec]
print(vec_2)

# filter the list to exclude negative numbers
vec_3 = [x for x in vec if x >= 0]
print(vec_3)

# apply a function to all the elements
vec_4 = [abs(x) for x in vec]
print(vec_4)

# call a method on each element
freshfruit = [' banana', ' loganberry ', 'passion fruit ']
fresh = [weapon.strip() for weapon in freshfruit]
print(fresh)

# create a list of 2-tuples like (number, square)
numbers = [(x, x**2) for x in range(6)]
print(numbers)

# flatten a list using a listcomp with two 'for'
vec_5 = [[1,2,3], [4,5,6], [7,8,9]]
vec_6 = [num for elem in vec_5 for num in elem] 
print(vec_6)
