from sys import exit
def gold_room():
    print("This room is full of gold.How much do you take?")
    choice = input(">")
    how_much = int(choice,base=0)
    # if "0" in choice or "1" in choice:
    #     how_much = int(choice) # 0,1 在输入中，强转为int ，测试的时候可以试试100g
    #     # 待定可否type 判断input 的类型
    # input_value = input("请输入一个值：")   # 获取用户输入值
    
    # # 尝试将输入值转换为整数
    # try:
    #     int_value = int(input_value)       # 强制转换为整数
    #     print("输入值是整数！")              # 输出提示信息
    #     # 其他对于整数的处理...
    # except ValueError:                      # 当无法转换为整数时会跑到这里
    #     print("输入值不是整数！")            # 输出提示信息
    #     # 其他对于非整数的处理...


    # try:
    #     how_much = int(choice,base=0)
   
    # except ValueError:
    #     # dead("Man,learn to type a number") # 后面定义dead函数
    #     print("Man,learn to type a number")
    # print(ValueError)
    
    if how_much <= 50:
        print("Nice ,you're not greedy,you win!")
        exit(0) #?
    else:
        dead("you greedy bastard!") 

def bear_room():
    print("""
         There is a bear here.
         The bear has a bunch of honey.
         The fat bear is in front of another door.
         How are you going to move the bear?
         Tips:
         You can "taunt bear" and bear will out of the door,and  you can "open door",other choice you will dead.
          """)
    bear_move = False 
    while True:
        choice = input(">")
        if choice == "take honey":
            dead("The bear looks at you and ten slaps your face off.")
        elif choice == "taunt bear"and not bear_move: # 第一次进门 bear_move = Flase 的时候not Flase 是真。 taunt 嘲讽的意思
            print(""" The bear has moved from the door 
                  You can go through now.""")
            bear_move = True
        elif choice == "taunt bear" and bear_move:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_move:# step 1 taunt bear ,and bear_move =True ;step2 open_door step3 get into gole_room
            gold_room()
        else:
            print("I got no idea what that mean")
def dead(why):
    print(f"{why}")
    exit(0)

def cthulhu_room():
    print("""Here you see the great evil Cthulhu.
          He,it, whatever stares at you and you go insane.
          Do you flee for your life or eat your head
          Tips:
          print 'feel' you can start the game ,if you choice eat your head you die.""")
    choice = input(">")
    if "feel" in choice:
        start() # 开始游戏
    elif "head" in choice:
        dead("We that was tasty")
    else:
        cthulhu_room()

def start():
    print("you are in dark room")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    choice = input(">")
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        print("You stumble around the room until you starve.")
        start()
start()