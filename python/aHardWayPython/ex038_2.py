list_poker = []
list_color = ['♠️','♥️','♣️','♦️']
list_joker = ['BIG_JOKER','joker']
list_number = ['1','2','3','4','5','6','7','8','9','10','jack','Queen','King']
def poker_create (list_color,list_number,list_joker):
    list_poker = []
    len_list_color =len(list_color)
    len_list_number = len(list_number)
    for i in range(len_list_color):
        for j in range(len_list_number):
            list_poker.append(f'{list_color[i]+list_number[j]}')
            j = j+1
        i = i +1
    len_list_joker = len(list_joker)
    for k in range(len_list_joker):
        list_poker.append(f'{list_joker[k]}')
    return list_poker
list_poker_normal = poker_create(list_color,list_number,list_joker)
print(list_poker_normal)
print(len(list_poker_normal))
poker_chinese=[]
color_chinese = ['黑','红','梅','方']
number_chinese = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
joker_chinese = ['大王','小王']
poker_chinese = poker_create(color_chinese,number_chinese,joker_chinese) 
print(poker_chinese)