import pandas as pd
import numpy as np
import random

data = pd.read_csv("./menu.csv", names=['분류','메뉴','별점','링크'])
# data = data.dropna(axis=0,how='any',thresh=None,subset=None,inplace=False)
data = data.fillna(" ")

korean = []
chinese = []
japanese = []
flour = []
desert = []
like = ["KFC"]
dislike = ["본죽"]

for i in range(2,len(data)):
    if(data['분류'][i]== '한식') :
        korean.append(data['메뉴'][i])
    elif(data['분류'][i]== '중식') :
        chinese.append(data['메뉴'][i])
    elif(data['분류'][i]== '일식') :
        japanese.append(data['메뉴'][i])
    elif(data['분류'][i]== '분식') :
        flour.append(data['메뉴'][i])
    elif(data['분류'][i]== '후식') :
        desert.append(data['메뉴'][i])

#=내가 원하는 메뉴가 있는지 여부 체크하고 있으면 음식에 대한 정보를 출력하는 코드를 작성하세요
like = input("원하는 메뉴는 무엇인가요?")
#print(data.loc[data['메뉴'] == 'KFC'])
if (data['메뉴']==like).any():
    print(data.loc[data['메뉴'] == like])
else:
    print("원하신 메뉴가 리스트에 존재하지 않습니다.")
menu = str(input("어떤 식사를 드시겠습니까? (ex. 한식,중식,일식,분식)\n"))

if(menu == '한식') :
    a=korean[random.randint(0,len(korean)-1)]
    while 1:
        if a in dislike:
            a=korean[random.randint(0,len(korean)-1)]
        else:
            print(a)
            break
elif(menu == '중식') :
    a=chinese[random.randint(0,len(chinese)-1)]
    while 1:
        if a in dislike:
            a=chinese[random.randint(0,len(chinese)-1)]
        else:
            print(a)
            break
elif(menu == '일식') :
    a=japanese[random.randint(0,len(japanese)-1)]
    while 1:
        if a in dislike:
            a=japanese[random.randint(0,len(japanese)-1)]
        else:
            print(a)
            break
elif(menu == '분식') :
    a=flour[random.randint(0,len(flour)-1)]
    while 1:
        if a in dislike:
            a=flour[random.randint(0,len(flour)-1)]
        else:
            print(a)
            break


print()
menu2 = str(input("후식을 드시겠습니까? (Y/N)\n"))

if(menu2 == "Y" or menu2 == "y") :
    print(desert[random.randint(0,len(desert)-1)])
