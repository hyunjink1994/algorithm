li = list(str(i) for i in range(10))

print("li :",li)
print("list(zip(li) : ",list(zip(li)))
print("list(zip(*li) : ",list(zip(*li)))
print("list(map(list, zip(li))) : ",list(map(list, zip(li, li[::-1]))))
print("list(map(list, zip(*li))) : ",list(map(list, zip(*li,*li))))


li2 = [list(i*j for i in range(10)) for j in range(10)]

print("li2 : ",li2)

print("list(zip(*li2)) :",list(zip(*li2)))
print("li2 : ",li2)
print("list(map(list, zip(*li2)))[::-1] ",list(map(list, zip(*li2)))[::-1])
print("li[::-1] ",li[::-1])
print("list(map(list, zip(*li[::-1]))) " ,list(map(list, zip(*li[::-1]))))