import email
import os
from email import policy
from email.parser import BytesParser
import sys
# 첫 번쨰 블록
def extract_text_from_eml (file_path): #  내용 추출블럭 만들기
    with open(file_path , 'rb' ) as f:
        msg = BytesParser(policy = policy.default).parse(f)
    try :
     text = ' '
     if msg.is_multipart(): # 메일이 여러 개의 파트로 나누어져 있는 경우
      for part in msg.walk():
       if part.get_content_type == 'text/plain':
        text += part.get_content()
       else : 
        text = msg.get_content()
      return text
    except :
      print("추출블록에서 에러")
      sys.exit()

#두 번쨰 블록
input_dir = 'goldmansachs'          # 내용 추출한 파일이 담긴 폴더
output_dir = 'goldmansachscorpus'   # 내용 추출한 파일을 저장할 폴더
if not os.path.exists(output_dir):    
    os.makedirs(output_dir)
try : 
 for filename in os.listdir(input_dir):  
   if filename.endswith('.eml'):            # 확장자 확인
       file_path = os.path.join(input_dir, filename)
       text = extract_text_from_eml(file_path)  # 내용 추출 함수 호출하여 반환된 내용을 text 변수에 저장
       output_path = os.path.join(output_dir,filename.replace('.eml','.txt')) # 확장자 변경
       with open(output_path,'w',excoding = 'utf-8') as f:
          f.write(text) # 내용 저장
except :
  print("내용 저장 과정에서의 에러")
  sys.exit()
# 세 번쨰 블록
from nltk.corpus import PlaintextCorpusReader
try :
 corpus_root = 'goldmansachscorpus'  # 내용 추출한 파일이 담긴 폴더
 wordlists = PlaintextCorpusReader(corpus_root, '.*.txt') # 확장자 확인
 print(wordlists.fileids()) # 파일 목록 확인
except :
  print("도수분석 과정에서의 에러")

'''아무래도 try except 사이에 함수호출이 있다보니 논리구조상 두번째 블록 -> 첫번째 블록 -> 
추출블록 에러 -> 내용 저장 과정 에러 이런 식인 듯. 필요에 따라 try ~ except 를 세분화하거나 아니면 함수블록 자체를 여러개로
구분하거나 하는 과정도 필요해 보인다.'''