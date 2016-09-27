#The goal in this problem is to find the minimum number of coins needed to change the input value (an integer) 
# into coins with denominations 1, 5, and 10
import sys

def get_change(m):
    #write your code here
    coins = 0
    if m >= 10:
        coins += (m//10)
        m = m % 10
    if m >= 5:
        coins += (m//5)
        m = m % 5
    if m > 0:
        coins += m
        
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
