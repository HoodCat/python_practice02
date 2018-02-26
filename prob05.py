import random

# 난수 생성. random 모듈에 random()함수 [0, 1)
while(True):
    print("수를 결정하였습니다. 맞추어 보세요")
    correct = round(random.random()*99 + 1)
    higher = 1
    lower = 100
    answer = -1
    count = 1

    while(answer != correct):
        print(higher, '-', lower, sep='')
        answer = int(input(str(count)+'>>'))
        if answer > correct:
            print('더 낮게')
            lower = answer
        elif answer < correct:
            print('더 높게')
            higher = answer
        count += 1
    
    print('맞았습니다')
    retry = input('다시하시겠습니까(y/n)>>')

    if retry=='n':
        break