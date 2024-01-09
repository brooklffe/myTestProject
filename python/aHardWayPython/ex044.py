class MyNewClass:
    '''这是一个文档字符串，主要是对类用法的解释，不是强制，但是推荐'''
    a = 10
    def func(self):
        print('Hello')
    pass
print(MyNewClass.__doc__)
print(MyNewClass.a)
print(MyNewClass.func) #  还没有对象，这里不会打印出hello
my_class = MyNewClass()
my_class.func()