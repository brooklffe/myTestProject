from sys import argv
script, fileName = argv
txt = open(fileName)
print(f"Here is your file {fileName}")
if(txt.readable()):
    print(txt.read())
print(f"Type the filename again : ",end="")
fileNameInput = input(">")
txtInput = open(fileNameInput)
if(txtInput.readable()):
    print(txtInput.read())
