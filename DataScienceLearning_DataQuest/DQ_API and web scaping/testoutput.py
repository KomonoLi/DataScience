#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding('utf-8') 


import csv

def run():  
    
    data = u'我的'
    print(data)
    #print(data.encode())
    print(type(data))
    
    a = data.encode('utf-8')
    print(a)
    print(type(a))

    '''
    #data = data.encode('gbk')
    #r = data.json()
    b = a.decode()
    
    print(b)
    '''


    with open('mycsvfile.csv', 'wb') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerow(data)
        wr.writerow('\n')
        wr.writerow(data)

        # -*- coding: utf-8 -*- 
 
  
  
if __name__ == "__main__":  
    run() 
    