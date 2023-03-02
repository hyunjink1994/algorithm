
modul = ['+', '-', '*', '/']
def cal(a, b, _modul):
    if _modul == 0:
        return a + b
    elif _modul == 1:
        return a - b
    elif _modul == 2:
        return a * b
    else:
        return int(a / b)

def dfs(idx, answer,N):
    if idx >= N:
        global  max_n, min_n
        if answer > max_n:
            max_n = answer
        if answer < min_n:
            min_n = answer
        return
    for i in range(4):
        if moduls[i]:
            moduls[i] -= 1
            dfs(idx + 1, cal(answer, numbers[idx + 1], i),N)
            moduls[i] += 1


T = int(input())
for t in range(1, T + 1):
    N = int(input()) - 1
    moduls = list(map(int, input().split()))
    max_n = -987654321
    min_n = 987654321
    numbers = list(map(int, input().split()))
    dfs(0, numbers[0],N)
    print('#{} {}'.format(t, max_n - min_n))
