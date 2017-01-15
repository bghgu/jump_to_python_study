#하위 디렉터리 검색하기
import os

def search(dirname):
    try:
        #os.listdir : 해당 디렉터리에 엤는 파일들의 리스트를 구할 수 있다
        filenames = os.listdir(dirname)
        for filename in filenames:
            #디렉터리와 파일명을 이어주는 os.path.join함수
            full_filename = os.path.join(dirname, filename)
            #재귀함수로 구현
            #해당 디렉터리의 하위 파일들을 다시 검색하기 시작하므로 결국 모든 파일들을 검색 할 수 있게 된다.
            if os.path.isdir(full_filename):
                search(full_filename)
            else:
                #파일명에서 확장자만 추출해주는 os.path.splitext함수
                #os.path.splitext는 파일명을 확장자를 기준으로 두 부분으로 나누어 준다.
                #os.path.splitext(full_filename)[-1]은 해당 파일의 확장자명
                ext = os.path.splitext(full_filename)[-1]
                if ext == '.py':
                    print(full_filename)
    #권한이 없는 디렉터리에 접근하면 그냥 패스
    except PermissionError:
        pass

search("c:/")
