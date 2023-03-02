N ,M, K = map(int,input().split())

li = [list(map(int,input().split())) for _ in range(N)]
qli = [list(map(int,input().split())) for _ in range(K)]

print(li)

for i in range(len(qli)):
    for j in range(2):
        qli[i][j]-=1

print(qli)


seq_li =[]
for i in range(qli[0][0]-qli[0][2],qli[0][0]+qli[0][2]+1):
    tmp = []
    for j in range(qli[0][1]-qli[0][2],qli[0][1]+qli[0][2]+1):
        tmp.append(li[i][j])
    seq_li.append(tmp)


print(seq_li)


dx = [0,1,0,-1]
dy = [1,0,-1,0]
nx=0
ny=0
answer=[]

for i in range(4):
    for j in range(4):
        nx+=dx[i%4]
        ny+=dy[i%4]
        print(nx, ny)
        answer.append(seq_li[nx][ny])

nx+=1
ny+=1

for i in range(4):
    for j in range(2):
        nx+=dx[i%4]
        ny+=dy[i%4]
        print(nx, ny)
        answer.append(seq_li[nx][ny])

print(answer)
tmp = answer.pop()
answer.insert(0,tmp)
print(answer)