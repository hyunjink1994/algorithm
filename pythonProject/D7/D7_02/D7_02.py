def parseInt(li):
    le = len(li)
    for i in range(le):
        for j in range(len(li[i])):
            if(j ==1):
                continue
            else:
                li[i][j] = int(li[i][j])

    return li

#LRV

def move(li,start,answer):

    # print("지금위치 :" , li[start][0])

    #탈출조건
    if(len(li[start])==2):
        answer.append(li[start][1])
        # print("자식없음! :",li[start][0])
    else:
        move(li,li[start][2],answer)
        # print("자기 처리 : ",li[start][0])
        if(len(li[start]) ==4):
            move(li,li[start][3],answer)
        answer.append(li[start][1])

    return answer

def answerchange(li):
    for i in range(len(li)):
        if(li[i] != '+' and li[i] != '-' and li[i] != '*' and li[i] != '/'):
            li[i] = int(li[i])
    return li


def cal(li):
    stack = []
    L = len(li)
    for i in range(L):
        if(li[i] == '+'):
            a = stack.pop()
            b = stack.pop()
            c = b+a
            stack.append(c)
        elif(li[i] == '-'):
            a = stack.pop()
            b = stack.pop()
            c = b-a
            stack.append(c)
        elif(li[i] == '*'):
            a = stack.pop()
            b = stack.pop()
            c = b*a
            stack.append(c)
        elif(li[i] == '/'):
            a = stack.pop()
            b = stack.pop()
            c = int(b/a)
            stack.append(c)
        else:
            stack.append(li[i])
        # print(stack)
    return stack[0]
T = 10
for case in range(T):
    N = int(input())

    li = [list(input().split()) for _ in range(N)]
    li = parseInt(li)
    empty = []
    li.insert(0,empty)
    answer_li = move(li,1,[])

    # answer =''
    # for i in range(len(answer_li)):
    #     answer+=answer_li[i]
    print("#{} {}".format(case+1, cal(answerchange(answer_li))))
