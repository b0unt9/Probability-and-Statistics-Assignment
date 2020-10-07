a, d, l = map(int, input().split())
n = (l - a)/d + 1
print(int(n*(a + l)/2))