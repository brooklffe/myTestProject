print(""" 
      and    True and False == False
      as     with X as Y : pass # 
      
            # with open("xxx.txt") as my_file:
            #     print("测试")
            # 1、首先内置函数open（）会先返回一个File对象
            # 2、然后File对象的__enter__方法会被自动调用，File对象的__enter__方法的返回值是self，即File对象本身
            # 3、__enter__（）方法返回的对象，会被赋值给as后面定义的变量my_file中
            # 4、接着with as代码体中所有代码执行，例子中仅有的print（）语句会执行
            # 5、代码体执行结束后，File对象的__exit__方法会被自动调用，with流程结束
          
      
      
      """)