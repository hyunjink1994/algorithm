r,c,k = map(int, input().split())
li= []
for i in range(3):
    li.append(list(map(int,input().split())))


# clock_list = list(map(list, zip(*li)))[::-1]

# reverse_clock_list = list(map(list, zip(*li[::-1])))

#stack, que

#dfs, bfs

# data sturucture


for i in range(k):
    li = list(map(list, zip(*li[::-1])))


print(li)