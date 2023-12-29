def printTwoArgs(*args):
    arg1,arg2 = args
    print(f" arg1:{arg1}\n arg2:{arg2}\n")
def printTwoArgsAgain(arg1,arg2):
    print(f"print_two_args_again \narg1:{arg1}\narg2:{arg2}")
def printOne(arg):
    print(f"arg:{arg}")
def printNothing():
    print("null")
arg1 = input("传y一个str")
arg2 = input("再传一个str")
printTwoArgs(arg1,arg2)
printTwoArgsAgain(arg1,arg2)
printOne(arg1)
printNothing()