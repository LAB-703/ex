import streamlit as st
import streamlit.components.v1 as components
from urllib import parse
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import pandas as pd

#import sys
#from imp import reload 
import numpy as np
import urllib.request
from urllib import parse
import requests
from fake_useragent import UserAgent
useragent = UserAgent()
from bs4 import BeautifulSoup as bs
import json
import pandas as pd
import warnings
warnings.filterwarnings(action='ignore')
from collections import OrderedDict


import pprint
#코드 실행 시간 측정 
import time
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta #달 계산에 필요

KEYWORD="탈원전" #df_keyword['통합'][1] # 검색할 키워드
START=datetime(2017,5,10)    #최초 시작달 1일
END=datetime(2022,5,9)   #마지막달 다음달 1일

List=[]
DAY=START
while DAY<END:
    st.write(str(DAY.strftime("%Y년 %m월"))+" 기사 추출 중...")
    page=1 #새 날짜로 리셋될 때마다 초기화 필요
    #stop=1 #마지막 페이지에서 멈춰주는 용도
    URL='https://m.search.daum.net/search?w=news&DA=PGD&enc=utf8&cluster=y&cluster_page=1&q='+str(KEYWORD)+'&period=u&sd='+str(DAY.strftime("%Y%m%d%H%M%S"))+'&ed='+str((DAY+relativedelta(months=1)-timedelta(days=1)).strftime("%Y%m%d%H%M%S"))+'&p='
    headers = {'User-Agent': useragent.random,
               'cache-control': 'private, no-cache, max-age=0',
                'content-encoding': 'br',
                'content-type': 'text/html; charset=utf-8',
                'expires': '-1',
                'server': 'kws',
                'set-cookie': 'UDI=REMOVED; expires=Thu, 01-JAN-1970 00:00:00 GMT; path=/; domain=;',
                'vary': 'Accept-Encoding',
                'x-content-type-options': 'nosniff',
                'x-xss-protection': '1',
              'cookie': 'webid=f21fda8898704a169426ef1e3960e3f5; webid_ts=1646331275933; TIARA=vtA6brAO_kkt31bIhbs4gMLl8lQJPKOD-kCaWNK6ihvFmiF6kISlTa46OA2OyS9cXzlfLNJylscRiHmEWzVF4k6.DR88t2thb_buPP2TC9g0; __T_=1; DTQUERY=%ED%83%88%EC%9B%90%EC%A0%84; ODT=NNSZ_1DVZ_TWAZ_VO2Z_DICZ_BRCZ_LB2Z_; DDT=KASZ_IIMZ_BR1Z_CCBZ_WSAZ_IVRZ_GG1Z_SNPZ_MS2Z_; _T_ANO=Tv18U7/keVKRvP0vcqIPrrXWE1kBzenQ0853du3L+gGrsA5rowbhuw+0Uimbx32xzwNLbXDkovwHaA8Ytc0YdFo8z8lYDC8dA4/kKNpC2m28B4ZG/ptRQ/gHE9oxHr7kiqQmmfc670cpuDk8yp13kREBDpfnBjfspf2vzWJ1a63ij77E+VmMJx+aRndPTd6rjsYnmlNvtJSQDk4Q+AHJg0DucbL95OH4gl07Ic+9kjg3WkAnkwliOUCeF4a+mcEk6b18CS9Dolv4DoTsdhSY+EIob6TdCicQodaym+bIYFB4fLAhuyCsubtcNTSOrPKTR0OTR9vut1SZOrVdK0mvCg==; webid_sync=1659854717681}'
              }

    #--------------------------------일별 파싱----------------------------------------
    while True:
        #--------------------------------------
        req =requests.get(URL+str(page),headers=headers)
        html_doc = req.text  
        soup = bs(html_doc, 'html.parser')
        try:
            while True:
                for a in soup.find_all('a'):
                    if a.get('href').startswith('http://v.media.daum.net')==True:
                        List.append(a.get('href'))
                    pass
                break #while문 break
        except AttributeError as e:  #for문에 더이상 요소가 잡히지 않아서 nonetype에러 발생하는 데 escape하기 위해
            print(e)
            continue
        if page==1:
            totalcount=html_doc[html_doc.find("totalCount:")+12:html_doc.find("totalCount:")+18].split(",")[0]
            lastpage=int(totalcount)//15+1
        elif page==lastpage:
            break
        else: 
            page+=1
        #------------------------------------------- 
    DAY=DAY+relativedelta(months=1)
    time.sleep(1)
    
df=pd.DataFrame(List,columns=["URL"]) 

def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
    return df.to_csv().encode('utf-8')

csv = convert_df(my_large_df)

st.download_button(
     label="Download data as CSV",
     data=csv,
     file_name='large_df.csv',
     mime='text/csv',
 )