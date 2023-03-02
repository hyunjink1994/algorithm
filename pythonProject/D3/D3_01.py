N=10
for test in range(N):
    T = int(input())
    instr = input()
    strli = input()

    answer = 0

    for i in range(len(strli)-len(instr)+1):
        if(instr == strli[i:len(instr)+i]):
            answer += 1

    print("#{} {}".format(T,answer))


