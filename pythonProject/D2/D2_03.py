T = 10

for t_case in range(T):
    n = int(input())
    table = [list(map(int, input().split())) for i in range(n)]
    answer = 0

    for a in range(len(table)):
        t_col = [table[i][a] for i in range(100)]
        count = 0
        tmp = 0
        for i in range(len(t_col)):
            if(t_col[i] == 1):
                tmp = 1
            if(t_col[i] == 2 and tmp ==1):
                count = count +1
                tmp = 0

        answer = answer + count

    print("#{} {}".format(t_case+1, answer))
