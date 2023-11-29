def print_formatted(number):

    # calculate the width dynamically
    width = len("{0:b}".format(number))

    for n in range(1, number + 1):
        for base in 'doXb':
            print('{0:{width}{base}}'.format(
                n, base=base, width=width), end=" ")
        print()


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
