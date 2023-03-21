A = [1-x for x in range(1,11)]
B = [pow(4,x) for x in range(8)]
C = [i for i in B if i % 2 == 0]
print(A)
print(B)
print(C)