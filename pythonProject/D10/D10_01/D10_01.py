# [제약 사항]
#
# 1. 시간 제한 : 최대 51개 테스트 케이스를 모두 통과하는 데 C/C++/Java 모두 3초
#
# 2. 지도의 한 변의 길이 N은 3 이상 8 이하의 정수이다. (3 ≤ N ≤ 8)
#
# 3. 최대 공사 가능 깊이 K는 1 이상 5 이하의 정수이다. (1 ≤ K ≤ 5)
#
# 4. 지도에 나타나는 지형의 높이는 1 이상 20 이하의 정수이다.
#
# 5. 지도에서 가장 높은 봉우리는 최대 5개이다.
#
# 6. 지형은 정수 단위로만 깎을 수 있다.
#
# 7. 필요한 경우 지형을 깎아 높이를 1보다 작게 만드는 것도 가능하다.

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

    # load_list = []
    # for i in range(N):
    #     part_list = []
    #     for j in range(N):
    #         load_max = max(checkLoad(map_li,i,j,1,[1]))
    #         part_list.append(load_max)
    #     load_list.append(part_list)
    # print(load_list)

    # for i in range(N):
    #     for j in range(N):
    #         for m in range(K):

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


    print(answer)