def makecurvelist(curve, i):
    answer = []
    for j in range(curve[i][3] + 1):
        if (j == 0):
            answer.append(curve[i][2])
        else:
            li_a = answer[::-1]
            for k in range(len(li_a)):
                li_a[k] += 1
                li_a[k] %= 4
            answer = answer + li_a
    return answer

def canvasC(curve,canvas,answer,i):
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]
    X = curve[i][0]
    Y = curve[i][1]
    canvas[X][Y] = 1
    for j in range(len(answer)):
        X += dx[answer[j]]
        Y += dy[answer[j]]
        canvas[X][Y] =1
    return canvas

def checkSqr(canvas):
    count = 0
    for i in range(len(canvas) - 1):
        for j in range(len(canvas) - 1):
            if (canvas[i][j] == 1 and
                    canvas[i + 1][j] == 1 and
                    canvas[i][j + 1] == 1 and
                    canvas[i + 1][j + 1] == 1):
                count += 1
    return count


N = int(input())
curve = [list(map(int, input().split())) for _ in range(N)]
curve_li = []
canvas = [[0 for _ in range(100)] for _ in range(100)]

for i in range(N):
    canvasC(curve,canvas,makecurvelist(curve,i),i)

print(checkSqr(canvas))

