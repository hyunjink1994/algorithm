T = int(input())

for test in range(T):
    num, change = map(int,input().split())
    exchange = change

    #자리수 구하고 --> 최대값 만들고 --> 몇번남았는지 %2 로 구함

    num_str = str(num)
    share = len(num_str)
    num_li = [int(num_str[i]) for i in range(len(num_str))]

    answer = []

    for i in range(change):
        max_index = num_li.index(max(num_li))
        if(max_index == 0 and len(num_li) >2):
            answer.append(num_li.pop(0))
            change+=1
        if(max_index != 0 ):
            tmp = num_li[0]
            num_li[0] = max(num_li)
            num_li[max_index] = tmp
            exchange-=1
        if(len(num_li) > 2):
            answer.append(num_li.pop(0))
        else:
            break


    if(exchange%2 == 1):
        tmp = num_li[-1]
        num_li[-1] = num_li[-2]
        num_li[-2] = tmp
        for i in range(len(num_li)):
            answer.append((num_li.pop(0)))

    else:
        for i in range(len(num_li)):
            answer.append(num_li.pop(0))

    print(answer)