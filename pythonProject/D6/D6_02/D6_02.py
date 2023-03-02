def cal (li):
    answer = []
    for i in range(16):
        lip = li[i]
        empty =[]
        for j in range(16):
            tmp = lip%10
            empty.insert(0,tmp)
            lip = int(lip/10)
        answer.append(empty)
    return answer

def findXY(li,GAP):
    answer = []
    for i in range(16):
        for j in range(16):
            if(li[i][j] == GAP):
                answer.append(i)
                answer.append(j)
    return answer

def findLoad(li,startX,startY,visit,answer):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    visit[startX][startY] = 1
    for i in range(4):
        nx = startX+dx[i]
        ny = startY+dy[i]
        if(nx < 0 or nx > 15 or ny <0 or ny > 15):
            continue
        if(visit[nx][ny] == 1):
            continue
        if(li[nx][ny] == 1):
            continue
        k = [nx,ny]
        answer.append(k)
        findLoad(li,nx,ny,visit,answer)

    return answer

N = 10
for i in range(N):
    T = int(input())
    li = [int(input()) for _ in range(16)]
    li = cal(li)
    visit = li
    start = findXY(li,2)
    end = findXY(li,3)
    answer = findLoad(li,start[0],start[1],visit,[])
    if(end in answer):
        print("#{} {}".format(i+1, 1))
    else:
        print("#{} {}".format(i+1, 0))
