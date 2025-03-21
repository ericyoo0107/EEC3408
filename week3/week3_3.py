number = int(input("양수 입력(3 이상): "))
result = []
prev = 1
now = 1
result.append(prev)
result.append(now)
for i in range(number - 2):
    temp = prev
    prev = now
    now = temp+now
    result.append(now)

print(result)