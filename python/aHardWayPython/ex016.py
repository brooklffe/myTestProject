from sys import  argv
script, fileName = argv
print(f"We are going to erase {fileName}")
print(f"这是{script} 在与你确认 如果不想删除 按 cmd+c 结束进程")
print(f"这是{script} 在与你确认 如果想删除，按回车")
input("?") #其实只是为了中断一下。。。。
print(f"Open the file file name is {fileName}")
txtFile = open(fileName,'w')
# txtFile.seek(0)
# if(txtFile == None):
#     print(f"找不到这个文件 文件名为{fileName}")
# else:
#     print(f"Oping {fileName}")
#     txtFile.close
#     print(txtFile.read())
#  不考虑文件名错误打不开的问题，网上说需要os模块处理 待定。
# 经过测试 如果open 给w的参数 如果没有这个文件会创建，另外貌似特殊情况open w的情况文件数据会丢失
txtFile.truncate()
print("You can input 3 line")
line1 = input("line1:")
txtFile.write(line1)
txtFile.write("\n")
print("写了1行")
line2 = input("line2:")
txtFile.write(line2)
txtFile.write("\n")
print("写了1行")
line3 = input("line3:")
txtFile.write(line3)
txtFile.write("\n")
print("写了1行")
print("写完了，关闭")
txtFile.close()