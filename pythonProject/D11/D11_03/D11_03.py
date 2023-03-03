dx = [0, -1, 0, 1, 0]
dy = [0, 0, 1, 0, -1]

def move(startX,startY,forward):
    return [startX+dx[forward] , startY+dy[forward]]

def connect(X,Y,C_list):
    answerX = []
    answerY = []
    for j in range(len(C_list)):
        distance_X = abs(X[0]-C_list[j][1]) + abs(X[1]-C_list[j][0])
        distance_Y = abs(Y[0]-C_list[j][1]) + abs(Y[1]-C_list[j][0])
        if(distance_X <= C_list[j][2]):
            answerX.append([j,C_list[j][3]])
        if(distance_Y <= C_list[j][2]):
            answerY.append([j,C_list[j][3]])

    return [answerX,answerY]

def maxSum(answerX,answerY,C_list):
    li = []
    C_value = [C_list[i][3] for i in range(len(C_list))]
    C_value.append(0)
    avail_X = [0 for _ in range(len(C_list)+1)]
    avail_Y = [0 for _ in range(len(C_list)+1)]

    for i in range(len(answerX)):
        avail_X[answerX[i][0]] = answerX[i][1]
    for i in range(len(answerY)):
        avail_Y[answerY[i][0]] = answerY[i][1]

    for i in range(len(avail_X)):
        tmp_a = avail_X[i]
        for j in range(len(avail_Y)):
            tmp_b = avail_Y[j]
            if(i == j):
                tmp_b = 0
            li.append(tmp_a+tmp_b)

    return max(li)

T = int(input())

for case in range(1,T+1):
    M, A = map(int,input().split())
    li = [[0]*11]*11
    move_A = list(map(int,input().split()))
    move_B = list(map(int,input().split()))
    C_list = [list(map(int,input().split())) for _ in range(A)]

    y = [10,10]
    x = [1,1]

    move_A.insert(0,0)
    move_B.insert(0,0)

    answer = 0
    for i in range(M+1):
        x = move(x[0],x[1],move_A[i])
        y = move(y[0],y[1],move_B[i])
        answerPrint = connect(x,y,C_list)
        answer += maxSum(answerPrint[0],answerPrint[1],C_list)
    print("#{} {}".format(case,answer))
