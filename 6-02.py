import math

a1 = int(input("초항을 입력하세요: "))
n = int(input("항의 개수를 입력하세요: "))
r = float(input("공비를 입력하세요: "))

result = a1*(1-r**n)/(1-r)

print(n,"항까지의 합은",result,"입니다.")