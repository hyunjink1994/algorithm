T = 10
for i in range(T):
    n = int(input())
    li = list(map(int,input().split()))
    li_count = [0 for i in range(101)]

    up = 0
    down = 0

    for j in range(len(li)):
        li_count[li[j]] = li_count[li[j]]+1

    for a in range(n):
        for k in range(len(li_count)):
            if(li_count[k] != 0):
                li_count[k] = li_count[k]-1
                li_count[k+1] = li_count[k+1]+1
                down = k
                if(li_count[k] == 0):
                    down = k+1
                break

        for l in range(len(li_count) - 1, 0, -1):
            if(li_count[l] !=0):
                li_count[l] = li_count[l]-1
                li_count[l-1] = li_count[l-1]+1
                up = l
                if(li_count[l] == 0):
                    up = l-1
                break

    print("#{} {}".format(i+1,up-down))