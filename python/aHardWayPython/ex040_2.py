class Parrot:
    #类属性
    species = "bird"
    # 属性
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def sing (self,song):
        return f"{self.name} sings {song}"
    def dance (self):
        return f"{self.name}is dancing"    
blu = Parrot ("麻雀",10)
woo = Parrot("鹦鹉",15)
# 访问类属性
print(f"麻雀是{blu.__class__.species}")
print(f"鹦鹉是{woo.__class__.species}")
# 访问示例属性
print(f"The {blu.name} 's  age is {blu.age}")
print(f"The {woo.name}'s age is {woo.age}") 
#调用sing 和dance
print(blu.sing("麻雀唱歌吱吱吱叽叽喳"))
print(blu.dance())
