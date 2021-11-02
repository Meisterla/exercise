import numpy as np

result = []


def queen(n, cur=0):
    if cur == len(n):
        print(n)
        return 0
    for col in range(len(n)):
        n[cur] = col
        flag = True
        for row in range(cur):
            if n[row] == col or col - n[row] == cur - row or col - n[row] == row - cur:
                flag = False
                break
        if flag:
            queen(n, cur+1)


queen([None]*4)

#print(result)