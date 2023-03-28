N = int(input('Enter quantity of numbers in list: '))
A = [i for i in range(1, N+1)]
print(A)
X = int(input('Enter searching number: '))
difference = []
for i in A:
    if i == X:
        print(i)
        exit()
    else:
        difference.append(abs(i-X))
min = difference[0]
imin = 0
for i in range(len(difference)):
    if difference[i] < min:
        min = difference[i]
        imin = i
print(A[imin])