i = 1
while (i < 10):
    j = 2
    while (j < 10):
        print(str(j) + "X" + str(i)+ "=" + str(i*j), end='\t')
        j += 1
    print()
    i += 1