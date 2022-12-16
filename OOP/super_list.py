class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList()

print(len(super_list1))

# super_list1.append(5)
# super_list1.append(70)
# print(super_list1)
# super_list1.pop()
# print(super_list1)
# super_list1.clear()
# print(super_list1)