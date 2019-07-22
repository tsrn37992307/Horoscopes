import requests
import pymysql
import os,re,time
import datetime
from selenium import webdriver
from bs4 import BeautifulSoup

con = pymysql.connect(host = '127.0.0.1',port = 3306 , user = "root" ,passwd = "",db = "horoscopes",charset = 'utf8')
cur = con.cursor()


url = "https://www.dcard.tw/f/horoscopes?latest=true"
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
driver.find_element_by_class_name('Header_navText_1m5321').click()
Height = driver.execute_script('return document.body.scrollHeight')

#資料庫新增指令
sql = "INSERT INTO horoscopes (school,title,gender,DateTime) VALUE (%s,%s,%s,%s)"

for i in range (1,99):
    okay = 0
    page+=1
    #javascript指令，使網頁下拉至最底層
    driver.execute_script("window.scrollTo(0,"+str(Height)+(');')) # 使頁面下拉至底部
    Height+=Height
    print("下拉次數 : " , page)
    time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # 學校、標題、性別
    DateTime = soup.find_all('span',re.compile('Header__PublishedDateTime'))

    for h in range(len(DateTime)):
        print("第" ,h, "筆 :" , DateTime[h].text)
        if DateTime[h].text[:5] == "7月19日":
            okay = 1
            print("已抓完今日到20日的所有文章")
            break
    if okay == 1:
        break

soup = BeautifulSoup(driver.page_source, 'html.parser')
school = soup.find_all('span',re.compile('PostAuthor_root'))
title = soup.find_all('h3',re.compile('Title__Text-v196i6-0'))
gender = soup.find_all('div',re.compile('AnonymousAvatar'))

for i in range(len(gender)):
    #print("gender : " , gender[i])
    c = gender[i]["class"]
    if c[0]== "AnonymousAvatar_male_3mpl_6":
        newgender.append("男性")
    elif c[0] == "AnonymousAvatar_female_swqLgz":
        newgender.append("女性")
    else:
        newgender.append("卡稱")

try:
    for count in range (0,999):
        print("第" + str(number) + "筆 : ","\n學校 : " +str(school[count].text), "\n標題 : " + str(title[count].text ), "\n性別 : " + str(newgender[count]),"\n時間 : " + str(DateTime[count].text))
        data = [(school[count].text, title[count].text, newgender[count], DateTime[count].text)]
        cur.executemany(sql,data)
        con.commit()
        number+=1
except:
    print("\n抓取完成")
    con.close()



