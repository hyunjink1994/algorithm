pipetype = [[0,0,0,0],[1,1,1,1],[1,0,0,1],[0,1,1,0],
            [1,0,1,0],[0,0,1,1],[0,1,0,1],[1,1,0,0]]

def connecting(pipetype,x,nx):
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

    start = [[R,C]]
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    end = []
    for i in range(L-1):
        for j in range(len(start)):
            x = start[j][0]
            y = start[j][1]
            for k in range(4):
                nx = x+ dx[k]
                ny = y+ dy[k]

                if(nx < 0 or ny <0 or nx >=N or ny >=M):
                    continue
                else:
                    if(connecting(pipetype,map_li[x][y],map_li[nx][ny]) and [nx, ny] not in end):
                        end.append([nx,ny])
        for m in range(len(end)):
            if(end[m] not in start):
                start.append(end[m])
        print("{} 시간 뒤 갈 수 있는 위치 : {}".format(i+1,start))
    print(len(start))





