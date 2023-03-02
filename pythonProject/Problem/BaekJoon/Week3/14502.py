def factorial(n):
    if(n == 0):
        return 1
    else:
        return n*factorial(n-1)

N = int(input())
li = list(map(int,input().split()))
li_cal = list(map(int,input().split()))

div_case =1
for i in range(len(li_cal)):
    div_case*=factorial(li_cal[i])

case_l = factorial(sum(li_cal)) / div_case

calcul = ['+', '-','*','/']
answer_list = []

for j in range(case_l):
    tmp = li_cal
    tmp_list = []
    for k in range():

        def permutation(arr, r):
            # 1.
            arr = sorted(arr)
            used = [0 for _ in range(len(arr))]

            def generate(chosen, used):
                # 2.
                if len(chosen) == r:
                    print(chosen)
                    return

                for i in range(len(arr)):
                    # 3.
                    if not used[i] and (i == 0 or arr[i - 1] != arr[i] or used[i - 1]):
                        chosen.append(arr[i])
                        used[i] = 1
                        generate(chosen, used)
                        used[i] = 0
                        chosen.pop()

            generate([], used)
