from collections.abc import Iterable

# mypy does not report if you dont have type anotaions
print("Hello world")

def greeting(name):
    return 'Hello ' + name

greeting(123)
greeting(b"Alice")

# lets add type annotations
def second_greeting(name: str) -> str:
    return 'Hello ' + name

# mypy is now able to report errors because we have type hints
second_greeting(3)
second_greeting(b'Alice')

second_greeting("World!")

# mypy also detects incorrect usage of variables inside a function
# provided we provide type hints
def bad_greeting(name: str) -> str:
    return "Hello " * name

# More complex types
# list containing strings
def greet_all(names: list[str])-> None:
    for name in names:
        print("Hello " + name)

names = ["Mike", "Jim", "Pam", "Andy"]
ages = [10, 12, 14, 17]

greet_all(names)
greet_all(ages)


# Lets have one that takes any iterable of strings
def second_greet_all(names: Iterable[str]) -> None:
    for name in names:
        print("Hello " + name)

# one that takes either ints or strings
def normalize_id(user_id: int | str) -> str:
    if isinstance(user_id, int):
        return f'user-{100_000 + user_id}'
    else:
        return user_id
    
# type inferance
def nums_below(numbers: Iterable[float], limit: float) -> list[float]:
    output = []
    for num in numbers:
        if num < limit:
            output.append(num)
    return output
