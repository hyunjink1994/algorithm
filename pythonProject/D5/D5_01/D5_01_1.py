def transfer(li):
    stack = []
    answer = []
    switch = 0

    for i in range(len(li)):
        if(li[i] == '('):
            continue
        elif(li[i] == ')'):
            answer.append(stack.pop(-1))
        elif(li[i] == '+'):
            stack.append(li[i])
        elif(li[i] == '*'):
            stack.append(li[i])
            switch = 1
        elif(switch == 1):
            answer.append(li[i])
            answer.append(stack.pop(-1))
            switch = 0
        else:
            answer.append(li[i])
        # print("answer :", answer)
        # print("stack : ", stack , "switch :" ,switch)

    for j in range(len(stack)):
        answer.append(stack.pop(-1))
    return answer

N= 10
for case in range(N):
    L = int(input())
    li = input()

    answer = transfer(li)

    answer_str = ''.join(answer) # 스택을 통한 후위 연산법


    count_a =0
    count_b =0
    for i in range(len(answer)):
        if(answer[i] == '+' or answer[i] == '*'):
            count_a +=1
    stack_answer = []
    for i in range(len(answer)):
        if(answer[i] == '*'):
            a = stack_answer.pop(-1)
            b = stack_answer.pop(-1)
            inputNum = a*b
            stack_answer.append(inputNum)
        elif(answer[i] == '+'):
            a = stack_answer.pop(-1)
            b = stack_answer.pop(-1)
            inputNum = a + b
            stack_answer.append(inputNum)
        else:
            stack_answer.append(int(answer[i]))
    print(stack_answer)