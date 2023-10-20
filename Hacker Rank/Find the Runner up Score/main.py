if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    scores = list(arr)
    scores.sort()
    max = scores[0]

    for item in scores:
        if item > max:
            prev_max = max
            max = item

    print(prev_max)
