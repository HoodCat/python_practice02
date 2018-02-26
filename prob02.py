from functools import reduce

buffer = [0]*5

print(len(buffer), '개의 숫자를 입력하세요', sep='')
for i in range(len(buffer)):
    buffer[i] = int(input())

# 함수형 프로그래밍
avg = reduce(lambda acc, x: acc+x, buffer) / len(buffer)
print('평균은', avg, '입니다')