N = 10
for case in range(N):
    T = int(input())
    li = list(map(int,input().split()))
    i = 0
    while (li[-1] > 0):
        i = i%5 +1
        tmp = li.pop(0)
        li.append(tmp-i)
    if(li[-1 < 0 ]):
        li[-1] = 0

    print("#{} ".format(case+1),end='')
    for j in range(len(li)):
        print("{} ".format(li[j]),end='')
    print()


