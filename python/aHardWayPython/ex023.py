import sys
script, encoding, error = sys.argv
def main(language_file, encoding,errors):
    line = language_file.readline()
    if line:#如果line不是最后一个字符，则line永远是true
        print_line(line,encoding,error)
        return main(language_file, encoding, errors)#递归，读完所有行 line False
languages = open("023languages.txt",encoding = "utf-8")
def print_line(line,encoding,errors):
    next_lang = line.strip() # Python中的strip方法可以去掉字符串开头和结尾的指定字符（默认是空格字符），包括换行符。
    raw_bytes = next_lang.encode(encoding, errors = errors)
    cooked_string = raw_bytes.decode(encoding,errors = errors)# .decode bytes字节串转成string
    print(raw_bytes,"<===>", cooked_string)
main(languages,encoding,error)
#wangaiming@8c7aaaed2d64 aHardWayPython % python3.11 023.py utf-8 strict  需要终端执行
