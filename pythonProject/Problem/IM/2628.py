R , C = map(int,input().split())
n = int(input())
li = [list(map(int,input().split())) for i in range(n)]

li_a = []
li_b = []
li_a.append(R)
li_b.append(C)
for i in range(n):
    if(li[i][0] == 0):
        li_b.append(li[i][1])
    else:
        li_a.append(li[i][1])
li_a.sort()
li_b.sort()
ans_a = []
ans_b = []
for i in range(len(li_a)-1):
    ans_a.append(li_a[i+1] - li_a[i])
for j in range(len(li_b)-1):
    ans_b.append(li_b[j+1] - li_b[j])
max_answer = 0
for i in range(len(ans_a)):
    for j in range(len(ans_b)):
        answer = ans_a[i]*ans_b[j]
        if(max_answer < answer):
            max_answer = answer
print(answer)
