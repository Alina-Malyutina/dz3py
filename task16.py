N = int(input('Enter quantity of numbers in list: '))

A = [i for i in range(1, N+1) ]
print(A)
X = int(input('Enter searching number: '))
print(A.count(X))