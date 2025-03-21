import random

numbers = []

for _ in range(10):
    numbers.append(random.randint(1, 10))

print("리스트 요소:")
for num in numbers:
    print(num)

user_input = int(input("1~10 사이의 정수를 입력하세요: "))

if user_input in numbers:
    print(f"{user_input}은(는) 리스트에 있습니다.")
    print(f"총 {numbers.count(user_input)}개 있습니다.")
else:
    print(f"{user_input}은(는) 리스트에 없습니다.")

numbers = [num for num in numbers if num != user_input]

print("업데이트된 리스트:")
for num in numbers:
    print(num)