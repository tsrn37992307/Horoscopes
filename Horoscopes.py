import requests
import re,os,time
from bs4 import BeautifulSoup
from selenium import webdriver


url = "https://www.dcard.tw/f/horoscopes?latest=true"
#res = requests.get(url)
page = 0
number = 1
newgender = []

#取得本檔案路徑
mypath = os.getcwd()
#開啟ChromeDriver
driver =  webdriver.Chrome(mypath+'\\chromedriver')
#等待3秒
driver.implicitly_wait(3)
driver.get(url)
Height = driver.execute_script('return document.body.scrollHeight')


#網頁下拉
for i in range (1,10):
    page+=1
    #javascript指令，使網頁下拉至最底層
    driver.execute_script("window.scrollTo(0,"+str(Height)+(');')) # 使頁面下拉至底部
    Height+=Height
    print("下拉次數 : " , page)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # 學校、標題、性別
    DateTime = soup.find_all('span',re.compile('Header__PublishedDateTime'))

    #print(DateTime[i].text[:5])
    #print(i)
    #抓取直接回應視窗(至最下層)




    for h in range(len(DateTime)):
        print("第" ,h, "筆 :" , DateTime[h].text)
        if DateTime[h].text[:5] == "7月20日":
            print("已抓完今日到20日的所有文章")
            break





soup = BeautifulSoup(driver.page_source, 'html.parser')


school = soup.find_all('span', re.compile('PostAuthor_root'))
title = soup.find_all('h3', re.compile('Title__Text-v196i6-0'))
gender = soup.find_all('div', re.compile('AnonymousAvatar'))
DateTime = soup.find_all('span',re.compile('Header__PublishedDateTime'))


for i in range(len(gender)):
    c = gender[i]["class"]
    if c[0] == "AnonymousAvatar_male_3mpl_6":
        newgender.append("男性")
    elif c[0] == "AnonymousAvatar_female_swqLgz":
        newgender.append("女性")
    else:
        newgender.append("卡稱")

try:
    for count in range (0,999):
        print("第" + str(number) + "筆 : ","\n學校 : " +str(school[count].text), "\n標題 : " + str(title[count].text ),"\n性別 : " + str(newgender[count]) , "\n時間 : " +str(DateTime[count].text))
        number+=1
except:
    print("\n抓取完成")
    

