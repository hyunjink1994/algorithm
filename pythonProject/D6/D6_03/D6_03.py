def cal(li,start_li,visit):
    for j in range(len(start_li)):
        visit.append(start_li[j])
    while (True):
        answer = []
        for i in range(len(li)):
            if(li[i][0] in start_li and li[i][1] not in visit):
                answer.append(li[i][1])
        if(len(answer) == 0):
            break
        for k in range(len(answer)):
            visit.append(answer[k])
        start_li = answer
    return start_li

T = 10
for case in range(1,T+1):
    N, M =map(int,input().split())
    li = list(map(int,input().split()))
    L = len(li)
    lia = li[::2]
    lib = li[1::2]
    start_li = [M]

    li = []
    visit = []
    for i in range(int(L/2)):
        k = [lia[i], lib[i]]
        li.append(k)

    answer = max(cal(li,start_li,visit))
    print("#{} {}".format(case,answer))