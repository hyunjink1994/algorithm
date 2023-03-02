N = 10
for i in range(N):
    L, li = map(str, input().split())
    L = int(L)
    li_a = [li[i] for i in range(len(li))]
    flag = 1
    while (flag ==1):
        tag = 0
        for j in range(len(li_a)-1):
            if(li_a[j] == li_a[j+1]):
                li_a.pop(j)
                li_a.pop(j)
                tag = 1
                break
        if(tag == 0):
            flag = 0
    answer = ''.join(li_a)
    print("#{} {}".format(i+1, answer))
