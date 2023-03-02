def move(li, i,j):
    li[i][j] = 0
    if(i == 0):
        return j
    elif(j>1 and li[i][j-1] == 1):
        return move(li,i,j-1)
    elif(j < 99 and li[i][j+1] == 1):
        return move(li,i,j+1)
    else:
        return move(li,i-1,j)
T = 10
for t_case in range(T):
    ladder = []
    n = int(input())
    ladder = [list(map(int,input().split())) for i in range(100)]
    goal = ladder[99].index(2)

    print("#{} {}".format(n , move(ladder,99,goal)))
