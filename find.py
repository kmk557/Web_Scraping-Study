import re

x = open('short.txt')
#파일을 불러옵니다.
for line in x:
    line = line.rstrip()        #오른쪽에서부터 공백이 아닐때까지 공백값을 컷
    if re.search('From:',line): #문장에서 '' 안의 값이 있는 지 확인한다. ( 대소문자 구분 )
        print(line)