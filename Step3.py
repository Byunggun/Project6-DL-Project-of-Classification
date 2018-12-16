# 5. 정제된 파일을 읽어서 형태소 분석->명사 추출->빈도수
# 6. 명사로 구성된 단어별 빈도수를 텍스트 파일로 저장(output_final.text)

# # #########빈도수, 상위 몇 개 출력 연습
# from konlpy.tag import Twitter
# from collections import Counter # (대문자)Counter:갯수세기
#
# colors=['r','b','r','g','b','b']
# num=[1,2,3,3,3,4,4,4,4,4,5]
# cnt=Counter(colors)
# # print(cnt) #=>Counter({'b': 3, 'r': 2, 'g': 1})
# # Counter는 "리스트, 튜플"에 저장된 데이터를 "딕셔너리" 형태로 각각의 데이터가 등장한 "횟수"를 출력.
# n=Counter(num)
# # print(n.most_common()) #=>[(4, 5), (3, 3), (1, 1), (2, 1), (5, 1)] #most_common() : (빈도수 별)내림차순 정렬
# # print(n.most_common(3)) #상위 3개를 출력

# ############day8-2와 연결
from konlpy.tag import Twitter
from collections import Counter

#get_tags():명사를 추출하는 함수
#text->gtext, noun_count->nrags에 연결시킴
#ntags=30 : 디폴드값(특정한 값이 설정되지 않음)이 30임
def get_tags(gtext,ntags=30):
    twitter=Twitter()
    NOUNS=twitter.nouns(gtext) #gtext에서 nouns()명사만 추출
    # print(NOUNS)
    count=Counter(NOUNS)
    # print(count) #=>Counter({'날씨': 5, ...})
    # print(count.most_common(ntags)) #튜플()로 추출. #=>[('날씨', 5),...]
    return_list=[]
    for word, cnt in count.most_common(ntags): #count.most_common(ntags) : 상위 30(ntags)개 추출
        temp={'key':word,'value':cnt}
        # print(temp)
        return_list.append(temp)
    return return_list #get함수로 go


def main():
    text_file_name="D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_cleaned.txt"
    noun_count=30 #noun_count->nrags
    output_file_name="D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_output_final.txt"
    open_text_file=open(text_file_name,"r")
    text=open_text_file.read() #text->gtext
    res=get_tags(text,noun_count)
    open_text_file.close()

    open_output_file=open(output_file_name,"w")
    for data in res :
        nouns=data['key']
        count=data['value']
        open_output_file.write("{} {}\n".format(nouns, count)) #"{} {}\n"이 문자열에 대해 (nouns,count)로 형식(format)을 만들라. 즉 nouns->첫번째{}, count->두번째{}에 넣는다

if __name__=="__main__":
    main()




