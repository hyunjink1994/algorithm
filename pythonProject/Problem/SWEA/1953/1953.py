# 첫 줄에 총 테스트 케이스의 개수 T가 주어진다.
#
# 두 번째 줄부터 T개의 테스트 케이스가 차례대로 주어진다.
#
# 각 테스트 케이스의 첫 줄에는 지하 터널 지도의 세로 크기 N, 가로 크기 M, 맨홀 뚜껑이 위치한장소의 세로 위치 R, 가로 위치 C, 그리고 탈출 후 소요된 시간 L 이 주어진다.
#
# 그 다음 N 줄에는 지하 터널 지도 정보가 주어지는데, 각 줄마다 M 개의 숫자가 주어진다.
#
# 숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미하며 숫자 0 은 터널이 없는 장소를 의미한다.

def checkpipe(map_li,i,j):
    if(map_li[i][j] != 0):
        return 1
    else:
        return 0

def move(map_li,i,j,count,start,answer):










    return


def pipe(pipe):
    if(pipe == 1):
        return
    if(pipe == 2):
        return
    if(pipe == 3):
        return
    if(pipe == 4):
        return
    if(pipe == 5):
        return
    if(pipe == 6):
        return
    if(pipe == 7):
        return














T = int(input())

for case in range(1,T+1):
    N,M,R,C,L = map(int,input().split())
    hole_loca = [R,C]
    map_li = [list(map(int,input().split())) for _ in range(N)]

    print(N,M,R,C,L)
    print(map_li)


