#정제된 파일(doping1_cleaned.txt)->word2vec사용하기. {작업 중}

from bs4 import BeautifulSoup
from konlpy.tag import Twitter
from gensim.models import word2vec

fp=open("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_cleaned.txt","r",encoding="utf-8")

#형태소 분석
results=[]
twitter=Twitter()
for line in fp: #{오류}
    malist=twitter.pos(line, norm=True, stem=True)    ##norm은 현대적인말 그래욬ㅋㅋㅋ 같은 것을 그래요로 바꾸어 주는 것이다.#stem은 그래요를 그렇다처럼 원형으로 바꾸어 주는 것이다.
    print("*malist*",malist)
    res=[]
    for word in malist:
        if not word[1] in ["Josa", "Eomi", "Punctuation", "Foreign"]:#함수 중요 #Q)해석?
            res.append(word[0])
            print("*word*",word)
    r1=(" ".join(res))
    results.append(r1)
    print("*r1*",r1)

fp_word2vec='doping1_text_for word2vec'
with open(fp_word2vec,"w",encoding="utf-8")as fp: #fp=toji.data
    fp.write("\n".join(results))

data=word2vec.LineSentence(fp_word2vec)
model=word2vec.Word2Vec(data,size=200,window=10,min_count=5,iter=10,sg=1)
model.save("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_model_word2vec.txt")

model=word2vec.Word2Vec.load("D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_model_word2vec.txt")
print(model.most_similar(positive=["형량"])) #most_similar():가장 닯은 것 찾기 1)긍정-의미가 가장 가까운 것 2)부정-반대
