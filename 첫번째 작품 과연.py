import email
import os
from email import policy
from email.parser import BytesParser
import sys
import nltk
# 첫 번쨰 블록
def extract_text_from_eml (file_path): #  내용 추출블럭 만들기
    with open(file_path , 'rb' ) as f:
        msg = BytesParser(policy = policy.default).parse(f)
    text = ' '
    parts = []
    # 메일의 본문을 추출하는 부분
    # 메일이 멀티파트인지 확인
    # 멀티파트인 경우 각 파트를 순회하며 본문을 추출
    # 싱글파트인 경우 본문을 바로 추출
    try:
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_dispo = str(part.get("Content-Disposition"))

                # 본문(text/plain)이고 첨부파일이 아니어야 함
                if content_type == 'text/plain' and 'attachment' not in content_dispo:
                    parts.append(part.get_content())
        else:
            # 싱글파트는 그냥 받아도 됨
            parts.append(msg.get_content())
    except Exception as e:
        print(f"Error extracting text: {e}")

    return '\n'.join(parts)

#두 번쨰 블록
input_dir = '/Users/hwang/Desktop/NLP/goldmansachs'          # 내용 추출한 파일이 담긴 폴더
output_dir = '/Users/hwang/Desktop/NLP/goldmansachscorpus'   # 내용 추출한 파일을 저장할 폴더
if not os.path.exists(output_dir):   
    os.makedirs(output_dir)
try : 
 for filename in os.listdir(input_dir):  
   if filename.endswith('.eml'):            # 확장자 확인
       file_path = os.path.join(input_dir, filename)
       text = extract_text_from_eml(file_path)  # 내용 추출 함수 호출하여 반환된 내용을 text 변수에 저장
       output_path = os.path.join(output_dir,filename.replace('.eml','.txt')) # 확장자 변경
       with open(output_path,'a+',encoding = 'utf-8') as f:
          f.write(text) # 내용 저장
except :
  print("내용 저장 과정에서의 에러")
  
# 세 번쨰 블록
from nltk.corpus import PlaintextCorpusReader

corpus_root = output_dir  # 내용 추출한 파일이 담긴 폴더
wordlists = PlaintextCorpusReader(corpus_root, '.*.txt') # 확장자 확인
print("코퍼스가 만들어졌습니다.")
print(wordlists.fileids()) # 코퍼스에 있는 파일 리스트 출력
if wordlists.fileids() == []:
    
  print("코퍼스가 없음.")

'''
완성본.
한 90% 는 인공지능이 만들었지만 그래도 기분이 좋다.
이 코드 사용 버전은 3.12.7 이다. 
'''