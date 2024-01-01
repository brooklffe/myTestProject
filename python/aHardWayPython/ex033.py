numbers = []
numbers2 = []
# while i <= 6:
#     print(f"现在i等于{i}")
#     numbers.append(i)
#     print(f"现在number的顶部数字是 {numbers[-1]}")
#     print(f"现在numbers列表是是{numbers}")
#     i=i+1
#     print(f"循环后i等于{i}")
def insert_to_list (number,list,step):
    list_name = type(list).__name__ # 只是list 类型的名称，并不是list的名字
    print(f"函数会插入从0到输入的数字的值{number}到列表{list_name}中")
    print(str(list))
    i = 0
    while i <= number:
        print(f"现在i等于{i}")
        list.append(i)
        print(f"现在{list_name}的顶部数字是 {list[-1]}")
        print(f"现在{list_name}列表是是{list}")
        if step == "":
            step =1 
        else:
            i=i+step
        print(f"循环后i等于{i}")

# import ex32 
# print_list(numbers) # 引入32后无函数待查  
def print_list(list):
    for number in list:
        print(f"这是函数的方式取列表数据{number}")
# print_list(numbers)
# for i in numbers:
#     print(f"这是for循环取number 列表中的额数据{i}")


insert_to_list(5,numbers)
insert_to_list(10,numbers2)

print(str(numbers))
print(numbers2)
insert_to_list(10,numbers2)