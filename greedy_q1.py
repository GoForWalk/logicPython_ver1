import time
start_time = time.time() # 측정 시작

# 입력 받기
n, m, k = map(int, input("1번").split())

# N개의 수를 공백으로 구분하여 입력 받기
data = list(map(int, input("2번").split()))

data.sort()  # 입력받은 수를 정렬
first = data[n-1]
second = data[n-2]

result = 0

# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

count = (m // (k + 1)) * k
count += m % (k + 1)

result = count * first
result += (m - count) * second

print(result)


end_time = time.time() #측정 종료
print("time : ", end_time - start_time) #수행시간 출력