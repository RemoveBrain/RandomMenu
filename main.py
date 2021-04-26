import pandas as pd
import random

data = pd.read_csv("./menu.csv", names=['분류','메뉴','별정','링크'])
korean = []
chinese = []
japanese = []
flour = []
desert = []

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

menu = str(input("어떤 식사를 드시겠습니까? (ex. 한식,중식,일식,분식)\n"))

if(menu == '한식') :
    print(korean[random.randint(0,len(korean)-1)])
elif(menu == '중식') :
    print(chinese[random.randint(0,len(chinese)-1)])
elif(menu == '일식') :
    print(japanese[random.randint(0,len(japanese)-1)])
elif(menu == '분식') :
    print(flour[random.randint(0,len(flour)-1)])

print()
menu2 = str(input("후식을 드시겠습니까? (Y/N)\n"))

if(menu2 == "Y" or menu2 == "y") :
    print(desert[random.randint(0,len(desert)-1)])
