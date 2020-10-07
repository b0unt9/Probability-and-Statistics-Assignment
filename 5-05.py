gugudan = int(input("단을 입력하세요:"))
i = 1

while i <= 9:
    print(str(gugudan) + "X" + str(i) + "=" + str(gugudan*i))
    i += 1

for j in range(1, 10):
    print(str(gugudan) + "X" + str(j) + "=" + str(gugudan*j))