import random

while(1):
    print("==============================================================")
    print("1. 배수의 합계")
    print("2. 구구단 출력")
    print("3. 숫자 맞추기 게임")
    print("4. 종료")
    num = int(input("작업번호 입력=>"))
    if (num == 1):
        start = int(input("시작 값을 입력하세요:"))
        end = int(input("끝 값을 입력하세요:"))
        drainage = int(input("배수를 입력하세요:"))
        sum = 0

        for i in range(start, end+1):
            if i % drainage == 0:
                sum += i

        print(str(start) + " 에서 " + str(end) + " 까지 " + str(drainage) + " 의 배수의 합은 " + str(sum) + " 입니다.")

    elif (num == 2):
        for i in range(1, 10):
            for j in range (2, 10):
                print(str(j) + "X" + str(i)+ "=" + str(i*j), end='\t')
            print()


    elif (num == 3):
        nums = [random.randint(1,9), random.randint(1,9), random.randint(1,9)]
        print("정답:", nums)
        try_count = 0
        strike_count = 0
    
        while(strike_count<3):
            strike_count = 0
            ball_count = 0
            innum = []
            for i in range(3):
                num = int(input(str(i+1)+"번째 수 입력=>"))
                innum.append(num)
            try_count += 1
            print(str(innum))

            for j in range(0, 3):
                for k in range(0, 3):
                    if(nums[j] == innum[k] and j == k):
                        strike_count += 1
                    elif(nums[j] == innum[k] and j != k):
                        ball_count += 1              
            print(str(strike_count)+" 스트라이크 "+str(ball_count)+" 볼")
            
        print(str(try_count)+"번 만에 맞추었습니다.")
        
    elif (num == 4):
        print("프로그램을 종료합니다...")
        print("Bye Bye~")
        print("==============================================================")
        exit()

    else:
        print("숫자를 잘못 입력했습니다. 다시 입력하세요.")

    