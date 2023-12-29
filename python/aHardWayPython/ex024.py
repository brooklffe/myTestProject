print("Let's practice everything")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')
#以下原文档就没有缩进。。。
poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.

"""
print("-"*10)
print(poem)
print("----------")
five = 10 - 2 + 3 - 6 #5
print(f"This should be five:{five}")
def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
start_point = 10000
beans, jars, crates = secret_formula(start_point)# beans = 10000*500=5000000 jars = 5000000/1000=5000 crates = 5000/100 = 50
print("With a starting point of :{}".format(start_point))#10000
print(f"We'd have {beans} beans,{jars} jars,and {crates} crates.")
start_point = start_point /10 #1000
print("We can also do that this way:")
formula = secret_formula(start_point) 
print("We'd have {}beans,{}jars,and {} crate.".format(*formula))