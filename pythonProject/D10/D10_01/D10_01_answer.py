def checkLoad(map_li, i,j, sum, answer):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    height = map_li[i][j]
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]

        if(nx < 0 or nx >=len(map_li) or ny <0 or ny>=len(map_li)):
            continue

        if(height > map_li[nx][ny]):
            checkLoad(map_li,nx,ny,sum+1, answer)
            answer.append(sum+1)
    return answer


def findXY(li):
    max_int = 0
    for i in range(len(li)):
        for j in range(len(li[0])):
            if(max_int < li[i][j]):
                max_int = li[i][j]

    answer_li =[]
    for i in range(len(li)):
        for j in range(len(li[0])):
            if(li[i][j] == max_int):
                k = [i,j]
                answer_li.append(k)
    return answer_li


T = int(input())
for case in range(1,T+1):
    N, K = map(int,input().split())
    map_li = [list(map(int,input().split())) for _ in range(N)]

    max_height_list = findXY(map_li)
    answer_list = []
    answer = 0
    for a in range(N):
        for b in range(N):
            for c in range(1,K+1):
                tmp = map_li[a][b]
                map_li[a][b]= tmp-c

                for el in max_height_list:
                    max_int = max(checkLoad(map_li,el[0],el[1],1,[1]))
                    if(answer < max_int):
                        answer = max_int

                map_li[a][b] = tmp


    print("#{} {}".format(case,answer))