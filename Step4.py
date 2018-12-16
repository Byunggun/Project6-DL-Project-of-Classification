
# 7. 상위 10개에 해당하는 단어를 시각화

#막대그래프 그리기
from matplotlib import pyplot as plt #matplotlib:화면에 시각화
import matplotlib
from matplotlib import font_manager, rc
import platform

#시각화 시 한글이 깨지는 문제(영어는 제대로 출력)를 해결해 줌. 아래 4문장은 늘 씀.
if platform.system()=="Windows": #현재 시스템이 윈도우 운영 체제라면,
    font_name=font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() #ttf는 윈도우에 쓰이는 '글자'들이 모여있는 파일임.
    rc('font',family=font_name) #이 문장은 늘 사용
matplotlib.rcParams['axes.unicode_minus']=False

f=open("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_output_final.txt","r")
i=1
news_word=[] #x축-단어
word_cnt=[] #y축-빈도수
while True:
    line=f.readline()
    word, count=line.split(" ") #word('날씨'가리킴)와  count(5가리킴)를 split로 공백 나누기
    news_word.append(word) #news_word에 word추가
    word_cnt.append(int(count[0])) #int(count[0]):순수하게 숫자만 나옴 #빈도수
    if i==10 : break
    i+=1
f.close()
print(news_word)
print(word_cnt)

## 여기서 부터


#그래프 꾸미기
xs=[i+0.1 for i, _ in enumerate(news_word)] #enumerate:열거형. news_word의 단어와 인덱스(위치)가 리턴되어짐. ex)날씨-0번째->i에 들어감.
plt.bar(xs,word_cnt) #bar:막대그래프 출력
plt.ylabel('등장 단어의 수') #ylabel:y축에 해당하는 값 쓰기
plt.title('2018 평창동계올림픽-스포츠 도핑 키워드')
plt.xticks([i for i, _ in enumerate(news_word)],news_word) #xticks : x축
# plt.xticks([i+0.5 for i, _ in enumerate(news_word)],news_word) #xticks : x축의 위치가0.5(i+0.5)만큼 이동
plt.show()

#cf.enumerate()와 _기호(뜻:삭제)
myName=['Kim','Park','Lee']
for i, name in enumerate(myName):
# for _, name in enumerate(myName): #i안쓰고 name에 해당하는 것만 출력
    print(i,name)
v=[name for _, name in enumerate(myName)]
print(v)
