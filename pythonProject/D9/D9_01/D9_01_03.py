cal_modual = ['+','-','*','/']

def cal(a,b,modual):
    if(modual == 0):
        return a+b
    if(modual == 1):
        return a-b
    if(modual == 2):
        return a*b
    else:
        return int(a/b)


T = int(input())

for case in range(1,T+1):
    N = int(input())
    cal_li = list(map(int,input().split()))
    num_li = list(map(int,input().split()))
    print("cal_li :",cal_li)
    print("num_li :",num_li)
    start = num_li.pop(0)
    print("num_li :",num_li)

    # dfs(0,-987654321,987654321,start,cal_li)
