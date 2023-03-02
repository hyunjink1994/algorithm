def pow (N,M):
    answer = 1
    for i in range(M):
        answer*=N
    return answer


T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    mod = N%M
    modi_mod = int
    while(mod != modi_mod):
        K = pow(N,N)
        modi_mod = K%M
        if(mod == modi_mod):
            break
        else:
            mod = modi_mod
    print("T : ",mod)
