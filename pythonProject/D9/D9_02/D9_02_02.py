T = int(input())
# 0~11
def search(i,pr_li,day_li,answer,sum):
    print("----------------------------module start : {} ----------------------------".format(i+1))
    if(i ==12):
        print("----------------------------sum : {} ----------------------------".format(sum))
        answer.append(sum)
        return sum
    m_day = pr_li[0] *day_li[i]
    m_month = pr_li[1]
    mm = min(m_day,m_month)
    print("----------------------------month start: {}--------------------".format(i+1))
    # print("mm :",mm,end='\t')
    # print("sum : ",sum)
    search(i+1,pr_li,day_li,answer,sum+mm)
    mm = min(m_day,m_month)
    print("----------------------------month end : {}--------------------".format(i+1))
    if(i<10):
        print("----------------------------quarter start: {}--------------------".format(i+1))
        # print("mm :",mm,end='\t')
        # print("sum : ",sum)
        search(i+3,pr_li,day_li,answer,sum+pr_li[2])
        print("----------------------------quarter end : {}--------------------".format(i+1))
    print("----------------------------module end : {}--------------------".format(i+1))
    return sum

for case in range(1,T+1):
    pr_li = list(map(int,input().split()))
    day_li = list(map(int,input().split()))
    answer = [pr_li[3]]
    search(0,pr_li,day_li,answer,0)
    print("#{} {}".format(case,min(answer)))



