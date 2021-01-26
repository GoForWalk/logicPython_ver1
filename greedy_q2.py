import time
start_time = time.time() # 측정 시작

n, m = map(int, input().split())

result = 0;

while True:
    data = list(map(int, input().split()))
    n -= 1
    temp = min(data)
    if temp >= result:
        result = temp
    if n == 0:
        break

print(result)


end_time = time.time() #측정 종료
print("time : ", end_time - start_time) #수행시간 출력