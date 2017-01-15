#간단한 메모장 만들기
import sys
#sys.argv는 프로그램 실행 시 입력된 값들을 읽어 들일 수 있는 파이썬 라이브러리
#sys.argv[0]은 입력받은 값 중에서 파이썬 프로그램 명(06_4.py), 따라서 필요 없는 값
#sys.argv[1]은 프로그램 실행 옵션값
#sys.argv[2]은 메모 내용
option = sys.argv[1]
#옵션 -a
if option == '-a':
    memo = sys.argv[2]
    #a옵션, 한줄씬 추가(append)
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
#옵션 -v
elif option == '-v':
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
