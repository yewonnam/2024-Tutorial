# -*- coding: utf-8 -*-
"""3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wiyp97lcR4eNxEXpD2StrcY51gk_8DR1
"""

# Commented out IPython magic to ensure Python compatibility.
import pandas as pd
import numpy as np
import seaborn as sns

# %matplotlib inline

# Commented out IPython magic to ensure Python compatibility.
import matplotlib.pyplot as plt
from IPython.display import set_matplotlib_formats

plt.rc('font',family='Malgun Gothic')

# %config InlineBackend.figure_format = 'retina'

# %matplotlib inline

df = pd.read_csv("C:\Users\user\Desktop\소상공인시장진흥공단_상가업소정보_의료기관_201909.csv", low_memory=False)
#타입이 섞여 있어서 로우메모리 펄스 설정을 함.
df.shape

###데이터 미리보기

df.head()
#쉬프트+탭 = 닥스트링 = 공식문서를 볼 수 잇음. 그러면서 학습가능.

df.tail()

df.info()
#오브젝트는 문자로 된 데이터 형태.

df.columns

df.dtypes

###결측치 확인

df.isnull()
#펄스면 값이 없다, 0
#트루면 값이 있다, 1

null_count = df.isnull().sum()
#결측치가 몇개인지 확인.

null_count

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline

import matplotlib as mpl  # 기본 설정
import matplotlib.pyplot as plt  # 그래프 그리기
import matplotlib.font_manager as fm  # 폰트 관리

'''
!apt-get update -qq         # apt-get 패키지 설치 명령어, -qq : 에러외 메세지 숨기기
!apt-get install fonts-nanum* -qq #나눔글꼴 설치
'''

fe = fm.FontEntry(fname=r'/usr/share/fonts/truetype/nanum/Malgun Gothic.ttf', name='Malgun Gothic') #파일 저장되어있는 경로와 이름 설정
fm.fontManager.ttflist.insert(0, fe)  # Matplotlib에 폰트 추가
plt.rcParams.update({'font.size': 10, 'font.family': 'Malgun Gothic'}) #폰트설정

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False
null_count.plot.bar(rot=60)
#rot 로테이션, 돌리기
#가로세로 바꾸기 = null_count.plot.barh(figsize=(5, 7)) = 사이즈지정

df_null_count = null_count.reset_index()
#df형태로 변환됨.
df_null_count.head()

df_null_count.columns = ['컬럼명', '결측치수']
df_null_count

#결측치 수로 정렬해서 다시보기, 내림차순=펄스
df_null_count_top = df_null_count.sort_values(by="결측치수", ascending=False).head(10)

df["지점명"].head()
#특정 컬럼만 가져오다
#NaN= not a number, 숫자가 없다, 결측치를 뜻함.

drop_columns = df_null_count_top["컬럼명"].tolist()
#리스트 형태로 바꾸다
drop_columns

df[drop_columns].head()

print(df.shape)
df= df.drop(drop_columns, axis=1)
#기본이 0, 행이 기준,, 컬럼은 1 열을 기준으로.
print(df.shape)

df.info()

### 기초통계보기(수치형데이터만 구할 수 잇음)

#평균값
df["위도"].mean()

#중앙값
df["위도"].median()

#최댓값
df["위도"].max()

#최솟값
df["위도"].min()

#갯수, 결측치를 제외하고 ~~개 잇다.
df["위도"].count()

df["위도"].describe()

#판다스에선두개이상의 데이터를 가져올때 리스트형태로 가져와야함.
df[["위도", "경도"]].describe()

df.describe()
#모든 수치형 데이터 분석이 기본.
df.describe(include="object")
#오브젝트 형태는 최대최소중앙 등 값이 없고 대신 탑=가장많이 등장한 오브젝트가 등장.
#프리퀀시, 탑의 빈도수를 뜻함.

#중복제거한 값 = 유니크값. shape 문자 요약에서 나옴.

df["상권업종대분류명"].unique()

df["상권업종대분류명"].nunique()

df["상권업종중분류명"].unique()

df["상권업종중분류명"].nunique()

df["상권업종소분류명"].unique()

df["상권업종소분류명"].nunique()

len(df["상권업종소분류명"].unique())
#nunique 대신 len도 사용가능

#카테고리형태데이터갯수세기
city = df["시도명"].value_counts()

city_normalize = df["시도명"].value_counts(normalize=True)
#각데이터가 전체에서 어느정도의 비율을 차지하는지 보여줌 = 일반화.

city.plot.barh()

city.plot.pie(figsize = (7,7))

city_normalize.plot.pie(figsize=(7,7))

#seaborn에는 파이차트가 없음.

c = sns.countplot(data=df,y="시도명")

df["상권업종대분류명"].value_counts()

c = df["상권업종중분류명"].value_counts()

n = df["상권업종중분류명"].value_counts(normalize=True)

c.plot.bar(rot=0)

n.plot.pie()

c = df["상권업종소분류명"].value_counts()

c.plot.barh(figsize=(7,8), grid=True)

###데이터 색인하기

df["상권업종중분류명"]=="약국/한약방"
#불리언으로 보여줌

df_medical = df[df["상권업종중분류명"]=="약국/한약방"].copy()
#약국 한약방인것만 df로 가져오기 . 그리고 카피해서 가져와서 바꾸기

df_medical.head()

df[df["상권업종대분류명"] == "의료"]["상권업종중분류명"]
#이건 속도느림. 두 번접근해서.

df.loc[df["상권업종대분류명"] == "의료","상권업종중분류명"].value_counts()

m = df["상권업종대분류명"]=="의료"
df.loc[m, "상권업종중분류명"].value_counts()

df_medi = df[df["상권업종중분류명"] == "유사의료업"]
df_medi.shape

df["상호명"].value_counts().head(10)

df_medi["상호명"].value_counts().head(10)

#여러조건으로 색인

#and
df_seoul_drug = df[(df["상권업종소분류명"] == "약국") & (df["시도명"] == "서울특별시")]

print(df_seoul_drug.shape)

#or = /
#and = &

c = df_seoul_drug["시군구명"].value_counts()
c.head()
#갯수

n = df_seoul_drug["시군구명"].value_counts(normalize=True)
n.head()
#비율

c.plot.bar(rot=60)

df_seoul_hospital = df[(df["상권업종소분류명"] == "종합병원") & (df["시도명"] == "서울특별시")].copy()

df_seoul_hospital["시군구명"].value_counts()

###텍스트데이터 색인하기

#~물결표시앞에 붙이면 아닌것
#종합병원이 들어가지 않은 것 중 상호명만 유니크값만 보여줘.
df_seoul_hospital.loc[~df_seoul_hospital["상호명"].str.contains("종합병원"), "상호명"].unique()

df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("꽃배달")]

df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기")]

drop_row = df_seoul_hospital[df_seoul_hospital["상호명"].str.contains("의료기|꽃배달|장례식장|상담소|어린이집")].index
drop_row = drop_row.tolist()
drop_row

#의원도
#startswith, endswith
drop_row2 = df_seoul_hospital[df_seoul_hospital["상호명"].str.endswith("의원")].index
drop_row2 = drop_row2.tolist()
drop_row2

drop_row = drop_row + drop_row2
len(drop_row)

print(df_seoul_hospital.shape)
df_seoul_hospital = df_seoul_hospital.drop(drop_row, axis=0)
print(df_seoul_hospital.shape)

df_seoul_hospital["시군구명"].value_counts().plot.bar()

plt.figure(figsize=(15,4))
sns.countplot(data=df_seoul_hospital, x="시군구명", order=df_seoul_hospital["시군구명"].value_counts().index)

###특정지역만보기

df_seoul = df[df["시도명"] == "서울특별시"].copy()
df_seoul.shape

df_seoul["시군구명"].value_counts().plot.bar(figsize=(10,4),rot=30)

plt.figure(figsize=(15,4))
sns.countplot(data=df_seoul, x="시군구명")

df_seoul[["경도","위도", "시군구명"]].plot.scatter(x="경도", y="위도", figsize=(8,7), grid=True)

plt.figure(figsize=(9, 8))
sns.scatterplot(data=df_seoul, x="경도", y="위도", hue="시군구명")
#sns에서만 hue옵션을 사용가능

plt.figure(figsize=(9, 8))
sns.scatterplot(data=df_seoul, x="경도", y="위도", hue="상권업종중분류명")

'''
1000개만 뽑아서
plt.figure(figsize=(9, 8))
sns.scatterplot(data=df[:1000] x="경도", y="위도", hue="시도명")
'''
plt.figure(figsize=(16, 12))
sns.scatterplot(data=df, x="경도", y="위도", hue="시도명")

#지도에 직접표시가 더 직관적일듯 하여 folium을 사용해볼 것


import folium

df_seoul_hospital["위도"].mean()
df_seoul_hospital["경도"].mean()

df_seoul_hospital.tail(1)

map = folium.Map(location=[df_seoul_hospital["위도"].mean(), df_seoul_hospital["경도"].mean()],zoom_start=12)
# folium

for n in df_seoul_hospital.index :
  name = df_seoul_hospital.loc[n, "상호명"]
  address = df_seoul_hospital.loc[n, "도로명주소"]
  popup = f"{name}-{address}"
  location = [df_seoul_hospital.loc[n, "위도"], df_seoul_hospital.loc[n, "경도"]]
  folium.Marker(
      location = location,
      popup = popup
  ).add_to(map)
map

