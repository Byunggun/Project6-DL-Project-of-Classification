# 3. 데이터 정제(크리닝)-영어, 특수기호 제거(정규식)
# 4. 정제된 결과를 텍스트 파일로 저장(output_cleaned.txt)
#입력:output.txt->데이터 크리닝->output_cleaned.txt로 저장

import re

doping1_INPUT_FILE_NAME="D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1.txt" #관례적으로 이런 방식으로 따로 파일로 주어 작성함. 입출력 파일의 변경 빈번하기에. 더 효율적임.
# doping2_INPUT_FILE_NAME="D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1.txt" #관례적으로 이런 방식으로 따로 파일로 주어 작성함. 입출력 파일의 변경 빈번하기에. 더 효율적임.

doping1_OUTPUT_FILE_NAME="D:\Python\MyGitHub\Project6-DL-Project-of-Classification\Doping Data/doping1_cleaned.txt"

#1)정제 함수(실무자.회사에서 실무를 담당.)
def clean_text(myText):
    #정제
    cleaned_text=re.sub('[a-zA-Z]', '', myText)#1차 정제 : text에 있는 영문 모두([a-zA-Z]) 삭제('')
    cleaned_text=re.sub('[\{\}\[\]\(\)\\\/▶_↑㎜.…,;\'\"@=|]','',cleaned_text) #2차 정제 : 특수문자({}[]-#()\)는 \기호 이용 ex){}표기시 \{\}로 표기해야.
    return cleaned_text

#2)메인 함수:입출력 작업에 빈번히 사용(팀장.관리자.회사에서 메니저의 역할격)
def main():
    doping1_read_file=open(doping1_INPUT_FILE_NAME, "r")
    # doping2_read_file = open(doping2_INPUT_FILE_NAME, "r")
    doping1_write_file=open(doping1_OUTPUT_FILE_NAME, "w")
    # print(read_file.read()) #파일 연 다음에 read() 필히 적어야
    text=doping1_read_file.read()
    # text2=doping2_read_file.read()
    print("before : ")
    print(text)
    # print(text2)
    cleaned_text=clean_text(text)
    # cleaned_text2 = clean_text(text2)
    print("after : ")
    print(cleaned_text)
    # print(cleaned_text2)
    doping1_write_file.write(cleaned_text)
    # doping1_write_file.write(cleaned_text2)
    doping1_read_file.close()
    doping1_write_file.close()

if __name__ == "__main__":
    main()