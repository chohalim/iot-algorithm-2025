def gugu(dan,num):
    print(f'{dan} x {num} = {dan*num:>2d}',end='\t')
    if num < 9:
        gugu(dan,num+1)

for dan in range(2,10):
    print(f'{dan}단')
    gugu(dan,1)
    print()