start, end, mode = input("숫자 2개와 출력 모드(v 또는 h) 입력: ").split()
start, end = int(start), int(end)

if mode == 'v':  # 세로 출력
    for i in range(1, 10):
        for j in range(start, end + 1):
            print(j, '×', i, '=', j * i, end='\t')
        print()
elif mode == 'h':  # 가로 출력
    for j in range(start, end + 1):
        for i in range(1, 10):
            print(j, '×', i, '=', j * i, end='\t')
        print()
else:
    print("잘못된 모드를 입력하세요 (v 또는 h)")
