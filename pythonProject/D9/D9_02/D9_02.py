T = int(input())

def search(i, sum, answer , pr_li, day_li):
    if(i ==12):
        return sum
    sum = pr_li[0] *day_li[i]

    return sum + search(i+1,sum,answer, pr_li, day_li)




def searchAns(i, sum, answer , pr_li, day_li):
    k = i
    if(i == 12):
        return sum
    print("i :", k)
    li = []
    daily = pr_li[0]*day_li[i]
    yearly = pr_li[3]
    monthly = pr_li[1]
    quartly = pr_li[2]

    mm = min(daily,monthly)

    searchAns(k+1,sum+mm, answer,pr_li,day_li)
    searchAns(k+3,sum+quartly,answer,pr_li,day_li)



    print("sum :",sum)

    return sum + searchAns(i+1,sum,answer, pr_li, day_li)





for case in range(1,T+1):
    pr_li = list(map(int,input().split()))
    day_li = list(map(int,input().split()))
    print(pr_li)
    print(day_li)
    print(searchAns(0,0,999999,pr_li,day_li))