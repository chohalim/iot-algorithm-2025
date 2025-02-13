# da03_linear_list.py
# 선형리스트 일반 구현
# 실제 파이썬이 이렇게 동작하는 게 아님
# 배열(선형리스트)이 어떻게 동작하는지 로직을 파악할 것
## 전역변수 선언 부분
katok = [] # 빈 배열
select = -1 # -1:통과 1:추가 2:삽입 3:삭제 4:종료 

## 함수 선언 부분
# 데이터 추가
def add_data(firend):
    katok.append(None)
    lenKatok = len(katok)
    katok[lenKatok-1] = firend

# 중간에 데이터 삽입
def insert_date(pos, friend):
    # 잘못된 인덱스를 넣었을 떄 예외처리 필요
    if pos < 0 or pos > len(katok):
        print('실행할 범위를 벗어났습니다.')
        return

    katok.append(None) # 빈칸 추가
    lenKatok = len(katok)

    for i in range(lenKatok - 1, pos, -1): # 추가할 위치까지 데이터를 뒤로 이동
        katok[i] = katok[i-1]
        katok[i-1] = None

    katok[pos] = friend

# 메인코드 영역
if __name__ == '__main__':

    while True:
        select = int(input('선택(1:추가, 2:삽입, 3:삭제, 4:종료) >'))

        if select == 1:
            date = input('추가 데이터->')
            add_data(date)
            print(katok)
        elif select == 2:
            pos, date = input('삽입위치, 이름, 데이터 입력 ->').split()
            pos = int(pos)
            insert_date(pos,date)
            print(katok)
        elif select == 3:
            pos = int(input('삭제위치 ->'))
            delete_date(pos)
            print(katok)
        elif select == 4:
            break
        else:
            print('1 ~ 4중 입력할 것')
            continue