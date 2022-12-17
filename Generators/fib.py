# fibonacci generator
def fib(num):
    a = 0
    b = 1    
    for i in range(num + 1):
        if i == 0:
            yield 0
            continue
        if i == 1:
            yield 1
            continue
        n = a + b
        a = b
        b = n 
        yield n

for i in fib(20):
    print(i)


