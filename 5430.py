import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    p = list(p)
    n = int(sys.stdin.readline().rstrip())
    state = 0
    rcount = 0
    if n == 0:
        arr = sys.stdin.readline().rstrip()
        arr = []
        for j in p:
            if j == "D":
                state = 1
                print("error")
                break
        if state == 0:
            print(arr)
    else:
        arr = sys.stdin.readline().rstrip()[1:-1].split(",")
        arr = list(map(str, arr))
        que = deque(arr)
        for j in p:
            if j == "R":
                if rcount == 1:
                    rcount = 0
                    continue
                rcount = 1
            elif j == "D":
                if len(que) == 0:
                    print("error")
                    state = 1
                    break
                else:
                    if rcount == 0:
                        que.popleft()
                    else:
                        que.pop()
        else:
            if rcount == 0:
                que = list(que)
                ab = ",".join(que)
                print('[' + ab + ']')
            else:
                que.reverse()
                que = list(que)
                ab = ",".join(que)
                print('[' + ab + ']')
