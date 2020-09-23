import random

for i in range(10):
    kick = input("어디로 킥을 하시겠습니까(왼쪽, 중앙, 오른쪽)? :")
    area = random.choice(['왼쪽', '중앙', '오른쪽'])

    if kick != area:
        print("골키퍼가 막은 곳:", area)
        print("페널티 킥이 성공하였습니다.")
    else:
        print("골키퍼가 막은 곳:", area)
        print("페널티 킥이 실패하였습니다.")