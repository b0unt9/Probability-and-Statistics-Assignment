n = int(input("항의 수를 입력하세요: "))

sigmak1 = n*(n+1)/2
sigmak2 = n*(n+1)*(2*n+1)/6
sigmak3 = (n*(n+1)/2)**2

k_dot_k_plus = n*(n+1)*(n+2)/3

print("항의 수가 "+str(n)+"인 ")
print("자연수의 합은 "+str(int(sigmak1)))
print("자연수의 제곱의 합은 "+str(int(sigmak2)))
print("자연수의 세제곱의 합은 "+str(int(sigmak3)))
print("연속된 두수의 곱의 합은 "+str(int(k_dot_k_plus)))