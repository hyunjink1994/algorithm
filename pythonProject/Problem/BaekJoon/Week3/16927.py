import math

def check (N, M, R, li):
    answer = (N>=2 and N<300)
    answer = answer * (M>=2 and M<300)
    answer = answer * (min(N,M) %2 ==0)
    answer = answer * (math.log(R) < 9 )
    answer = answer * (math.log(max(li)) < 8)

    return answer

N,M,R = map(int,input().split())

li = [list(map(int,input().split())) for i in range(N)]

print(check(N,M,R,li))