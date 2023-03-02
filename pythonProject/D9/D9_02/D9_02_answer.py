T = int(input())
def search(i,pr_li,day_li,answer,sum):
    if(i ==12):
        answer.append(sum)
        return sum
    m_day = pr_li[0] *day_li[i]
    m_month = pr_li[1]
    mm = min(m_day,m_month)
    search(i+1,pr_li,day_li,answer,sum+mm)
    if(i<10):
        search(i+3,pr_li,day_li,answer,sum+pr_li[2])
    return sum


for case in range(1,T+1):
    pr_li = list(map(int,input().split()))
    day_li = list(map(int,input().split()))
    answer = [pr_li[3]]
    search(0,pr_li,day_li,answer,0)
    print("#{} {}".format(case,min(answer)))



