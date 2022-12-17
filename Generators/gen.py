def my_generator(num):
    for i in range(num):
        yield i
    
for i in my_generator(1000):
    print(i)