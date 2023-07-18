import urllib.request as request
import json
import csv
url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(url) as response:
    data = json.load(response)
    attractionData=data["result"]["results"]

#write data into attraction.csv file
with open("attraction.csv",mode="w",newline="",encoding='utf-8') as file:
    writer = csv.writer(file)
    for spot in attractionData:
        area = spot["address"][5:8]
        imgUrl = "https" + spot["file"].split("https")[1]
        rowdata = [spot["stitle"],area,spot["longitude"],spot["latitude"],imgUrl]
        writer.writerow(rowdata)

#store data in temp list (nested list)
#[[mrtName,spot1,spot2...],[mrtName,spot1...],[mrtName,spot1...]...] 
temp=[]
for spot in attractionData:
    mrtName=spot["MRT"]
    name = spot["stitle"]
    found=False
    if mrtName != None:
        for mrt in temp:
            if(mrt[0]==mrtName):
                mrt.append(name)
                found=True
        if(found==False):
            temp.append([mrtName,name])

#write temp list into mrt.csv file
with open("mrt.csv",mode="w",newline="",encoding="utf-8") as file:
    writer =csv.writer(file)
    for mrtAttraction in temp:
        writer.writerow(mrtAttraction)