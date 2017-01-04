#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import weibo  
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8') 

#import json

APP_KEY = '295408420'  
APP_SECRET = 'e6f6f5627fe416cef8ec220809f407ae'  
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'  
  
  
def run():  
    
    client = weibo.APIClient(APP_KEY, APP_SECRET, CALL_BACK)   
    auth_url = client.get_authorize_url()  
      
    print "auth_url : \n" + auth_url  
      
    code = raw_input("input the retured code : ")  
      
    r = client.request_access_token(code)  
    client.set_access_token(r.access_token, r.expires_in) 

    data = client.statuses.home_timeline.get(count=100)
    print data


    alldata = []
    for item in data['statuses']:
        alldata.append(item['text'].decode())
        #alldata.append('\n')

    with open('mycsvfile1001.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        for num in alldata:
            wr.writerow([num])
        

    
    
if __name__ == "__main__":  
    run() 
    




