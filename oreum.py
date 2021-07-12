# https://github.com/paullabkorea/foliummap.git


# import는 모듈을 불러와서 프로그램에 적용 시키는 명령어
# R에서 사용하는 library()와 같은 역할
# import 옆 numpy, pandas, forium, warnings는 모듈명
# import numpy 'as np' , import pandas 'as pd'
# as np, as pd는 모듈명을 길게 쓰기 귀찮아서 줄여서 별칭 부여한것

# python의 약속
# 변수, 함수, 모듈에는 소문자만 사용, 스네이크표기법 사용
# 변수 : location, zoom_start, parking_y, parking_n, df_oreum 등
# 함수() : 함수명은 변수와 비슷한데 옆에 ()가 있음
# filterwarnigs(), add_to(), read_csv(), print(), save() 등
# 클래스는 첫문자 대문자, 다음문자들은 소문자, 카멜표기법 사용
# CustomIcon(), Map(), Marker(), LayerControl() 등 
# 첫문자 대문자 이면서 옆에 ()가 있음
# 파이썬에서 라이브러리, 패키지, 모듈에 대한 구분이 불명확함(제가 아직 이해를 다 못함ㅋ)
# 모듈은 함수와 클래스(클래스도 변수와 실행문 모음) 등의 모음이며
# 1차 파일 형태(folium.py)이나 여러파일을 하나에 폴더(folium)에 넣어
# 각각의 파일을 불러와 사용할 수 있음  -> 라이브러리 또는 패키지라 부름


import numpy as np # numpy
import pandas as pd
import folium
import warnings  
from folium.features import CustomIcon
# from 모듈명.모듈명 import 클래스명
# folilium모듈(폴더)안에 freatures 모듈(파일)안에 있는 
# CustomIcon이라는 클래스를 직접 불러오는 경우에 사용

warnings.filterwarnings(action='ignore') 
# 프로그램 실행시 나타나는 경고 무시


m = folium.Map(
    location = [33.3684955195788, 126.52918183373025],
    #tiles = 'Stamen Terrain',
    zoom_start = 10
)

# folium모듈에 있는 Map클래스 안의 변수 location과 zoom_start에 값을 각각 넣어줌
# 그리고 m 이라는 변수,,,여기서는 클래스를 넣었기 때문에 인스턴스라 부름...에 넣어줌
# 클래스나 인스턴스에 대한 개념은 아직 몰라도 됨.
# 그냥 위와 같은 형태로 인스턴스 = 모듈명.클래스명(변수들 초기값 지정) 쓰인다는 것만
# 눈으로 봐두면 됨.


parking_y = folium.FeatureGroup(name='주차장유').add_to(m)
parking_n = folium.FeatureGroup(name='주차장무').add_to(m)

# FeatureGroup이라는 클래스안의 name변수에 '주차장유'라는 값을 넣고,
# m(지도 인스턴스)에 추가                    
# 이것두 형태만 눈에 익히시면 되요.ㅋㅋ


df_oreum = pd.read_csv('o.csv', encoding='cp949')
## 중요 ## 데이터 분석하면 이 문장은 아주 많이 쓰임.
# csv파일 안의 데이터를 데이터프레임 형식으로 df_oreum 변수안에 넣어줌. 
# 한글 처리를 위해 encoding='cp949' 사용
# pd(pandas) 모듈 안에 있는 read_csv()함수를 사용
# 함수 read_csv(불러올파일명, 인코딩 형식) 으로 불러옴..

print(df_oreum)
tooltip = 'Click!!'
# 마우스 오버할때 나오는 글자


print(df_oreum.shape) # dataframe oreum 의 크기확인 (행,열)을 튜플 형식으로 보여줌

for i in range(df_oreum.shape[0]): # 데이터프레임 안에 있는 행 수만큼 반복문 실행

    icon_image = 'mountains.png'
    icon = CustomIcon(
        icon_image,
        icon_size = (20, 20),
        popup_anchor = (30, -30),
    )

    if df_oreum.iloc[i]["주차장"] == 'Y':
        folium.Marker(
            [df_oreum.iloc[i]['위도'], df_oreum.iloc[i]['경도']],
            popup = f'<div style="width:100px"><strong>{df_oreum.iloc[i]["오름명"]}</strong><br>\
            주차장 : {df_oreum.iloc[i]["주차장"]}<br>\
            화장실 : {df_oreum.iloc[i]["화장실"]}<br>\
            <img width="80px" src="a.jpg"><br>\
            <a href="https://www.visitjeju.net/kr/search?q=%EC%98%A4%EB%A6%84#">상세페이지 이동</a></div>',
            tooltip = df_oreum.iloc[i]["오름명"],
            icon= icon
        ).add_to(parking_y)
    else :
        folium.Marker(
            [df_oreum.iloc[i]['위도'], df_oreum.iloc[i]['경도']],
            popup = f'<div style="width:100px"><strong>{df_oreum.iloc[i]["오름명"]}</strong><br>\
            주차장 : {df_oreum.iloc[i]["주차장"]}<br>\
            화장실 : {df_oreum.iloc[i]["화장실"]}<br>\
            <img width="80px" src="a.jpg"><br>\
            <a href="https://www.visitjeju.net/kr/search?q=%EC%98%A4%EB%A6%84#">상세페이지 이동</a></div>',
            tooltip = df_oreum.iloc[i]["오름명"],
            icon = icon
        ).add_to(parking_n)

folium.LayerControl(collapsed=False).add_to(m)

m.save('index.html')