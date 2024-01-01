print("""You enter a dark room with two doors.
DO you go through door #1 or door#2?""")
door = int(input(">"))
def print_door_number(door):
    print(f"这是{door}#房间")

if door == 1:
    print_door_number(door)
    inside_door = int(input("房间1可以进入更深层的房间，打字选择进入1，或2>"))
    if inside_door == 1:
        door_num = str(door)+"# 门："+str(inside_door)
        print_door_number(door_num)
        print("恭喜，闯关成功")
    elif inside_door == 2:
        door_num = str(door)+"# 门："+str(inside_door)
        print_door_number(door_num)
        print("没有路了，闯关失败")
    else:
        print("输入错误")
elif door ==2:
    print_door_number(door)
    print("没有路了，闯关失败，给你一次机会重新输入一个数")
    input_door2 = int(input("请输入一个数字，如果恰好满足某个范围，则会有后门>"))
    if input_door2 in range(0,50):# 0 < input_door2<50
        print("恭喜，后门开放，闯关成功")
    else:
        print("机会没把握住，闯关失败")
else:
    print("输入错误，请重新运行程序，按提示输入1或2")