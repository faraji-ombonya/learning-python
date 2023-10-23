# This is not the best use case, Was just itching to see what happens. LOL

if __name__ == '__main__':
    N = int(input())

    commands = []

    for i in range(N):
        commands.append(input())

    my_list = []

    def insert(arguments, my_list):
        my_list.insert(int(arguments[1]), int(arguments[2]))

    def remove(arguments, my_list):
        my_list.remove(int(arguments[1]))

    def append(arguments, my_list):
        my_list.append(int(arguments[1]))

    def sort(arguments, my_list):
        my_list.sort()
    
    def pop(arguments, my_list):
        my_list.pop()

    def reverse(arguments, my_list):
        my_list.reverse()


    my_functions = {
        "insert": insert,
        "remove": remove,
        "append": append,
        "sort": sort,
        "pop": pop,
        "reverse": reverse
    }


    for command in commands:
        arguments = command.split()
        my_functions[arguments[0]](arguments, my_list)
