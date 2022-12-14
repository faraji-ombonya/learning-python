# use for loop to find sum of items in a list  

my_list = [1,2,3,4,5,6,7,8,9,10]

my_sum = 0
number_of_items = 0

for item in my_list:
    my_sum += item
    number_of_items += 1

print(f"Sum of items in the list = {my_sum}")
print(f'Number of items in the list = {number_of_items}')