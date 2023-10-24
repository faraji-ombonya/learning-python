# A tuple consists of a number of values separated by commas, for instance
t = 12345, 54321, 'hello!'
print(t)
print(t[0])

# tuples may be nested
u = t, (1,2,3,4,5)
print(u)

# Tuples are immutable
# t[0] = 888

# but they can contain mutable objects
v = ([1, 2, 3], [3, 2, 1])
print(v)

# a tuple with zero items
t = ()

# a tuple with 1 item: note the trailing comma
t = 1,