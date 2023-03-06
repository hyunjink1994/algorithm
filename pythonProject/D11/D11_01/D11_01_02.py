pipetype = [[0,0,0,0],[1,1,1,1],[1,0,0,1],[0,1,1,0],
            [1,0,1,0],[0,0,1,1],[0,1,0,1],[1,1,0,0]]

def connecting(x,nx):
    a = pipetype[x]
    b = pipetype[nx]
    for i in range(4):
        if(a[i] == 1 and b[3-i] == 1):
            return 1
    return 0




T = int(input())
for case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    map_li = [list(map(int,input().split()))for _ in range(N)]

    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    x = R
    y = C

    answer = [[x,y]]


    for i in range(1,L):
        for j in range(len(answer)):
            x = answer[j][0]
            y = answer[j][1]
            for k in range(4):
                nx = x+dx[k]
                ny = y+dy[k]
                if(nx < 0 or ny <0 or nx>=N or ny >=M):
                    continue
                else:
                    if(connecting(map_li[x][y],map_li[nx][ny])):
                        if([nx,ny] not in answer):
                            answer.append([nx, ny])
        print(answer)
    print(len(answer))
