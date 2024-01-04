mystuff = []
mystuff.append('hello')
mystuff.append('world')
print(mystuff)
# step1 ,找 = 哪里定义了mystuff函数，然后 点 找mystuff内部支持的函数， 看到mystuff是列表，找到通用的函数 append
# step2 append 与mystuff支持的所有函数名称对比，发现有个append函数，使用这个函数
# step3 看到左括号，去调用函数，append（mystuff，‘hello’）

class Thing(object):
    def test(message):
        print(message)

a = Thing#  如果a = Thing（） 报错，a = Thing  不会报错
a.test("hello")
# 为啥没报错？需要测试一下终端输入是否报错
print("-"*20)
ten_things = "Apple Orange Crow Telephone Light Sugar" #如果有多个空格，会找到一个空格，后面的空格也被分 ['Apple', 'Orange', '', '', '', 'Crow', 'Telephone', 'Light', 'Sugar', 'Boy'] stuff[0]
stuff = ten_things.split(' ')#需要用空格分，如果没写空格，拆分不出来字段
more_stuff =["Day","Night","Song","Frisbee","Corn","Banana","Girl","Boy"]
while len(stuff) !=10:
    next_one = more_stuff.pop()
    print("Adding:",next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} item now")
print("There we go: do something with stuff")
print(stuff[0])# get list index 0
print(f"{stuff} stuff[0]")
print(stuff[1])# get list index1
print(stuff)
print(stuff[-1])# get list pop()
print(stuff)
print(stuff.pop)#<built-in method pop of list object at 0x1005d43c0>
print(f"{stuff} stuff.pop")
print(stuff.pop())
print(f"{stuff} stuff.pop()")

print(' '.join(stuff))
print(stuff)
print('#'.join(stuff[3:5]))# 3-4 not include 5
