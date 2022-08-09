import streamlit as st
import streamlit.components.v1 as components
from urllib import parse
import requests
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta
import clipboard
import pandas as pd

st.set_page_config(layout="wide",
menu_items={
        'Get Help': 'https://github.com/LAB-703',
        'Report a bug': "https://github.com/LAB-703",
        'About': '''SPDX-FileCopyrightText: © 2021 Lee Jeong Min
        SPDX-License-Identifier: BSD-3-Clause'''
    })


#page_bg_img = '''
#<style> 
#.stApp {
#  background-image: url("https://marketplace.canva.com/EAD2962NKnQ/2/0/1600w/canva-rainbow-gradient-pink-and-purple-zoom-virtual-background-_Tcjok-d9b4.jpg");
#  background-size: cover;
#}
#</style>
#'''
#
#st.markdown(page_bg_img, unsafe_allow_html=True)


#page_bg_img2 = '''
#<style>
#.stApp {
#  background-image: url("https://i.ytimg.com/vi/o9TNC1Uu7d0/mqdefault.jpg");
#  background-size: cover;
#}
#</style>
#'''

#st.markdown(page_bg_img2, unsafe_allow_html=True)
#
##타이틀/ 서브타이틀 
#st.markdown('<p align="center" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 40px;">키워드 ‘장애인’에 대한 국민권익위원회 민원 데이터 분석</p>', unsafe_allow_html=True)
#st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 30px;">제1회 국민권익위원회 민원데이터 분석 경진대회 결과보고서</p>', unsafe_allow_html=True)
#st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 30px;"></p>', unsafe_allow_html=True)
#st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">제출일 : 2021. 11. 19.</p>', unsafe_allow_html=True)
#st.markdown('<p align="right" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 30px;">팀 💪굳건히</p>', unsafe_allow_html=True)
#st.markdown('---------------------------------------------------- ')
#
##사이드바
select_event = st.sidebar.selectbox("목차", ("0️⃣ 팀 소개", "1️⃣ 추진배경", "2️⃣ 분석방법","3️⃣ 분석결과", "4️⃣ 현황 파악", "5️⃣ 정책 제언"))


################################# 팀 소개#############################################
if select_event == '0️⃣ 팀 소개':
    URL=input("")
    URL=st.text_area("url을 입력해주세요.",
                               max_chars=140,placeholder="네이버와 다음만 가능합니다.")
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
        'accept' : "*/*",
        'accept-encoding' : 'gzip, deflate, br',
        'accept-language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7'}
    req =requests.get(URL,headers=headers)
    html_doc = req.text  
    soup = bs(html_doc, 'html.parser')
    TITLE=soup.find("h2",{"class":"media_end_head_headline"}).get_text()
    DATE_retrieve=datetime.now().strftime("%Y.%m.%d")
    DATE_write=soup.find("span",{"class":"media_end_head_info_datestamp_time _ARTICLE_DATE_TIME"}).get_text()[:10]
    DATE_modify=soup.find("span",{"class":"media_end_head_info_datestamp_time _ARTICLE_MODIFY_DATE_TIME"}).get_text()[:10]
    AUTHOR=soup.find("em",{"class":"media_end_head_journalist_name"}).get_text().split()[0]
    COMPANY=soup.find("em",{"class":"media_end_linked_more_point"}).get_text()
    APA=AUTHOR+". "+"("+DATE_write+"). "+TITLE+". "+COMPANY+". "+URL
    CHICAGO=AUTHOR+', "'+TITLE+'" '+COMPANY+", "+DATE_write+", "+URL
    APA_bt=st.button('APA')
    if APA_bt==True:
        clipboard.copy(APA)
    CHICAGO_bt=st.button('CHICAGO')
    if CHICAGO_bt==True:
        clipboard.copy(CHICAGO)
        
        
        
#
#    st.markdown('<p align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 30px;">0️⃣ 팀 💪굳건히❓</p>', unsafe_allow_html=True)
#    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">장애인이 <b>굳건히</b> 자립적인 생활을 도모할 수 있도록 <b>국</b>민 <b>권</b>익 <b>위</b>원회에 지원한 팀 💪굳건히입니다.</p>', unsafe_allow_html=True)
#    st.markdown(' ')
#    st.markdown('---------------------------------------------------- ')
#    st.markdown('<p align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 30px;">팀원 소개</p>', unsafe_allow_html=True)
#    st.markdown(' ')
# 
#    # 페이지 레이아웃 3갈래
#    #팀원 소개
#    col1, col2, col3 = st.columns(3)
#    with col1:
#        st.image("박지영.jpg", width=100)
#        st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">대표자 : 박지영</p>', unsafe_allow_html=True)
#        st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">국립재활원 재활연구소 연구원</p>', unsafe_allow_html=True)
#
#    with col2:
#        st.image("증명사진_이정민.jpg", width=100)
#        st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">팀원 : 이정민</p>', unsafe_allow_html=True)
#        st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">국립재활원 재활연구소 인턴연구원</p>', unsafe_allow_html=True)
#
#    with col3:
#        st.image("https://github.com/LAB-703/LAB-703/blob/main/%EB%B0%95%EC%98%81%EB%B9%88.jpg?raw=true", width=100)
#        st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">팀원 : 박영빈</p>', unsafe_allow_html=True)
#        st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">국립재활원 재활연구소 인턴연구원</p>', unsafe_allow_html=True)
#    st.markdown('---------------------------------------------------- ')   
#    st.markdown(' ')
#    st.markdown('<p align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">※ 팀원 2명은 행정안전부와 한국지능정보사회진흥원에서 실시 중인 ‘공공빅데이터 분석 청년인재 양성사업’을 통해 국립재활원에 파견된 인턴연구원임</p>', unsafe_allow_html=True)
#  
#    
#########################################################추진배경################################################################     
#elif select_event == '1️⃣ 추진배경':
#    st.markdown('<pre align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 20px;">1️⃣ 추진배경</pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">
#<b>○ 국민권익위원회 장애인 관련 민원의 분포를 살펴보면 점차 증가하는 추세로 나타남</b> <br>
#<b>○ 장애는 내가 원해서, 나의 부모가 원해서 생기는 것이 아닌 불가항력으로 누구에게나 발생할 수 있는 것</b> <br>
#  - 장애인은 선천적 혹은 불의의 사고, 질병 등으로 일상생활, 사회생활에 상당한 제한을 가지게 됨 <br>
#<b>○ 장애인의 처우와 인식이 많이 개선되었음에도 실제 장애인들이 체감하는 불편사항은 여전히 존재</b> <br>
#  - 일상생활, 사회생활 중 신체활동의 제약, 시설·환경적 제약, 사회적 인식에 따른 제약 등으로
#    다른 사람의 도움이 필요한 경우가 많은 취약계층임 <br>
#<b>○ 소수 취약계층인 장애인의 사회적·정책적 인권 보장이 필요</b> <br>
#  - 장애인에 관한 문제는 개인이나 일부 소수 그룹에서 해결하기 어려우므로 정부에서 정책적으로 해결하기 위한
#    노력이 필요할 것으로 사료됨 <br>
#</pre>''', unsafe_allow_html=True)
#    
#    
#    
#    
###############################################분석방법#############################################################################
#elif select_event == '2️⃣ 분석방법':
#    st.markdown('<pre align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 20px;">2️⃣ 국민권익위원회 민원데이터 분석 추진방법</pre>', unsafe_allow_html=True)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 분석 과정</b></pre>', unsafe_allow_html=True)
#    st.image("분석과정.png")
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 활용 데이터 목록</b></pre>', unsafe_allow_html=True)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b><표 1> 활용 데이터 목록</b></pre>', unsafe_allow_html=True)
#    st.image("활용데이터목록.png")
#    
#    
#    
#    
#    
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">
#<b>□ 분석 방법 및 내용 </b><br>
#  ○ (활용 소프트웨어) Excel, R의 ggplot, dplyr, KoNLP 등, Python의 pandas, numpy, NLTK, KONLPy 등을
#     이용하여 데이터를 정제하고 분석 실시 <br>
#  ○ (분석 방법) <br>
#    가) ‘장애인’ 키워드에 대한 민원 빅데이터 API 추출 및 워드 클라우드 시각화 분석(in R)<br>
#    나) 워드 클라우드 결과 관련 자료 조사, 뉴스 크롤링 및 워드 클라우드 시각화 분석(in R)<br>
#    다) 국민권익위원회에서 제공받은 데이터 중 “장애인” 키워드 추출 → 총 2,622건 추출(in Excel)<br>
#    라) 추출한 데이터 중 건별로 “제목”과 “질문내용”을 한 문장(제목 + 질문내용)으로 결합(in Excel)<br>
#    마) 민원 글 내의 특수문자 제거 및 한국어 맞춤법 검사 수행(in Python)<br>
#    바) 5가지 형태소 분석기를 비교하여 분석 목적에 적합한 성능을 보인 “kkma” 분석기 사용(in Python)<br>
#    사) 총 21,043개 형태소 분석 결과 오류 검토 후 수정(in Excel)<br>
#    아) 다양한 품사 중 의미 있는 명사, 동사, 형용사만 사용 및 데이터 형태 변환(in R)<br>
#    자) n그램을 활용하여 단어 연관성 검토<br>
#    차) 텍스트 군집분석을 통해 최적의 k값 후보군(k = 3, 4, 5) 도출(in Python)<br>
#    타) 텍스트 마이닝 기법 중 하나인 토픽 모델링 기법을 활용하여 시각화(in Python)
#</pre>''', unsafe_allow_html=True) 
#    
###############################################분석결과#############################################################################    
####################################가가가가가가가가가가가가가가가가가가가가가가 ###############################   
#elif select_event == '3️⃣ 분석결과':
#    st.markdown('<pre align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 20px;">3️⃣ 국민권익위원회 민원데이터 분석 결과</pre>', unsafe_allow_html=True)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 17px;"><b>가. 민원 빅데이터 API 추출 및 키워드 “장애인” 워드 클라우드 시각화 분석 결과</b></pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">
#  ○ 점자블록 등의 이동경로 문제(ex/공중화장실, 구청 등) <br>
#  ○ 지역상품권, 수여상장 등의 종이문서에 점자 표기(ex/상품권, 임명장, 표창증서, 위촉장 등)<br>
#  ○ 생활용품(ex/음료나 의약품 등) 점자 표기 <br>
#</pre>''', unsafe_allow_html=True)  
#    ###########################################################################################################################
#    st.markdown('---------------------------------------------------- ')
#    
#    HtmlFile = open("장애인-민원 연관어 분석 정보 워드클라우드(상위 50건).html", 'r',encoding='utf-8')
#    source_code = HtmlFile.read() 
#    print(source_code)
#    components.html(source_code, height=450,  scrolling=False)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 1] 장애인-민원 연관어 분석 정보 워드클라우드(상위 50건) </b></pre>', unsafe_allow_html=True)
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">* 마우스를 올리면 value를 확인할 수 있습니다.<br> ** value의 의미는 키워드인 "장애인"과의 단어 간 연관도를 뜻합니다.<br>담당자 문의 결과, 분석 솔루션 프로그램에서 자체적으로 도출된 값이므로 정확한 공식을 파악할 수 없었습니다.</p>', unsafe_allow_html=True)
#    HtmlFile = open("점자표기-민원 연관어 분석 정보 워드클라우드(상위 3건 제외).html", 'r',encoding='utf-8')
#    source_code = HtmlFile.read() 
#    print(source_code)
#    components.html(source_code, height=750, scrolling=False)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 2] 점자표기-민원 연관어 분석 정보 워드클라우드(상위 3건 제외)</b><br>(※ 상위 3건 시각장애인, 장애인복지카드, 장애인등록증의 value가 너무 높게 나와 다른 키워드들이 보이지 않았음)</pre>', unsafe_allow_html=True)
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">* 마우스를 올리면 value를 확인할 수 있습니다.<br>** value의 의미는 키워드인 "장애인"과의 단어 간 연관도를 뜻합니다. <br>담당자 문의 결과, 분석 솔루션 프로그램에서 자체적으로 도출된 값이므로 정확한 공식을 파악할 수 없었습니다.</p>', unsafe_allow_html=True)
########################나나나나나나나나나나나나나나나나나나###############################################    
#    st.markdown('---------------------------------------------------- ')
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 17px;"><b>나. 워드 클라우드 결과 관련 자료 조사, 뉴스 크롤링 및 워드 클라우드 시각화 분석</b></pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 점자 관련 자료 조사 </b>  <br>
#  ○ 점자 표기 관련 실태조사 보고서, 점자 제공에 관한 기타 법률조항 확인
#</pre>''', unsafe_allow_html=True) 
######################################################################################################################    
#    col1, col2 = st.columns(2)
#    with col1:
#        
#        st.image("점자표기 실태조사(문화체육관광부 국립국어원).png")
#        st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 3] 2020 점자 표기 실태조사(문화체육관광부 국립국어원)</b></pre>', unsafe_allow_html=True)
#              
#    with col2:
#        
#        st.image("제 1차 점자발전기본계획(2019-2023) 문화체육관광부.png")
#        st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 4] 제1차 점자발전기본계획(2019-2023)(문화체육관광부)</b></pre>', unsafe_allow_html=True)
#############################################################################################        
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 점자 관련 뉴스 조사</b>  <br>
#  ○ 점자 관련 신문기사(2021.01.01.-2021.11.01.의 1360건 본문) 크롤링하여 점자표기에 대한 니즈 분석
#</pre>''', unsafe_allow_html=True) 
#    
#    
#    HtmlFile = open("점자뉴스(워드클라우드).html", 'r',encoding='utf-8')
#    source_code = HtmlFile.read() 
#    print(source_code)
#    components.html(source_code, height=600, scrolling=False)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 5] 점자관련 뉴스 기사에 대한 워드 클라우드 분석</b></pre>', unsafe_allow_html=True)
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">* 마우스를 올리면 빈도를 확인할 수 있습니다.</p>', unsafe_allow_html=True)
#        
#     
#    
#    HtmlFile = open("점자뉴스-상위 50개 가중치 키워드(워드클라우드).html", 'r',encoding='utf-8')
#    source_code = HtmlFile.read() 
#    print(source_code)
#    components.html(source_code, height=600, scrolling=False)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 6] 점자뉴스-상위 50개 가중치 키워드 워드클라우드</b></pre>', unsafe_allow_html=True)
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">* 마우스를 올리면 빈도를 확인할 수 있습니다.</p>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">    - 워드클라우드 전반적인 흐름으로 보아 사회 다방면에서의 점자 표기 법제화에 대한 니즈 확인 <br>
#    - 빠르게 피부로 와 닿을 수 있도록 배리어프리존 확장을 위한 다양한 시도가 필요한 것으로 판단됨
#</pre>''', unsafe_allow_html=True)
#    ####################################다다다다다다다다다다다다다다다다다다다다다다##########################    
#    st.markdown('---------------------------------------------------- ')
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 17px;"><b>다. 국민권익위원회 유사사례 정보(키워드 \'장애인\')의 n그램  시각화 분석 결과 </b></pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">
#<b>□ 텍스트마이닝을 위한 형태소 분석 및 전처리 </b><br>
#  ○ ‘빅카인즈’ 플랫폼에서 형태소 분석 시행<br>
#  ○ (제목&” “&내용)으로 제목과 내용을 한 문장으로 결합(in Excel) <br>
#  ○ “부정어 + 동사”를 결합하여 부정의미 동사 생성 <br>
#   - 기존의 “못”, “않”, “안되” 등의 부정어는 띄어쓰기, 혹은 보조동사(VXV)로 형태소 분리되어 부정의 의미를 반영하지 못함. 이 과정을 통해서 부정의 의미를 반영. <br>
#  ○ 의미가 없는 “~ 있다”, “~ 하다”, “~ 되다“, “~ 같다” 등 검토 후 삭제 <br>
#  ○ 수식의 의미를 갖는 “~ 위해”, “~ 관해”, “~ 대해” 등 삭제 <br>
#</pre>''', unsafe_allow_html=True)                                                                   
#    
#    st.image("장애인 유사사례정보 n그램 분석 시각화.png",width=800)  
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 7] 장애인-민원 유사사례정보 n그램 (n≥4)</b></pre>', unsafe_allow_html=True)
#################################라라라라라라라라라라라라라라라라라라라########################################### 
#    st.markdown('---------------------------------------------------- ')
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 17px;"><b>라. 국민권익위원회 빅데이터 분석 경진대회 데이터 중 “장애인”키워드 분석</b></pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b> □ EDA 차원에서 장애인 관련 민원 연도별 월별 분포 분석 </b>
#</pre>''', unsafe_allow_html=True)                                                                          
#    
#    HtmlFile = open("장애인 관련 민원 연도별 월별 분포.html", 'r',encoding='utf-8')
#    source_code = HtmlFile.read() 
#    print(source_code)
#    components.html(source_code, width=800, height=550, scrolling=False)  
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 8] 국민권익위원회 장애인 관련 민원 연도별 월별 분포 (날짜 미기재건 : 42건) </b></pre>', unsafe_allow_html=True)
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">* 마우스를 올리면 연도별 월별 빈도를 확인할 수 있습니다.</p>', unsafe_allow_html=True)
#    
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b> □ 텍스트마이닝을 위한 형태소 분석 및 전처리</pre>''', unsafe_allow_html=True)
#     
#    st.image("형태소분석일부.png")
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 9] 형태소 분석 결과(일부) </b></pre>', unsafe_allow_html=True)
#    
#    st.image("명,동,형용사를 건별로 한 줄에 결합(일부).PNG")
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 10] 명/동/형용사를 건별로 한 줄에 결합(일부) </b></pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">
#  ○ hanspell 이용, 특수문자 제거 및 맞춤법 검사 시행(in Python)<br>
#  ○ 5가지 형태소 분석기 중 kkma로 형태소 분석 시행 (in Python)<br>
#  ○ 명사/동사/형용사 추출 및 민원 건별 단어 결합 (in R)<br>
#  ○ 의미가 없는 “~ 있다”, “~ 하다”, “~ 되다“, “~ 같다” 등 검토 후 삭제<br>
#  ○ 수식의 의미를 갖는 “~ 위해”, “~ 관해”, “~ 대해” 등 삭제
#</pre>''', unsafe_allow_html=True)  
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b> □ 텍스트마이닝 파이계수 시각화 분석 결과 </pre>''', unsafe_allow_html=True)
#    
#    st.image("국권위민원데이터_파이계수.png")        
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 11] 국민권익위원회 장애인 민원 데이터 파이계수 </b></pre>',unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b> □ 텍스트 군집분석</b>
# ○ 주어진 문서에 대하여 각 문서에 어떤 주제들이 존재하는지를 확인하기 위한 확률적 토픽 모델 기법 중 하나인<br> LDA(Latent Dirichlet Allocation, 잠재 디리클레 할당) 활용
#   ※ 다차원 척도를 통해 유사한 토픽을 근처에 배치하기 위한 확률 분포의 유사성을 젠슨-섀넌 발산(Jensen-Shannon Divergence) 지수를 계산한 것. <br>         해당 지표는 기본적으로 각 토픽에 있는 단어 들의 확률 분포에 따른 위치를 보여줌.<br>
# ○ 불용어 추가 처리 후 재시각화를 반복하여 군집을 보다 효과적으로 분류<br>
# ○ 텍스트 군집분석을 통해 최적의 k값 후보군(k = 3, 4, 5) 도출(in Python)</pre>''', unsafe_allow_html=True)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b><표 2> 각 군집(k)별 특징</b></pre>', unsafe_allow_html=True)
#    st.image("군집비교표.png",width=900)
#    
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">  ○ 텍스트 마이닝 기법인 토픽 모델링 기법 중 LDA를 활용하여 시각화(in Python)
#</pre>''', unsafe_allow_html=True)
#    
#    HtmlFile = open("국민권익위원회 장애인 관련 민원 LDA 토픽 모델링 (k=4).html", 'r',encoding='utf-8')
#    source_code = HtmlFile.read() 
#    print(source_code)
#    components.html(source_code,width=1200, height=800, scrolling=False)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 12] LDA를 활용한 토픽 모델링 시각화 일부 (k=4의 토픽1인 경우)</b></pre>', unsafe_allow_html=True)
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">* 피씨나 모바일(크롬)으로 연결 시, 좌측 원을 누르면 빨갛게 표시됩니다.<br> ** 오른쪽 막대그래프의 파란색은 민원 데이터 전체에서의 단어 빈도, 빨간색은 클러스터 내의 문서에서의 단어 빈도를 나타냅니다.<br>*** 모바일로 확인 시, 원 쪽을 클릭한 후 막대그래프 쪽을 클릭해야 선택된 내용이 반영됩니다.</p>', unsafe_allow_html=True)
#
#
#################################################현황 파악###########################################
#elif select_event == '4️⃣ 현황 파악':
#    st.markdown('<pre align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 20px;">4️⃣ 도출된 이슈에 대한 현황 파악</pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 장애인전용주차구역 관련 현황</b>
#  ○ 대부분의 비장애인들은 주차 위반에 대해 과태료 10만원이 부과된다는 것을 알고 있지만 대수롭지 않게 생각하고 있음 </pre>''', unsafe_allow_html=True)
#    st.image("캡쳐본1.png")
#    st.markdown('<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">* 출처: "최대 과태료 2백만 원" 장애인 전용 주차구역 집중 단속 현장(KBS 교양, ‘21.04.08. 방영)</p>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">  - 기존 10 만원에서 100만원으로 과태료 인상 및 반복위반시 가중 처벌에 대한 개정안 발의<br>(장애인·노인·임산부 등의 편의증진 보장에 관한 법률 일부 개정 법률안, ‘21.03.08)  </pre>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">○ 개정된 장애인 주차가능 표지(’17.09)에 대한 인지 부족 <br>
#   - 기존 사각형 표지에서 14년만에 원형 표지로 변경됨. 표지 색상에 따라 노란색은 장애인 본인이 운전, 
#     흰색은 보호자가 운전하는 경우로 나뉨. 흰색은 장애인이 동승한 경우에 한해서 주차 가능 <br>
#   - 장애인 사용 차량이라고 하더라도 장애인 전용 주차구역에 주차할 수 없는 자동차에 대한 표시는
#     기존 사각형 모양이 그대로 유지됨  </pre>''', unsafe_allow_html=True)
#    st.image("장애인주차표지.png")
###########################################장애인##############################################    
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">   - 장애인 및 장애인 보호자의 인지부족 </pre>''', unsafe_allow_html=True)
#    col1, col2, col3 = st.columns(3)
#    with col1:
#        st.image("캡쳐본2.png")
#        st.markdown('''<pre align="center" style="font-family:나눔고딕; color:black; font-size: 15px;">표지 개정에 대해 모름<br>*(04:30) </pre>''', unsafe_allow_html=True)
#    with col2:
#        st.image("캡쳐본3.png")
#        st.markdown('''<pre align="center" style="font-family:나눔고딕; color:black; font-size: 15px;">주차불가인 표지 사용<br>**(05:59)</pre>''', unsafe_allow_html=True)
#    with col3:
#        st.image("캡쳐본4.png")
#        st.markdown('''<pre align="center" style="font-family:나눔고딕; color:black; font-size: 15px;">주차 가능한 경우를 정확히 모름<br>***(00:52)</pre>''', unsafe_allow_html=True)
##########################################비장애인#################################################   
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">   - 비장애인의 인지부족 </pre>''', unsafe_allow_html=True)
#    col1, col2 = st.columns(2)
#    with col1:
#        st.image("캡쳐본5.png")
#    with col2:
#        st.image("캡쳐본6.png")
#    st.markdown('''<pre align="center" style="font-family:나눔고딕; color:black; font-size: 15px;">   잠시 주차하는 것은 불법이 아니라고 판단<br>*(2:18)/***(06:30)</pre>''', unsafe_allow_html=True)
########################################영상 각주###############################################    
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   *'최대 과태료 2백만 원' 장애인 전용 주차구역 집중 단속 현장(KBS 교양, ‘21.04.08 방영분)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   **'나 하나쯤이야'...단속 비웃는 ′장애인 주차구역′ 위반(헬로! 대구경북, ‘19.12.18 방영분)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   ***[나경훈의 현장포착] 장애인 전용 주차구역 '단속' 그 현장은? (아침이 좋다, ‘19.11.25 방영분)</p>''', unsafe_allow_html=True)
#########################################카페글############################################3    
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">   - 장애인전용주차구역에 대한 포털사이트 사례</pre>''', unsafe_allow_html=True)
#    st.image("캡쳐본8.png")
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   *‘장애인 주차 구역 위반이요’(네이버 카페 구별맘, ‘19.11.19 게시글)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   **‘장애인 주차구역 내 불법 주정차 위반’(네이버 카페 거사모, ‘21.10.21 게시글)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   ***‘장애인주차구역 신고하시나요’(네이버 카페 장애인 행정 도우미, ‘21.09.18 게시글)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   ****‘장애인 주차구역 멀쩡한 사람이 주차하네요’(네이버 카페 텐인텐 대전세종, ‘21.11.13 게시글)</p>''', unsafe_allow_html=True)
############################################네이버 데이터랩#####################################################3
#    st.markdown('---------------------------------------------------- ')
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">  ○ 장애인 주차구역에 관한 검색량 변화<br>
#    - 2017년 개정된 장애인 주차가능 표지와 장애인 주차구역에 대한 검색량이 폭발적으로 증가(NAVER 데이터랩)
#      했으나 정확하게 인지되지 못했던 것을 알 수 있음</pre>''', unsafe_allow_html=True) 
#    
#    st.image("네이버데이터랩(장애인주차구역).png",width=800)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 13] NAVER 키워드: 장애인 주차구역 통합 검색량 (기준: 16.11.14~21.11.14) </b></pre>',unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   * 위 그래프는 해당 검색어가 검색된 횟수를 일/주/월별 각각 합산하여 조회기간 내 최다검색량을 100으로 설정하여 상대적인 변화를 나타냄</p>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 시각장애인 점자활용 관련 현황</b><br>
#  ○ 시각장애인의 보행 편의를 위한 기술 개발<br>
#    - RFID Tag가 삽입된 점자블록과 시각장애인 전용 스마트 지팡이를 활용하여 시각장애인을 위한 대중교통 시스템이 개발되었으나 상용화되지 못함<br>
#    - 시각장애인들의 니즈와 실행현장의 현황이 적용된 기술 개발 및 상용화를 위한 행정적 지원 검토 필요<br>
#  ○ 점자 표기 활성화를 위한 사례 <br>
#    - 정부: 공공시설물의 표지판, 지류(현금, 상품권, 상장 등) 등에 장애인에 대한 편의 보강 필요 <br>
#    - 최근 LG에서 실시한 음성매뉴얼, 점자스티커 부착 등에 대한 시각장애인의 호응이 높았으나, 상비약, 상품권 등 일상생활에서 확인이 필요한 많은 제품에 점자표기 필요
#</pre>''', unsafe_allow_html=True)
#    st.image("캡쳐본9.png")
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   *아무 데나 놔두는 전동킥보드…"시각장애인에겐 지뢰밭"(KBS, ‘20.11.22 방영분)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   **[기업] LG전자 가전제품에 점자 스티커...고객 접근성 높인다(YTN news, ‘21.03.04 방영분)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   ***시각장애인용 '점자' 표기 확대 방침에 식품업계 호응은?...테라·참이슬·아이시스·칠성사이다 '솔선'(소비자가 만드는 신문, 김경애 기자, ‘21.07.11)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   ****의약품 점자 표기 법제화 완료…2024년부터 약사법 개정안 시행(이투데이, 강태우 기자, ‘21.10.03)</p>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">  ○ 보도 턱, 킥보드 방치 등 개선 필요<br>
#    - 장애인 유동인구가 많거나 관련 민원이 상대적으로 많은 지역을 우선하여 보도 턱이 높거나 훼손된 경우 정비 필요<br>
#    - 층으로 구분된 보도 턱이 아닌 경사로 된 형태 제작 권장<br>
#    - 최근 10월 공유 전동킥보드 이용 활성화로 인해 거리에 무분별하게 주차된 킥보드로 인해 시각장애인들이 통행에 방해를 받고 있으며, 점자블록이 파손되는 등의 불편 야기
#</pre>''', unsafe_allow_html=True)
#    st.image("캡쳐본11.png")
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   *점자블록 위 킥보드 주차… 시각장애인엔 ‘길위의 벽’(동아일보, ‘20.11.27)</p>''', unsafe_allow_html=True)
#    
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">  ○ 시각장애인 문맹률 86%로 점자 교육시설 태부족*<br>
#    - 시각상실 92%가 후천적인 요인이며 점자 배우기는 다시 눈뜨는 일처럼 매우 어려워 배움을 포기하는 시각장애인이 많음<br>
#    - 최근 SK텔레콤에서 스마트 점자학습 시스템을 개발**
#</pre>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="center" style="font-family:나눔고딕; color:black; font-size: 15px;">스마트 점자학습 시스템’ 개념도 (자료=SK텔레콤)
#</pre>''', unsafe_allow_html=True)
#    st.image("캡쳐본10.png")
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   *시각장애인 문맹률 86%, 점자 교육시설 태부족(경남도민일보, ‘21.9.8)</p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   **SK텔레콤, ‘스마트 점자학습 시스템’ 개발(미디어 생활, ‘19.8.19)</p>''', unsafe_allow_html=True)
############################################정책 제언###############################################
#elif select_event == '5️⃣ 정책 제언':
#    st.markdown('<pre align="left" style="font-family:나눔고딕 ExtraBold; color:black; font-size: 20px;">5️⃣ 도출된 이슈에 대한 정책 제언</pre>', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 장애인전용주차구역에 대한 정책 제언</b><br>
#  <b>○ 주차 가능한 상황에 대한 정확한 정보 홍보 필요</b><br>
#    - 장애인전용주차구역에 주차가 가능한 상황에 대한 현행 정보에 대한 전국민 대상 홍보<br>
#    - 공익광고를 통해 준법 정신을 기르고, 장애인과 비장애인의 입장 차의 간극을 줄여 공감과 이해를 통한 사회적 통합 지향<br>
#    - 장애인 주차 가능 표지에 대한 비장애인의 이해도를 높여 표지를 보고 의심하거나, 신고제도를 오·남용하지 않도록 함 <br>
#  <b>○ 장애인 주차표지에 대한 오∙남용 인식 개선 필요</b> <br>
#    - 장애인과 장애인의 보호자 등에게 복지제도를 오·남용하지 않도록 인식 개선 <br>
#  <b>○ 공적 문서로 ‘장애인 주차 가능 표지’로 활용</b>할 수 있도록 하여 표지에 대한 신뢰성 확보<br>
#  <b>○ 비장애인의 장애인전용주차구역 주·정차 금지에 대한 인식 개선 필요</b><br>
#    - 장애인전용주차구역에 비장애인이 <b>1분 1초</b>라도 주·정차를 하면 안 된다는 것을 대대적인 홍보를 통하여 전국민 인식 개선</pre>''', unsafe_allow_html=True)   
#    
#    st.image("광고시안.gif")
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 18] 장애인전용주차구역에 대한 이해 증진을 위한 공익광고 예</b></pre>', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">   * 본 시안은 민원 데이터 분석 결과를 바탕으로 제작한, 장애인전용주차구역에 대한 비장애인의 인식개선을 위한 공익 광고의 예시입니다. </p>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>□ 시각장애인의 편의를 위한 정책 제언<br>
#  ○ RFID 기술을 이용한 시각장애인의 보행 편의 증진</b></pre>''', unsafe_allow_html=True)
#    
#    st.image("RFID시나리오시안.png",width=800)
#    st.markdown('<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>[그림 19] RFID 기술이 적용된 장애인 복지카드와 음향 신호기 활용 예</b></pre>', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 15px;">   * 본 시안은 민원 데이터 분석 결과를 바탕으로 제작한, 시각장애인 RFID 기술 접목 음향신호기의 예시입니다. </p>''', unsafe_allow_html=True)
#    st.markdown('''<p align="right" style="font-family:나눔고딕; color:black; font-size: 10px;">   *이미지 활용 출처: 장애인 복지카드(전주시청), 이외(픽사베이, 픽토그램)</p>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;">    - 시각장애인 음향신호기와 RFID 기술이 적용된 장애인 복지카드가 가까워지면, 시각장애인이 버튼을 찾아 누르지 않아도 음향 신호가 자동으로 활성화<br>
#      - 횡단보도 이외에도 장애인이 자주 방문하여 음향신호기가 주기적으로 울리도록 설치된 시설에서는 시각장애인이 오갈 때에만 신호가 울려 비장애인과의 소음 갈등 해결 가능<br>
#      - 또한 음향 소리를 자연의 소리나 적정 데시벨을 고려한 경고음으로 할 것을 제언함. 이로써 장애인/비장애인이 모두 만족할 정책으로 활용될 것을 기대함</pre>''', unsafe_allow_html=True)
#    st.markdown('''<pre align="left" style="font-family:나눔고딕; color:black; font-size: 15px;"><b>○ 시각장애인의 보행 편의를 위한 기술 개발 및 상용화를 위한 행정 지원 필요</b><br>
#      - RFID Tag가 삽입된 점자블록과 시각장애인 전용 스마트 지팡이를 활용하여 시각장애인을 위한 대중교통 시스템이 개발되었으나 상용화되지 못함<br>
#      - 시각장애인들의 니즈와 실행현장의 현황이 적용된 기술 개발 및 상용화를 위한 행정적 지원 검토 필요<br>
#  <b>○ 점자 표기 활성화</b>를 위한 사회구성원의 협동 유도<br>
#      - 학생을 비롯한 많은 국민들이 정부와 기업의 손이 닿지 않은 곳곳에 점자가 표기된 무장애 공간을 만들어 장애인과 비장애인이 더불어 사는 사회에 다가갈 수 있는 ESG(환경·사회·지배구조) 경영 추구 필요<br>
#  <b>○ 보도 턱 높낮이 개선 필요</b><br>
#      - 장애인 유동인구가 많거나 관련 민원이 상대적으로 많은 지역을 우선하여 보도 턱이 높거나 훼손된 경우 정비 필요<br>
#      - 층으로 구분된 보도 턱이 아닌 경사로 된 형태 제작 권장<br>
#  ○ 후천적 시각장애인의 점자 문맹률 개선을 위한 <b>점자 교육 실시</b> </pre>''', unsafe_allow_html=True)
#  
#  
#  
#  
#
#
#
#
#  
#  
#  
#  
#  
#  
#  
#  
#
#
#
#
#
#
#
#





        
#  st.image("https://mediahub.seoul.go.kr/wp-#content/uploads/2020/09/b246829e13c13baea2fb04c1a3ad02ff.jpg",width=800,channels="RGB",caption="출처 : 서울시")
       

# st.header("Button")
# if st.button("Button!!"):
#     st.write("Yes")
#     
#     
# st.header("Chart Data")
# chart_data = pd.DataFrame(np.random.randn(50, 3), columns=["a", "b", "c"])
# st.bar_chart(chart_data)


