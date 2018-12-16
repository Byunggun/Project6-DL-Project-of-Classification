##################################################word2vec##############################################################

import codecs
from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec
# #utf-16인코딩으로 파일을 열고 출력
fp=open("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_output_final.txt","r")
soup=BeautifulSoup(fp,'html.parser') #fp를 parser를 이용해서 형태소 분석
# print(soup)
# # body=soup.select_one("body > text")
# # print(body)
text=soup.getText() #getText(): 순수하게 텍스트(한글,한자,영어,숫자,등등)만 추출, 태그x
# print(text)

# #형태소 분석
results=[]
twitter=Twitter()
lines=text.split("\r\n")
print(lines)
for line in lines:
    malist=twitter.pos(line, norm=True, stem=True)    ##norm은 현대적인말 그래욬ㅋㅋㅋ 같은 것을 그래요로 바꾸어 주는 것이다.#stem은 그래요를 그렇다처럼 원형으로 바꾸어 주는 것이다.
    # print(malist)
    res=[]
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation", "Foreign"]:#함수 중요 #Q)해석?
            res.append(word[0])
            # print(word)
    r1=(" ".join(res))
    results.append(r1)
    # print(r1)
# #
# # ###################################
# # #지금부터 워드->벡터화=워드 임베딩
# # ###################################
toji_file='D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_cleaned.txt'
with open(toji_file,"w",encoding="utf-8")as fp: #fp=toji.data
    fp.write("\n".join(results))

#아래 문장에서 toji_file의 모든 내용을 읽어서 data에 저장
#전역변수에 from gensim.models import word2 기술 후 word2vec.LineSentence(해당파일)
data=word2vec.LineSentence(toji_file)
# print(data) #=><gensim.models.word2vec.LineSentence object at 0x0000025FCFFB5908>
model=word2vec.Word2Vec(data,size=200,window=10,min_count=5,iter=10,sg=1)
# #대/소문자 조심. Word2Vec:클래스임. ():계산하고자 하는 워드 삽입.
# #size:벡터의 차원, 즉 200차원의 벡터 공간에 워드를 표현. cf.데이터 량이 많아 차원에서 벗어나는 데이터는 버려지게 된다.
# #window는 앞뒤로 참조하는 단어 갯수(갯수가 많을 수록 단어 의미가 명확해지나 속도 느려짐).
# #min_count:최소 30번 이상 등장한 단어들에 대해서만 임베딩.
# #iter:반복하라
# #sg:CBOW(sg=0) 아니면 SKip=Gram(sg=1)중 택일.(나중에 더 학습 예정)

#모델 저장하기
model.save("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_word2vec.txt")
# print("#모델이 만들어 졌습니다") #모들만들어 졌으니 이 위는 주석처리해도 모델불러오기를 실행할 수 있음.

#모델 불러오기
model=word2vec.Word2Vec.load("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_word2vec.txt")
# print(model.most_similar(positive=["집"])) #most_similar():가장 닯은 것 찾기 1)긍정-의미가 가장 가까운 것 2)부정-반대
# print(model.most_similar(negative=["땅"])) #most_similar():가장 닯은 것 찾기 1)긍정-의미가 가장 가까운 것 2)부정-반대
print(model.most_similar(positive=["형량","주사"])) #most_similar():가장 닯은 것 찾기 1)긍정-의미가 가장 가까운 것 2)부정-반대