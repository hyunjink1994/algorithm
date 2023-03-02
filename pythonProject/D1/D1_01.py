T = int(input())
for i in range(T):
    n = int(input())
    li = list(map(int,input().split()))

    li_s = set(li)
    dic = dict()
    for j in li_s:
        dic[j] = li.count(j)
    answer = [k for k,v in dic.items() if(max(dic.values()) == v)]
    print("#{} {}".format(i+1, answer[0]))



