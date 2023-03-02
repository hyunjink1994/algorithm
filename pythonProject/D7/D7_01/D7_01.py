def parseInt(li):
    le = len(li)
    for i in range(le):
        for j in range(len(li[i])):
            if(j ==1):
                continue
            else:
                li[i][j] = int(li[i][j])

    return li

#LVR

def move(li,start,answer):

    # print("지금위치 :" , li[start][0])

    #탈출조건
    if(len(li[start])==2):
        answer.append(li[start][1])
        # print("자식없음! :",li[start][0])
    else:
        move(li,li[start][2],answer)
        answer.append(li[start][1])
        # print("자기 처리 : ",li[start][0])
        if(len(li[start]) ==4):
            move(li,li[start][3],answer)

    return answer




T = 10
for case in range(T):
    N = int(input())

    li = [list(input().split()) for _ in range(N)]
    li = parseInt(li)
    empty = []
    li.insert(0,empty)
    answer_li = move(li,1,[])
    answer =''
    for i in range(len(answer_li)):
        answer+=answer_li[i]
    print("#{} {}".format(case+1, answer))
