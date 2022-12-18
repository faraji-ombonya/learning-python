from time import time

def perfomance(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f"Took {t2-t1} seconds")
        return result
    return wrapper



@perfomance
def my_list(size):
    new_list = [item for item in range(0, size)]
    return print(new_list)

my_list(1000000)