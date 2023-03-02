def sum_max(arr, i):
    ans_ho = 0
    ans_ver = 0
    for j in range(100):
        ans_ho = ans_ho + arr[i][j]
    for k in range(100):
        ans_ver = ans_ver + arr[k][i]
    return max(ans_ver, ans_ho)


for t in range(10):
    CN = int(input())
    arr = [list(map(int, input().split())) for __ in range(100)]
    ans_arr = []
    ans_cro = 0
    ans_cro_re = 0
    for i in range(100):
        ans_arr.append(sum_max(arr, i))
        ans_cro = ans_cro + arr[i][i]
        ans_cro_re = ans_cro_re + arr[99 - i][i]
    ans_arr.append(ans_cro)
    ans_arr.append(ans_cro_re)
    print('#{0} {1}'.format(t + 1, max(ans_arr)))