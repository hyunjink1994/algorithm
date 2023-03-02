
import psutil
modul = ['+', '-', '*', '/']


def cal(a, b, _modul):
    if _modul == 0:
        return a + b
    elif _modul == 1:
        return a - b
    elif _modul == 2:
        return a * b
    # //를 하게되면 내림으로 되기때문에 버림으로 처리
    else:
        return int(a / b)


def dfs(idx, _ans):
    print("----------------------------dfs start : {}-------------------------".format(idx))
    if idx >= N:
        global max_n, min_n
        if _ans > max_n:
            max_n = _ans
        if _ans < min_n:
            min_n = _ans
        print("max_n :", max_n ,end='\t')
        print("min_n :",min_n)
        print("------------------------------end---------------------------------")
        return
    for i in range(4):
        if moduls[i]:
            print("moduls : ",moduls)
            moduls[i] -= 1
            print(_ans , moduls[i] , numbers[idx+1])
            print("answer : ",cal(_ans, numbers[idx + 1], i))
            dfs(idx + 1, cal(_ans, numbers[idx + 1], i))
            moduls[i] += 1


T = int(input())
for t in range(1, T + 1):
    N = int(input()) - 1
    moduls = list(map(int, input().split()))
    max_n = -987654321
    min_n = 987654321
    numbers = list(map(int, input().split()))
    dfs(0, numbers[0])
    print('#{} {}'.format(t, max_n - min_n))


# print(psutil.virtual_memory())