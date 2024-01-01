print("这是一个猫狗比数量大小的游戏，请按提示输入")
cat_num = int(input("请输入猫的数量"))
dog_num = int(input("请输入狗的数量"))
people_num = int(input("请输入人的数量"))

def compare_a_b(name_a,num_a,name_b,num_b):
    if num_a > num_b:
        print(f"{name_a}的数量比{name_b}的数量多")
    if num_a < num_b:
        print(f"{name_a}的数量比{name_b}的数量少")
    if num_a == num_b:
        print(f"{name_a}的数量和{name_b}的数量相同")

compare_a_b('cat',cat_num,'dog',dog_num)
compare_a_b('cat',cat_num,'people',people_num)
compare_a_b('dog',dog_num,'people',people_num)

dog_num += 10
print("狗的数量增加了10")
compare_a_b('cat',cat_num,'dog',dog_num)
compare_a_b('cat',cat_num,'people',people_num)
compare_a_b('dog',dog_num,'people',people_num)
