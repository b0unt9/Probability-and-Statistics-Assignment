start = int(input("시작 값을 입력하세요:"))
end = int(input("끝 값을 입력하세요:"))
sum = 0

for i in range(start, end+1):
    sum += i

print(str(start) + "에서 " + str(end) + "까지의 합은 " + str(sum) + "입니다.")