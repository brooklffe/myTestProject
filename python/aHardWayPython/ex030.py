people = 33
cars = 30
trucks = 15

def compare_people_and_cars(people,cars):
    if people > cars:
        print("We should not take the cars.")
        return people
    elif people < cars:
        print("We should take the cars.")
        return cars
    else:
        print("We can't  decide.")
        return 0

def compare_trucks_and_cars(trucks,cars):
    if trucks > cars:
        print("That's too many trucks.")
        return trucks
    elif trucks < cars:
        print("Maybe we could take the trucks.")
        return cars
    else:
        print("We still can't decide.")
        return 0
def compare_people_and_trucks(people,trucks):
    if people > trucks:
        print("Alright ,let's just take the trucks.")
        return people
    else:
        print("Fine,let's stay home then")
        return 0

# compare_people_and_cars = compare_people_and_cars(people,cars) # 谁大返回谁， 相等返回1
# if compare_people_and_cars == people:
#     print("people > cars 下面比较cars 和trucks 谁大") #谁大返回谁， 小于等于返回0
#     if compare_trucks_and_cars(trucks,cars) == cars:
#         print("cars>trucks , so people>cars>trucks")
#     elif compare_trucks_and_cars(trucks,cars) == trucks:
#         print("cars<trucks ,so need compare ")
        
# elif compare_people_and_cars == cars: 
#     print("cars>people,下面比较people和trucks 谁大")
   
# else:
#     print("people = car")
    

compare_people_and_cars = int(compare_people_and_cars(people,cars))
compare_people_and_trucks = int(compare_people_and_trucks(people,trucks))
compare_trucks_and_cars = int(compare_trucks_and_cars(trucks,cars))

if compare_people_and_cars == people and compare_trucks_and_cars == cars:
    print("people > cars > trucks")
elif compare_people_and_cars == people and compare_trucks_and_cars == trucks and compare_people_and_trucks == people:
    print("people > cars > trucks")
elif compare_people_and_cars == people and compare_trucks_and_cars == trucks and compare_people_and_trucks == trucks:
    print("trucks>people>cars")
elif compare_people_and_cars == cars and compare_people_and_trucks == people:
    print("cars > people > trucks")
elif compare_people_and_cars == cars and compare_people_and_trucks == trucks and compare_trucks_and_cars == trucks:
    print("trucks > cars > people" )
elif compare_people_and_cars == cars and compare_people_and_trucks == trucks and compare_trucks_and_cars == cars:
    print("cars > trucks > people" )
# 暂时没有考虑相等的情况