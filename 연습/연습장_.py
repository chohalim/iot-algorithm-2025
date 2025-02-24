def binSearch(ary, fData):
    pos = -1
    start = 0
    end = len(ary)-1
    count = 0

    while (start <= end):
        mid = (start+end)//2
        count += 1
        if fData == ary[mid]:
            print(f'총 검색횟수 {count}')
            return mid
        elif fData > ary[mid]:
            start = mid+1
        else:
            end=mid-1

    print(f'총 검색횟수 {count}')
    return pos
    

import random
Ary = [i for i in range(1,100001)]
dataAry = [random.choice(Ary) for _ in range(100000)]
dataAry.sort()
findData=int(input('찾는 데이터를 입력하세요 ->'))

position = binSearch(dataAry,findData)
if position == -1:
    print(f'{findData}(이) 없네요.')
else:
    print(f'{findData}는 {position}위치에 있음')



