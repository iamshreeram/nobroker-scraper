import time
import requests
import json
import csv
import copy

'''
Downloading via rest api of nobroker
'''

searchparam="W3sibGF0IjoxMy4wMDY2NjI1LCJsb24iOjgwLjIyMDYzNjksInBsYWNlSWQiOiJDaElKZlFxa21uQm5Vam9SVUNkUl9KV0dOTW8iLCJwbGFjZU5hbWUiOiJHdWluZHkiLCJzaG93TWFwIjpmYWxzZX0seyJsYXQiOjEyLjk2MDk1NywibG9uIjo4MC4yNTYxODcsInBsYWNlSWQiOiJDaElKS1cwc3dUMWRVam9ScFpzVEZ3QVNfenciLCJwbGFjZU5hbWUiOiJQYWxhdmFra2FtIiwic2hvd01hcCI6ZmFsc2V9LHsibGF0IjoxMi45NjgyMTI2LCJsb24iOjgwLjI1OTk0MjcsInBsYWNlSWQiOiJDaElKdjRFSU5UOWRVam9SazN5VG1HSDFRdjAiLCJwbGFjZU5hbWUiOiJLb3R0aXZha2thbSIsInNob3dNYXAiOmZhbHNlfV0="
TOTALPAGESTOSCRAPE=800

payload={}
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'nbSource=www.google.com; nbMedium=organic; nbCampaign=https%3A%2F%2Fwww.google.com%2F; __zlcmid=DUMMYzLCMID; nbDevice=desktop; mbTrackID=DUMMYmbTRACKID; nbcit=DUMMYNBCIT; dummy=foo; JSESSION=DUMMYSESSIONID; headerFalse=false; isMobile=false; deviceType=web; js_enabled=true; nbpt=RENT; nbcr=chennai',
    'If-None-Match': 'W/"1a14af43277c795b7732658dc31d60a6d"',
    'Connection': 'keep-alive',
    'Accept-Encoding': 'gzip, deflate, br',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'
}

csv_file = "chennai-new.csv"

def getdata(pageno):
    url = "https://www.nobroker.in/api/v3/multi/property/RENT/filter?pageNo=" + str(pageno) + "&searchParam=" + str(searchparam) +"&sharedAccomodation=0&orderBy=nbRank,desc&radius=2&traffic=true&travelTime=30&propertyType=rent&rent=13000,18000&buildingType=AP,IH&city=chennai"
    response = requests.request("GET", url, headers=headers, data=payload)
    resp = json.loads(response.text)
    return resp


for pageno in range(1,TOTALPAGESTOSCRAPE):
    pgno=pageno+1
    resp = getdata(pgno)
    datains = resp['data']
    print("Entering pages of :", pageno)
    json_object = json.dumps(datains)
    if datains != []:
        with open(csv_file, 'a') as csvfile:
            csvfile.write(str(json_object) + '\n')
    else:
        print("datains is null")
        break
    time.sleep(1) # adding sleep to avoid rate-limitation from server 

