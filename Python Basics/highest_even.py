def highest_even(my_list):
    '''
    Print the highest even number in a list
    '''
    even = []
    for item in my_list:
        if item % 2 == 0:
            even.append(item)
    return max(even)
    
res = highest_even([10,2,3,4,5,6,40])
print(res)
