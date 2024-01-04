states = {
    'Oregon' : 'OR',
    'Florida' : 'FL',
    'California' : 'CA',
    'New York' : 'NY',
    'Michigan' : 'MI'
}
cities = {
    'CA':'San Francisco',
    'MI':'Detroit',
    'FL':'Jacksonville'
}
cities['NY'] = 'New York'
cities['OR'] = "Portland"
print("*"*20)
print("NY State has :",cities['NY'])
print("OR State has :",cities['OR'])
print("*"*20)
print("MI",states['Michigan'])
print('NY',states['New York'])
print("*"*20)
print('NY',states[cities['NY']])
print('New York',cities[states['New York']])
print("*"*20)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")
for print_dick , i in list(cities.items()):
    print(f"{print_dick}:{i}")
states_china = {
    '北京市': '京',
    '上海市' : '沪',
    '重庆市' : '渝',
    '天津市' : '津',
    '河北省' : '冀',
    '山东省' : '鲁',
    '山西省' : '晋',
    '黑龙江省' : '黑',
    '吉林省' : '吉',
    '辽宁省' : '辽',
    '内蒙古自治区' : '蒙',
    '西藏自治区' : '藏',
    '青海省' : '青',
    '四川省' : '川',
    '贵州省' : '贵',
    '云南省' : '云',
    '陕西省' : '陕',
    '江西省' : '赣',
    '浙江省' : '浙',
    '江苏省' : '苏',
    '广西壮族自治区' : '桂',
    '广东省' : '粤',
    '福建省' : '闽',
    '海南省' : '琼',
    '香港特别行政区' : '港',
    '澳门特别行政区' : '澳',
    '湖南省' : '湘',
    '湖北省' : '鄂',
    '安徽省' : '皖',
    '河南省' : '豫',
    '甘肃省' : '甘',
    '台湾省' : '台',
    '宁夏回族自治区' : '宁',
    '新疆维吾尔自治区' : '新',

}
city_china = {
    '北京市': '北京',
    '上海市' : '上海',
    '重庆市' : '重庆',
    '天津市' : '天津',
    '河北省' : '石家庄',
    '山东省' : '济南',
    '山西省' : '太原',
    '黑龙江省' : '哈尔滨',
    '吉林省' : '长春',
    '辽宁省' : '沈阳',
    '内蒙古自治区' : '呼和浩特',
    '西藏自治区' : '拉萨',
    '青海省' : '西宁',
    '四川省' : '成都',
    '贵州省' : '贵阳',
    '云南省' : '昆明',
    '陕西省' : '西安',
    '江西省' : '南昌',
    '浙江省' : '杭州',
    '江苏省' : '南京',
    '广西壮族自治区' : '南宁',
    '广东省' : '广州',
    '福建省' : '福州',
    '海南省' : '海口',
    '香港特别行政区' : '香港',
    '澳门特别行政区' : '澳门',
    '湖南省' : '长沙',
    '湖北省' : '武汉',
    '安徽省' : '合肥',
    '河南省' : '郑州',
    '甘肃省' : '兰州',
    '台湾省' : '台北',
    '宁夏回族自治区' : '银川',
    '新疆维吾尔自治区' : '乌鲁木齐',
}
city_abbrev_china = {
    '京': '北京',
    '沪' : '上海',
    '渝' : '重庆',
    '津' : '天津',
    '冀' : '石家庄',
    '鲁' : '济南',
    '晋' : '太原',
    '黑' : '哈尔滨',
    '吉' : '长春',
    '辽' : '沈阳',
    '蒙' : '呼和浩特',
    '藏' : '拉萨',
    '青' : '西宁',
    '川' : '成都',
    '贵' : '贵阳',
    '云' : '昆明',
    '陕' : '西安',
    '赣' : '南昌',
    '浙' : '杭州',
    '苏' : '南京',
    '桂' : '南宁',
    '粤' : '广州',
    '闽' : '福州',
    '琼' : '海口',
    '港' : '香港',
    '澳' : '澳门',
    '湘' : '长沙',
    '鄂' : '武汉',
    '皖' : '合肥',
    '豫' : '郑州',
    '甘' : '兰州',
    '台' : '台北',
    '宁' : '银川',
    '新' : '乌鲁木齐',
}
print('_'*20)
for abbrev ,city_china in list(city_abbrev_china.items()):#abbrev简称
    print(f"{abbrev} has the city {city_china}")
print('_'*20)
for states,abbrev in list(states_china.items()): # 从字典的list列表中取出来2个参数 省， 简称
    print(f"{states} state is abbreviated {abbrev}",end='')
    print(f"and has city{city_abbrev_china[abbrev]}")# 通过简称的参数从简称--城市 字典中查到城市。
print('_'*20)

state_temp = '鄂豫皖自治区'


def find_state (state_name):
    state = states_china.get(state_name)
    if not state:
        print(f"Sorry , no {state_name}")
    elif state:
        print(f"{state_name}is in state_china,简称 {states_china.get(state_name)} 省会城市是{city_abbrev_china.get(states_china.get(state_name))}")
    else:
        print("unknown ERROR")

find_state(state_temp)
find_state('天津市')
find_state('云南省')
print("请输入中国的xx省，系统会查询出他的简称和省会,结束请输入quit")

while True:
    input_state = input(">")
    if input_state != '退出':
        find_state(f'{input_state}')
        print("请再次输入")
    elif input_state == '退出':
        break
    else:
        print("unknown ERROR")