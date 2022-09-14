import streamlit as st
import streamlit.components.v1 as components
from urllib import parse
import requests
from datetime import datetime, timedelta
import pandas as pd

#import sys
#from imp import reload 
import numpy as np
import urllib.request
from urllib import parse
import requests
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

st.sidebar.subheader("Filter Displayed Accounts")

start_d = st.sidebar.date_input(
     "Search Date")
st.sidebar.write('Search Date start :', start_d)

end_d = st.sidebar.date_input(
     "Search Date")
st.sidebar.write('Search Date end :', end_d)

def platform(p):
      p= st.sidebar.checkbox(p)
     if p==True:
          st.sidebar.write(platform)

platform(naver_news)          

accounts = [START,END]
account_selections = st.sidebar.multiselect(
    "Select Accounts to View", options=accounts, default=accounts
)
st.sidebar.subheader("Filter Displayed Tickers")

symbols =[START,END]
symbol_selections = st.sidebar.multiselect(
    "Select Ticker Symbols to View", options=symbols, default=symbols
)
st.subheader("Selected Account and Ticker Data")
