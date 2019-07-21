import requests,re
from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f/horoscopes?latest=true"
res = requests.get(url)
soup = BeautifulSoup(res.text,'html.parser')
number = 1
newgender = [ ]
#學校、標題、性別

school = soup.find_all('span',re.compile('PostAuthor_root'))
#print(school)
title = soup.find_all('h3',re.compile('Title__Text-v196i6-0'))
#print(title)
gender = soup.find_all('div',re.compile('AnonymousAvatar'))
#print(gender)
'''
c = gender[0]["class"]
print("lp : " , c[0])
if c[0] == "AnonymousAvatar_female_swqLgz":
    print("hello")
else:
    print(",omffgrglok")
'''
#判別男性女性
print(len(gender))

for i in range(len(gender)):
    print("gender : " , gender[i])
    c = gender[i]["class"]
    if c[0]== "AnonymousAvatar_male_3mpl_6":
        newgender.append("男性")
    elif c[0] == "AnonymousAvatar_female_swqLgz":
        newgender.append("女性")
    else:
        newgender.append("卡稱")

try:
    for count in range (0,30):
        print("第" + str(number) + "筆 : ","\n學校 : " +str(school[count].text), "\n標題 : " + str(title[count].text ), "\n性別 : " + str(newgender[count]))
        #print("第 "+number+"筆 \n" ,"學校 : " + school[count] , "標題 : " + title[count] , "性別 : " + gender[count] )
        number+=1
except:
    print("\n抓取完成")
    

