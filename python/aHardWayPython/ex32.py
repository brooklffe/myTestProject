def print_list(list):
    # i = 0
    for number in list:
        # i = 0
        print(f"{number}")
#         i = i+1
# list_number = [1,2,3,4,5,6]
# print_list(2,list_number)
the_count = [1,2,3,4,5]
fruits = ['apples','oranges','pears','apricots','banana']
change = [1,'pennies',2,'dimes',3,'quarters']
for number in the_count:
    print(f"This is count {number}")
for fruit in fruits:
    print(f"{fruit}")
print_list(the_count)
print_list(fruits)
print_list(change)
for i in change:
    print(f"I got {i}")
elements = []
print_list(elements)
for i in range(0,100,5):# 开始 结束 步长
    print(f"Adding {i} to the list")
    elements.append(i)
print_list(elements)
elements.append(fruits)
print_list(elements)