if __name__ == "__main__":

    input = str(input()).split()
    n = int(input[0])
    m = int(input[1])

    for i in range(n + 1):
        if (i % 2):
            if i == n:
                print("WELCOME".center(m, "-"))
                continue

            mid = ".|." * i
            print(mid.center(m, "-"))

    for i in range(n + 1, 0, -1):
        if (i % 2):
            if i == n:
                continue

            mid = ".|." * i
            print(mid.center(m, "-"))
