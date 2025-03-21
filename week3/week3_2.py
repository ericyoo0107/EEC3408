import random

# 1) 빈 리스트 만들기
lotto = []

# 2) 1~45 정수 중 6개 랜덤 생성하여 리스트에 추가 (중복 없음)
lotto_numbers = random.sample(range(1, 46), 6)

# 3) 6개 요소는 오름차순 정렬
lotto_numbers.sort()

# 4) ‘당첨번호:’와 ‘보너스번호:’ 문자열을 리스트에 추가
lotto.append("당첨번호:")
lotto.extend(lotto_numbers)

# 5) 1~45 정수 중 1개 랜덤 생성하여 리스트에 추가 (중복 없음)
bonus_number = random.choice([num for num in range(1, 46) if num not in lotto_numbers])
lotto.append("보너스번호:")
lotto.append(bonus_number)

# 6) 리스트 출력
print(lotto)
