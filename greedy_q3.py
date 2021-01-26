n, k = map(int, input().split())

count = 0

while n != 1:
    temp = n % k
    if temp == 0:
        n /= k
        count += 1
    else:
        n -= temp
        count += temp

print(count)
