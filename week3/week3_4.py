korean = int(input("국어 점수: "))
english = int(input("영어 점수: "))
math = int(input("수학 점수: "))
science = int(input("과학 점수: "))

total = korean + english + math + science
average = total / 4

if average >= 95:
    grade = 'A+'
elif average >= 90:
    grade = 'A0'
elif average >= 85:
    grade = 'B+'
elif average >= 80:
    grade = 'B0'
elif average >= 75:
    grade = 'C+'
elif average >= 70:
    grade = 'C0'
elif average >= 65:
    grade = 'D+'
elif average >= 60:
    grade = 'D0'
else:
    grade = 'F'

print(f"국어: {korean}, 영어: {english}, 수학: {math}, 과학: {science}")
print(f"합계: {total}, 평균: {average:.2f}")
print(f"학점: {grade}")
