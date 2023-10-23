if __name__ == '__main__':
    N = int(input())

    commands = []

    for i in range(N):
        commands.append(input())

    my_list = []

    for command in commands:
        arguments = command.split()

        match arguments[0]:
            case "insert":
                my_list.insert(int(arguments[1]), int(arguments[2]))
            case "print":
                print(my_list)
            case "remove":
                my_list.remove(int(arguments[1]))
            case "append":
                my_list.append(int(arguments[1]))
            case "sort":
                my_list.sort()
            case "pop":
                my_list.pop()
            case "reverse":
                my_list.reverse()
                
