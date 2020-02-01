import os
import xmltodict
import re

from urllib.request import urlretrieve

if not os.path.isfile("data.xml"):
    os.system("scrapy crawl amz_spider -o data.xml")
with open("data.xml") as o:
        data = xmltodict.parse(o.read())
image = list(data["items"]["item"]["image"]["value"])
name = list(data["items"]["item"]["name"]["value"])
sel_img = [(image[i],name[i]) for i in range(len(image)) if len({"mdh","sampann","everest","suhana"} & set(re.findall(r"[\w']+", name[i].lower())))]

#download images to images/
for i in sel_img:
    urlretrieve(i[0],"images/"+i[1]+".jpeg")