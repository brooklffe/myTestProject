def add(a, b):
    print(f"Adding {a} + {b} = {a+b}")
    return a + b
def subtract(a, b):
    print(f"Substract {a} - {b} = {a-b}")
    return a - b
def multiply(a, b):
    print(f"Multiply {a} * {b} = {a*b}")
    return a * b
def divide(a, b):
    print(f"dividing {a}/{b} = {a/b}")
    return a / b
# add(100.20,50)
# subtract(100,3.5)
# multiply(2.5,4.5)
# divide(6,4)

# add(100,divide(10,multiply(subtract(5,4),2)))
user_inputa = input("请输入一个数字：")
a = float(user_inputa)
print(a)
user_inputb= input("请输入一个数字：")
b = float(user_inputb)
print(b)
# 直接a = float(input()) 会报错 str不能转成float

add(a,b)
subtract(a,b)
multiply(a,b)
divide(a,b)
