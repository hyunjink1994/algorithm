def findLoad(startli, endli, answer):
    visited = []
    for i in range(len(endli)):
        for j in range(len(answer)):
            if (endli[i] == answer[j]):
                visited.append(startli[i])
    visited = set(visited)
    answer = list(visited)
    if (0 in answer):
        return answer
    if (len(answer) == 0):
        return answer
    else:
        return findLoad(startli, endli, answer)


N = 10
for i in range(N):
    T, L = map(int, input().split())
    li = list(map(int, input().split()))
    start = li[::2]
    end = li[1::2]
    answer = [99]
    ans = 0
    if (0 in findLoad(start, end, answer)):
        ans = 1
    print("#{} {}".format(T, ans))