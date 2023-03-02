def cal(li, answer, stack):
    for i in range(len(li)):
        if(li[i] == '('):
            stack.append(li[i])
        elif(li[i] == ')'):
            while(len(stack) != 0):
                if(stack[-1] == '('):
                    stack.pop()
                    break
                else:
                    answer.append(stack.pop())
        elif(li[i] == '*'):
            stack.append(li[i])
        elif(li[i] == '+'):
            while(len(stack) !=0):
                if(stack[-1] == '('):
                    break
                else :
                    answer.append(stack.pop())
            stack.append(li[i])
        else:
            answer.append(li[i])
    return answer

N= 10
for case in range(N):
    L = int(input())
    li = input()

    answer = cal(li,[],[])
    stack_answer = []


    for i in range(len(answer)):
        if(answer[i] == '*'):
            a = int(stack_answer.pop())
            b = int(stack_answer.pop())
            inputNum = a*b
            stack_answer.append(inputNum)
        elif(answer[i] == '+'):
            a = int(stack_answer.pop())
            b = int(stack_answer.pop())
            inputNum = a+b
            stack_answer.append(inputNum)
        else:
            stack_answer.append(int(answer[i]))
    print("#{} {}".format(case+1, stack_answer[0]))