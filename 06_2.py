#3과 5의 배수 합 구하기
result = 0
for n in range(1, 1000):
    if n % 3 == 0 or n % 5 == 0:
        result = result + n
print(result)
