def paint5(li,i,j,N,M):
    li = uppaint(li,i,j,N,M)
    li = leftpaint(li,i,j,N,M)
    li = rightpaint(li,i,j,N,M)
    li = downpaint(li,i,j,N,M)
    return li
def leftpaint(li,i,j,N,M):
    for k in range(i-1,-1,-1):
        if(li[i][k] == 6):
            break
        else:
            li[i][k] = '#'
    return li
def rightpaint(li,i,j,N,M):
    for k in range(i+1,M):
        if(li[i][k] == 6):
            break
        else:
            li[i][k] = '#'
    return li
def uppaint(li,i,j,N,M):
    for k in range(j-1,-1,-1):
        if(li[k][j] == 6):
            break
        else :
            li[k][j] = '#'
    return li
def downpaint(li,i,j,N,M):
    for k in range(j+1,N):
        if(li[k][j] == 6):
            break
        else:
            li[k][j] = '#'
    return li
def countZero(li,i,j,N,M):
    countL = 0
    countR = 0
    countU = 0
    countD = 0

    for k in range(i-1,-1,-1):
        if(li[i][k] == 6):
            break
        else:
            countL+=1

    for k in range(i+1,M):
        if(li[i][k] == 6):
            break
        else:
            countR+=1

    for k in range(j-1,-1,-1):
        if(li[k][j] == 6):
            break
        else :
            countU+=1

    for k in range(j+1,N):
        if(li[k][j] == 6):
            break
        else:
            countD+=1

    return [countL,countR,countU,countD]



N,M = map(int,input().split())

li = [list(map(int,input().split())) for _ in range(N)]




for i in range(N):
    for j in range(M):
        if(li[i][j] == 5):
            li = paint5(li,i,j,N,M)
            print(countZero(li,i,j,N,M))

print(li)





