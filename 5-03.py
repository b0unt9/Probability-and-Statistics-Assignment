start = int(input("시작 값을 입력하세요:"))
end = int(input("끝 값을 입력하세요:"))
drainage = int(input("배수를 입력하세요:"))
sum = 0

for i in range(start, end+1):
    if i % drainage == 0:
        sum += i

print(str(start) + "에서 " + str(end) + "까지 " + str(drainage) + "의 배수의 합은 " + str(sum) + "입니다.")