pipetype = [[0,0,0,0],[1,1,1,1],[1,0,0,1],[0,1,1,0],
            [1,0,1,0],[0,0,1,1],[0,1,0,1],[1,1,0,0]]

def solution(map_li,N,M,input_li,answer):
    for t in range(len(input_li)):
        x = input_li[t][0]
        y = input_li[t][1]

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if(nx < 0 or ny <0 or nx >= N or ny >= M):
                continue
            else:
                pipeA = map_li[x][y]
                pipeB = map_li[nx][ny]
                if (pipetype[pipeA][i] == 1 and pipetype[pipeB][3 - i] == 1 and [nx,ny] not in answer):
                    answer.append([nx,ny])

    return answer


T = int(input())
for case in range(1,T+1):
    N, M, R, C, L = map(int,input().split())
    map_li = [list(map(int,input().split()))for _ in range(N)]

    dx = [-1,0,0,1]
    dy = [0,-1,1,0]

    start = [[R,C]]
    answer = [[R,C]]

    for i in range(L-1):
        start = solution(map_li,N,M,start,answer)
    print("#{} {}".format(case,len(start)))

