import itertools
import psutil

T = int(input())

for case in range(1,T+1):
    N = int(input())
    cal_li = list(map(int,input().split()))
    num_li = list(map(int,input().split()))
    plie = []
    for i in range(len(cal_li)):
        for j in range(cal_li[i]):
            plie.append(i)

    pli = list(itertools.permutations(plie,len(plie)))
    pli = list(set(pli))

    answer_min = int(2**24)
    answer_max = 0
    for i in range(len(pli)):
        stack = []
        stack.append(num_li[0])
        for j in range(len(pli[i])):
            stack.append(num_li[j+1])
            b = stack.pop()
            a = stack.pop()
            if(pli[i][j] ==0):
                c = a+b
                stack.append(c)
            elif(pli[i][j] ==1):
                c = a-b
                stack.append(c)
            elif(pli[i][j] ==2):
                c = a*b
                stack.append(c)
            elif(pli[i][j] ==3):
                c = int(a/b)
                stack.append(c)
        if(stack[0] >= answer_max):
            answer_max = stack[0]
        elif(stack[0] <= answer_min):
            answer_min = stack[0]

    print("#{} {}".format(case,answer_max-answer_min))
print(psutil.virtual_memory())