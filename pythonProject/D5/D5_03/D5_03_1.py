def cal(N,li, answer):
    li_start = [li[i][0] for i in range(len(li))]
    li_end = [li[i][1] for i in range(len(li))]
    stack = []
    print("li :",li)
    for i in range(N):
        if(i not in li_end and i not in answer):
            stack.append(i)
    if(len(stack)==0):
        return answer
    else:
        p = stack.pop()
        answer.append(p)
        index = []
        for i in range(len(li_start)):
            if(li_start[i] == p):
                index.append(i)
        for j in range(len(index)):
            li.pop(index[j]-j)
        return cal(N,li,answer)
T = 10
for case in range(1,T+1):
    N,M = map(int,input().split())
    li = list(map(int,input().split()))
    li = [[li[2*i]-1, li[2*i+1]-1] for i in range(M)]

    answer = cal(N,li,[])
    print("#{} ".format(case),end='')
    for j in range(len(answer)):
        print("{}".format(answer[j]+1), end=' ')
