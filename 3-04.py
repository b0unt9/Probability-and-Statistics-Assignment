money = int(input("투입한 돈: "))
price = int(input("물건값: "))
change = money - price
print("거스름돈:", change)
print("500원 동전의 개수:", change//500)
print("100원 동전의 개수:", (change % 500)//100)