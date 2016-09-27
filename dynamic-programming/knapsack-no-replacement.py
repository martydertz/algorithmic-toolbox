# Uses python3
import sys
import math
# small 'w' is list of weights of bars
# big 'W' is capacity of knapsack

def optimal_weight(W, w):
  
    results = [[0] * (W + 1) for x in range(len(w))]
    # Set results[0] to w[0] if w[0] <= j
    results[0] = [w[0] if w[0] <= j else 0 for j in range(W + 1)]
    for i in range(1, len(w)):
        for j in range(1, W + 1):
            if w[i] <= j:
                if results[i - 1][j] < (results[i - 1][j - w[i]]) + w[i]:
                    results[i][j] = (results[i - 1][j - w[i]]) + w[i]
                else:
                    results[i][j] = results[i - 1][j]  
            else:
                results[i][j] = results[i - 1][j] 
           
    return results[-1][-1]
  

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
