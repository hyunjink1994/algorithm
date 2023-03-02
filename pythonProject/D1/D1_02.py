T = 10
for i in range(T):

    n = int(input())
    li = list(map(int, input().split()))
    diff = 0
    for j in range(2, len(li)-2):
        vs_li = li[j-2:3+j]
        if(max(vs_li) == li[j]):
            l = max(vs_li)
            vs_li.pop(2)
            diff = diff + l - max(vs_li)
        else:
            continue
    print("#{} {}".format(i+1,diff))