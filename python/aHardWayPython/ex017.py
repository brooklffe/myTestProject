from sys import argv
from os.path import exists
script, fromFile, toFile = argv
print(f"将{fromFile}文件内容复制到{toFile}")
#首先判断文件是否存在
print(f"先看这两个文件是否都存在，\n{fromFile}这个文件{exists(fromFile)};\n{toFile}这个文件{exists(toFile)};\n")
if(exists(fromFile) ):
    objFileFromFile = open(fromFile)
    fromFileData = objFileFromFile.read()
    print(f"{fromFile}文件数据长度为 " +str(len(fromFileData)))
    objFileToFIle = open(toFile,'w')
    objFileToFIle.write(fromFileData)
    objFileFromFile.close()
    objFileToFIle.close()
    print("复制完成")