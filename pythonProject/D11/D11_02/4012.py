import itertools

# pool = ['A', 'B', 'C']
# print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
# print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기
# print(list(map(''.join, itertools.combinations(pool,2)))) # 2개의 원소로 조합 만들기


T = int(input())
for case in range(1,T+1):
    N = int(input())
    table = [list(map(int,input().split())) for _ in range(N)]
    # 0, 1, 2, 3
    comb = [i for i in range(N)]
    comb_list = list(itertools.combinations(comb,int(N/2)))
    answer = []
    for i in range(len(comb_list)):
        m = list(comb_list[i])
        tmp = [i for i in range(N)]
        for j in range(int(N/2)):
            if(m[j] in tmp):
                tmp.remove(m[j])
        a_p = list(itertools.permutations(m,2))
        b_p = list(itertools.permutations(tmp,2))

        sumA = 0
        sumB = 0
        for k in range(len(a_p)):
            sumA += table[a_p[k][0]][a_p[k][1]]
            sumB += table[b_p[k][0]][b_p[k][1]]
        answer.append(abs(sumA-sumB))
    print("#{} {}".format(case,min(answer)))

