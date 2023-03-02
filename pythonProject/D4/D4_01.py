def pow (a,b):
    if(b == 0 ):
        return 1
    return a*pow(a,b-1)
N=10
for case in range(N):
    T=int(input())
    a,b = map(int,input().split())
    print("#{} {}".format(T,pow(a,b)))