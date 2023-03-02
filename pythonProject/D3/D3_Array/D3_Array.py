li = [list(map(int,input().split())) for i in range(5)]

li_s = []
# for i in range(len(li)):
#     for j in range(len(li[0])):
#         li_s.append(li[i][j])
# li_s = sorted(li_s)

print(li_s)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

pointX = 0
pointY = 0

for i in range(len(li)):
    for j in range(len(li[0])):
        print(li[pointX][pointY])

