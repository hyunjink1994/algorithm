li = [list(map(int, input().split())) for i in range(4)]

paper = [[0 for i in range(100)] for i in range(100)]
answer = 0

for t in range(len(li)):
    for i in range(li[t][0],li[t][2]):
        for j in range(li[t][1],li[t][3]):
            paper[i][j] = 1

for a in range(len(paper)):
    for b in range(len(paper)):
        answer = answer+paper[a][b]

print(answer)

