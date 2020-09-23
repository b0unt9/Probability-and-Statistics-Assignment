import random

hour = random.randint(1,24)
weather = bool(random.getrandbits(1))

print("좋은 아침입니다. 지금 시각은", hour, "시입니다.")
if weather == True:
    print("현재 날씨가 화창합니다.")
else:
    print("현재 날씨가 화창하지 않습니다.")

if 6 <= hour and hour <= 9 and weather == True:
    print("종달새가 노래를 합니다.")
else:
    print("종달새가 노래를 하지 않습니다.")