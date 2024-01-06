# Alien   
# Player  玩家
# Gothon  哥顿人
# Maze 迷宫
# Room
# Scene 场景
# Ship 飞船
# Escape_Pod 救生舱
# Planet 行星
# Map  进入一个场景，进入下一个场景
# Engine  play


#——————————
# 场景：
# Death 玩家死去
# Central_Corridor  游戏起点，遇到哥顿人，需要讲笑话
# Laser_Weapon_Armory 需要猜对房间密码组合，找到炸弹
# The_Bridge  埋炸弹
# Escape_Pod  英雄逃离， 需要猜测哪个救生舱
from sys import exit
from random import randint
from textwrap import dedent #去掉“”“ 开头的空白

class Scene(object):
    
    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter()")
        exit(1)

class Engine(object):
    def __init__(self,scene_map):
        self.scene_map = scene_map
        
    def play(self):
        current_scene = self.scene_map.opening_scene() # map.opening_scene（） 需要在map 中定义 
        last_scene = self.scene_map.next_scene('finished') # map.next_scene() 需要在map中定义

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
            
        current_scene.enter()

class Death(Scene):
    quips = [
        "你死了，死亡情况1",
        "你死了，死亡情况2",
        "你死了，死亡情况3",
        "你死了，死亡情况4",
        "你死了，死亡情况5",
        "你死了，死亡情况6",        
    ]
    def enter(self):
        print(Death.quips[randint(0,len(self.quips)-1)])
        exit(1)
class Central_Corridor(Scene):
    def enter(self):#dedent（处理格式问题）
        print(dedent("""
             来自25号星球的哥顿人入侵了你的飞船，你是最后一个幸存者。你的任务是去“Laser_Weapon_Armory”武器库拿到炸弹
             把炸弹放在bridge，然后在逃生仓找到最后的逃生设备。
             你正在从中央大厅去武器库逃跑的路上，一个面目可憎的哥顿人出现了，他挡住了门，拿着枪正对着你
        """))
        action = input(">")

        if action == "shoot!":
            print(dedent("""
             跟哥顿人各种pk，
             哥顿人没事，
             然后你挂了，
             哥顿人吃了你。。。。
            """))
            return 'death'
        
        elif action == "dodge!":
            print(dedent("""
             跟哥顿人各种pk，
             哥顿人没事，一枪爆了你的头。。。
             然后你挂了，
             哥顿人吃了你。。。。
            """))
            return 'death'
        
        elif action =="tell a joke":
            print(dedent("""
             跟哥顿人各种pk，
             你给哥顿人讲了一个笑话，哥顿人笑的走不动了，你干掉了他们。。。
             然后你找到了通往武器房间的大门
            """))
            return 'laser_weapon_armory'
        else:
            print("没有奏效，写点靠谱的。 可以写‘shoot！’ 或 ‘dodge！’ 或 tell a joke")
            return 'central_corridor'

class Laser_Weapon_Armory(Scene):
    def enter(self):
        print(dedent("""
             你来到了武器库，这里有更多的哥顿人
             这里死一般的寂静，你跑到了远处寻找炸弹
             这里有一个键盘锁，你需要输入密码，如果10次机会没能打开，锁就会关闭，你就无法取得炸弹。
             提示：密码3是位数
             """))
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        print(f"{code}")
        guess = input("[keypad]>")
        guesses = 0
        while guess!= code and guesses <10:
            print("错误")
            guesses += 1
            guess = input("[keypad]>")
        if guess == code:
            print("密码正确，取得了炸弹，现在你得返回bridge  将炸弹安装好")
            return 'the_bridge'
        else:
            print("10次都没有猜对密码， 你挂了。。。。")
            return 'death'
      
class The_Bridge(Scene):
    def enter(self):
        print(dedent("""
             你返回了廊桥，然后发现了哥顿人，你可以扔了炸弹 throw the boom 或者 slow place the bomb
             你看看你要干啥：
             请输入
            """))
        action = input(">")
        if action == "throw the boom":
            print(dedent("""
              你扔出了炸弹，哥顿人没事，但是你挂了。。。
              啊啊啊啊
              啊啊啊哦啊
            """))
            return 'death'
        elif action == "slow place the bomb":
            print(dedent("""
              你埋了炸弹。。。
              然后悄咪的撤退了
              下一个目标就是去逃生仓
            """))
            return 'escape_pod'
        else:
            print("没搞对，重新输入你要干嘛 你懂的 你需要 后者 你可以扔了炸弹 throw the boom 或者 slow place place the boom")    
            return'the_bridge'
    
     

class Escape_Pod(Scene):
    def enter(self):
        print(dedent("""
              你来到了逃生仓。
              但是5个里面只有1个好的
              选一个，，，看看能不能不挂。。。。
               """))
        good_pod = randint(1,5)
        print(good_pod)
        guess = input("选几号？>")
        if int(guess) != good_pod:
            print("选错了 挂了。。。")
            return 'death'
        else:
            print("选对了，你要逃出生天 ....")
            return'finished'

class Finished(Scene):
    def enter(self):
        print("you win good job")
        return 'finished'

class Map(object):
    scenes ={
        'central_corridor': Central_Corridor(),
        'laser_weapon_armory':Laser_Weapon_Armory(),
        'the_bridge':The_Bridge(),
        'escape_pod':Escape_Pod(),
        'death':Death(),
        'finished':Finished(),
    }

    def __init__(self,start_scene):
        self.start_scene = start_scene 
    def next_scene(self,scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
print(a_map)
a_game = Engine(a_map)
print(a_game)
a_game.play()