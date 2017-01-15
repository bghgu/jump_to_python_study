#문서 파일을 읽어서 그 문서 파일 내에 있는 탭(tab)을 공백(space) 4개로 바꾸어주는 스크립트
import sys

src = sys.argv[1]
dst = sys.argv[2]
#파일을 읽어 들인다
f = open(src)
tab_content = f.read()
f.close()
#문자 교체 내장 함수로 교체
space_content = tab_content.replace("\t", " "*4)
print(space_content)
#바꾼 문자열을 새 파일에 저장
f = open(dst, 'w')
f.write(space_content)
f.close()
