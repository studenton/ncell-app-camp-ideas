def get_page(url):
    try:
        import urllib
        return urllib.urlopen(url).read()
    except:
        return ''
from bs4 import BeautifulSoup
# import lxml
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

source = requests.get("http://ncellappcamp.com/ideas")
soup = BeautifulSoup(source.content, "lxml")
idea_des=soup.find_all('div',{'class':'field-content'})
ideaname=soup.find_all('div',{'class':'idea-name'})
namelist=[]
des_list=[]
for item in ideaname:
    namelist.append(str(item.text).replace('\n',''))

for item in idea_des:
    des_list.append(str(item.text).replace('\n',''))
with open("ideas.csv","w") as file:
    for i in range(727):
        file.write('"'+ namelist[i]+'",'+'"'+ des_list[i]+ '"\n')