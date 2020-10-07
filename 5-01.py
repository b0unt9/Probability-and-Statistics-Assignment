num = int(input("하나의 정수를 입력하세요:"))
sum = 0

for i in range(num+1):
    sum += i

print("1부터 " + str(num) + "의 합은 " + str(sum) +"입니다.")