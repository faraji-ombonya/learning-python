def count_substring(string, sub_string):
    
    j = 0
    counter = 0
    for i in range(len(string)):

        result = string[j:].find(sub_string)

        if result > -1:
            j = result + 1 + j
            counter +=1

    return counter


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    
    count = count_substring(string, sub_string)
    print(count)