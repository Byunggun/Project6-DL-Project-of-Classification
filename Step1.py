#Q)불러오기 후 각각의 파일에 저장해 수많은 파일 생성?

#<자료 수집>
#네이버 뉴스, 2018.2.9.-2.25., 키워드: 스포츠 도핑
#cf.https://search.naver.com/search.naver?where=news&query=%EC%8A%A4%ED%8F%AC%EC%B8%A0%20%EB%8F%84%ED%95%91&sm=tab_opt&sort=0&photo=0&field=0&reporter_article=&pd=3&ds=2018.02.09&de=2018.02.25&docid=&nso=so%3Ar%2Cp%3Afrom20180209to20180225%2Ca%3Aall&mynews=0&mson=0&refresh_start=0&related=0
####

from bs4 import BeautifulSoup
import urllib.request as req

# 1. 스포츠 도핑 기사자료 스크랩
from bs4 import BeautifulSoup
import urllib.request as req

#OUTPUT_FILE_NAME->doping1.txt
doping1_OUTPUT_FILE_NAME='D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1.txt'
doping1_URL="http://www.sportalkorea.com/news/view.php?gisa_uniq=2018022508475516&section_code=20&cp=se&gomb=1"

# doping2_URL="http://www.seoul.co.kr/news/newsView.php?id=20180225500002&wlog_tag3=naver"

# 2. 텍스트 파일로 저장(doping1.txt)
# #1)크롤링 함수 get_text():
def get_text(SSS): #URL="https:..."이 SSS로 들어감
    sourceFromURL=req.urlopen(SSS)
    soup=BeautifulSoup(sourceFromURL,'lxml', from_encoding='utf-8') #'lxml'은 'html.parser'와 같은 기능 but 속도 높음
    # print(soup)

    # text=soup.find_all('div',id='CmAdContent')# div태그를 모두 찾고, id가 'CmAdContent'인 것 모두 찾아라.
    # print(len(text))
    #
    text=""
    for item in soup.find_all('div', id='CmAdContent'):
        # print(item.find_all(text=True)) #text=True : 텍스트만 추출.
        text=text+str(item.find_all(text=True)) #item이 리스트로 출력되니 스트링(str)으로 바꾸어야함(여러개의 div태그로 구성될 시 유용함).
    print(text)
    return text
    # print(str(sourceFromURL))
    # return text

# #2)메인함수
#프로그램의 시작과 끝은 main함수로 시작 끝남.
def main():
    open_output_file=open(doping1_OUTPUT_FILE_NAME, "w")
    # get_text(doping1_URL)
    res=get_text(doping1_URL) #URL="https:..."이 res로 들어감
    open_output_file.write(res) #url->text

    # res2=get_text(doping2_URL) #URL="https:..."이 res로 들어감
    # open_output_file.write(res2) #url->text

    open_output_file.close()

# #함수 호출 부분:아래 main()->def main()을 호출함
# 8-2에서 import 하게 되면,__name__에 8-2가 들어감(cf.module1)
# 아래는 함수가 아니라 파이썬 문장임
if __name__=='__main__':
    main() #main함수를 호출해라


