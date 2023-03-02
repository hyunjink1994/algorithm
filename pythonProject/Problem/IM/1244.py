def switch(n):
    if n == 0 :
        return 1
    if n == 1 :
        return 0

L = int(input())
li = list(map(int,input().split()))
n = int(input())
stu = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    if(stu[i][0] == 1):
        for j in range(stu[i][1],L,stu[i][1]):
            li[j-1] = switch(li[j-1])
    if(stu[i][0] == 2):
        li[stu[i][1]-1] = switch(li[stu[i][1]-1])
        for k in range(1, int(L/2)):
            if stu[i][1] + k > L or stu[i][1] - k < 1 : break
            else:
                if(li[stu[i][1]-k-1] == li[stu[i][1]+k-1]):
                    li[stu[i][1]-k-1] = switch(li[stu[i][1]-k-1])
                    li[stu[i][1]+k-1] = switch(li[stu[i][1]+k-1])
                else:break
for i in range(len(li)):
    if(i%20 == 0):
        print()
    print(li[i],end=' ')


