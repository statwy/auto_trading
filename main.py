# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
from function.crawling_for_mail  import crawling
from function.crawling_for_mail  import data_to_file, exchange_rate_to_file
from function.mail_func import mail, exchange
from function.get_memberlist import get_memberlist
import math
import datetime
import time
from function.insert import insertpremium 
from function.main_func import bollingerband, append_maxsize, premium_int
from function.buy import buy

while True :
    try :
        time.sleep(10)
        
        premium=crawling('bithumb','poloniex')
        if premium < 0.03 :
            result=buy(50000,0.1,'btc')
            print(result)
        else :
            print(result)
    except :
        print("전체 로직 에러 ")
#    if i==2000 :
#        break


# bollinger band test plot
plt.plot(upper_bound)
plt.plot(premium)
plt.plot(lower_bound)    


#함수, 나중에 다른 폴더로 뺄 계획 
##############################################################################

#def bollingerband(x,y=100,sigma=5) :
#    x=pd.DataFrame(x)
#    mva=x.rolling(window=y).mean()
#    mvstd=x.rolling(window=y).std()
#    upper_bound=mva+sigma*mvstd
#    lower_bound=mva-sigma*mvstd
#    return list(upper_bound[0]), list(lower_bound[0])
#
#
#def append_maxsize(x,y,z) :
#    if len(x)<z :
#        x.append(y)
#    else :
#        x.pop(0)
#        x.append(y) 
#    return x
#
#
#def gener_percentFlag(x,y) :
#    global percent_flag
#    percent_flag={}
#    percent_flag['Boll']=1
#    for i in range(x,y+1) :
#       a='p_%d' %i
#       percent_flag[a]=1
#
#def setup_percentFlag(x,y,z) :
#    for i in range(x,y+1) :
#        a='p_%d' %i
#        percent_flag[a]=1
#    b='p_%d' %z
#    percent_flag[b]=0
#    percent_flag['Boll']=0
#
#       
#def premium_int(x,y) : 
#    z= max(math.floor(x*100),math.floor(y*100))
#    return z 
#
#        