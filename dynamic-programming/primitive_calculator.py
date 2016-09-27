# Uses python3
import sys

def optimal_sequence(n):
    minNumOperations = [(10**9,0)]*(n+1)
    minNumOperations[0] = (0,0)
    minNumOperations[1] = (0,1)
    for num in range(1,n+1):
        double = num*2
        triple = num*3
        plusOne = num+1
        numOperations = minNumOperations[num][0] + 1
        if double <= n:
            if numOperations < minNumOperations[double][0]:
                minNumOperations[double] = (numOperations,2)
        if triple <= n:
            if numOperations < minNumOperations[triple][0]:
                minNumOperations[triple] = (numOperations,3)
        if plusOne <= n:
            if numOperations < minNumOperations[plusOne][0]:
                minNumOperations[plusOne] = (numOperations,1)

    path = [n]
    while n > 1:    
        operation = minNumOperations[n][1]
        if operation == 1:
            path.append(n-1)
            n -=1
        if operation == 2:
            path.append(n//2)
            n = n//2
        if operation == 3:
            path.append(n//3)
            n = n//3
    return list(reversed(path))
                

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

