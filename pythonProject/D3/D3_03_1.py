def oddRow(li, i, j, k, answer):
    if(j-k>=0 and j+k <= 99 and li[i][j-k] == li[i][j+k]):
        answer += 2
        return oddRow(li,i,j,k+1,answer)
    else:
        return answer

def oddCol(li,i,j,k,answer):
    if(i-k>=0 and i+k<=99 and li[i-k][j] == li[i+k][j]):
        answer +=2
        return oddCol(li,i,j,k+1,answer)
    else:
        return answer

def evenRow(li,i,j,k,answer):
    if(j-k >= 0 and j+k <= 98 and li[i][j-k] == li[i][j+k+1]):
        answer+=2
        return evenRow(li,i,j,k+1,answer)
    else:
        return answer
def evenCol(li,i,j,k,answer):
    if(i-k>=0 and i+k<=98 and li[i-k][j] == li[i+k+1][j]):
        answer+=2
        return evenCol(li,i,j,k+1,answer)
    else:
        return answer

N = 10
for case in range(N):
    T = int(input())
    li = [input() for i in range(100)]

    answer_list =[]

    max_int = 0
    for i in range(100):
        for j in range(100):
            if(max_int <= oddCol(li,i,j,1,1)):
                max_int = oddCol(li,i,j,1,1)
            if(max_int <= oddRow(li,i,j,1,1)):
                max_int = oddRow(li, i, j, 1, 1)
            if(max_int <= evenCol(li,i,j,0,0)):
                max_int = evenCol(li, i, j, 0, 0)
            if(max_int <= evenRow(li,i,j,0,0)):
                max_int = evenRow(li, i, j, 0, 0)

    print("#{} {}".format(T, max_int))