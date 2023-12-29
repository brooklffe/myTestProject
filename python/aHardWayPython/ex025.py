#无法import 数字0开头的文件？ python不允许数字开头的文件
def break_words(stuff):
    """ This function will break up words for us."""
    words = stuff.split(' ')#''拆分
    return words

def sort_words(words):
    """Sorts the words."""
    return sorted(words)#排序

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)# 列表0
    print(word)

def print_last_word(words):
    """Prints the last word after poping it off"""
    word = words.pop(-1)#列表最后一个
    print(word)

def sort_sentence(sentence):
    """Take in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one"""
    sort_words= sort_sentence(sentence)
    print_first_word(sort_words)
    print_last_word(sort_words)