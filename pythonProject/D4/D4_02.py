def transfer(li):
    li_c = ['(', '[', '{', '<', '>', '}', ']', ')']
    answer_li = []
    for i in range(len(li)):
        for j in range(len(li_c)):
            if (li[i] == li_c[j]):
                answer_li.append(j)
    return answer_li


def program(li):
    for i in range(len(li) - 1):
        if (li[i] + li[i + 1] == 7):
            li.pop(i)
            li.pop(i)
            return program(li)
    return li


N = 10
for case in range(N):
    l = int(input())
    li = input()
    stack = transfer(li)
    answer = 0
    if (len(program(stack)) == 0):
        answer = 1
    print("#{} {}".format(case + 1, answer))
