import sys
sys.setrecursionlimit(10**7)


def checkLoad(map_li, i,j, sum, answer):
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    height = map_li[i][j]
    for k in range(4):
        nx = i+dx[k]
        ny = j+dy[k]

        if(nx < 0 or nx >=len(map_li) or ny <0 or ny>=len(map_li)):
            continue

        if(height  ==  map_li[nx][ny]-1):
            checkLoad(map_li,nx,ny,sum+1, answer)
            answer.append(sum+1)
    return answer


def findIndex(check_list,N):
    max_int = max(check_list)
    answer = []
    for i in range(len(check_list)):
        if(max_int == check_list[i]):
            a = int(i/N)
            b = int(i%N)
            answer.append([a,b])
    return answer

T = int(input())
for case in range(1,T+1):
    N = int(input())
    map_li = [list(map(int,input().split())) for _ in range(N)]

    check_list = []
    for i in range(N):
        for j in range(N):
            check_list.append(max(checkLoad(map_li,i,j,1,[1])))
    index = []
    for i in findIndex(check_list,N):
        index.append(map_li[i[0]][i[1]])

    print("#{} {} {}".format(case, min(index),max(check_list)))