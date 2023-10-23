if __name__ == '__main__':
    N = int(input())

    commands = []

    for i in range(N):
        commands.append(input())

    my_list = []

    for command in commands:
        arguments = command.split()

        if arguments[0] == "insert":
            my_list.insert(int(arguments[1]), int(arguments[2]))

        elif arguments[0] == "print":
            print(my_list)

        elif arguments[0] == "remove":
            my_list.remove(int(arguments[1]))

        elif arguments[0] == "append":
            my_list.append(int(arguments[1]))

        elif arguments[0] == "sort":
            my_list.sort()

        elif arguments[0] == "pop":
            my_list.pop()
        
        elif arguments[0] == "reverse":
            my_list.reverse()
