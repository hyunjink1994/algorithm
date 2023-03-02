import operator

def calR(li , r):
    ans_li = li[r]
    s = set(ans_li)
    dic = dict()
    for i in s:
        dic[i] = ans_li.count(i)
    dic = sorted(dic.items(), key=operator.itemgetter(1))
    lib = []
    for i in range(len(dic)):
        if(dic[i][0] == 0):
            continue
        lib.append(dic[i][0])
        lib.append(dic[i][1])
    return lib

def calC(li, c):
    ans_li = [[i[c] for i in li ]]

    return calR(ans_li, 0)

def check(li):
    rl = len(li)
    rc = len(li[0])

    if(rl >= rc):
        return [0,rl]
    else:
        return [1,rc]

def cross(li):
    zli = list(zip(*li))
    ans = []
    for i in range(len(zli)):
        ans.append(list(zli[i]))
    return ans

def blankfull(li):
    max_int = 0
    for i in range(len(li)):
        if(max_int<len(li[i])):
            max_int = len(li[i])

    for i in range(len(li)):
        for j in range(max_int - len(li[i])):
            li[i].append(0)

    return li

def checklegnth(li):
    answer_list = []
    x_len = len(li);
    y_len = len(li[0]);

    if(x_len >100):
        for i in range(100):
            answer_list.append(li[i])

    if(y_len > 100):
        for i in range(100):
            ans_li = [[i[c] for i in li]]
            answer_list.append(ans_li)

        answer_list = cross(answer_list)

    return answer_list






r,c,k = map(int, input().split())
li= []
for i in range(3):
    li.append(list(map(int,input().split())))



answer = -1
for i in range(100):
    checklegnth(li)
    answer_list = []
    if(len(li) >= r and len(li[0]) >= c):
        if(li[r-1][c-1] == k):
            answer = i
            break

    for i in range(check(li)[1]):
        if (check(li)[0] == 0):
            answer_list.append(calR(li, i))
        else:
            answer_list.append(calC(li, i))
        answer_list = blankfull(answer_list)
    if (check(li)[0] == 1):
        answer_list = cross(answer_list)
    li = answer_list

print(answer)