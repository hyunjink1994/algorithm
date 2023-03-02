N =10
for test in range(N):
    block = int(input())
    strli = [input() for i in range(8)]

    seg_block = int(block/2)
    count = 0

    for i in range(len(strli)):
        for j in range(len(strli)-block+1):
            test_li = strli[i][j:j+block]
            answer = 1
            for l in range(seg_block):
                if(test_li[l] == test_li[-l-1]):
                    answer*=1
                else:
                    answer*=0
            if(answer == 1):
                count+=1

    for i in range(len(strli)):
        for j in range(len(strli)-block+1):
            test_li = [strli[j+u][i] for u in range(block)]
            answer =1
            for l in range(seg_block):
                if(test_li[l] == test_li[-l-1]):
                    answer*=1
                else:
                    answer*=0
            if(answer == 1):
                count+=1

    print("#{} {}".format(test+1, count))