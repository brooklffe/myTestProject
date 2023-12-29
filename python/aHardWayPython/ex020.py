from sys import argv
script, inputFile = argv
def printFileAll(file):
    print(f"i'll print the all file ,file name is {file}")
    print(file.read())
def rewindFile(file):
    print("i will rewind the file seek == 0")
    file.seek(0)
def printFileSomeLine(file,lineNUm):
    print(f"i will read {file} file,i will print the {lineNUm} line")
    # file.seek(lineNUm) #不能用seek（num）直接光标来定义行，光标传的值只定一了
    file.seek(0)
    for i in range(lineNUm - 1):
        file.readline()
    print(lineNUm,file.readline())
objectFile = open(inputFile)
printFileAll(objectFile)
rewindFile(objectFile)
printFileSomeLine(objectFile,4)