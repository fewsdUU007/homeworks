n = int(input())
otv=[]
p=''
for i in range(1,n):
    for j in range(i,n):
        if n%(i+j) == 0:
         otv.append(str(i)+str(j))
for i in range(len(otv)):
    p+=otv[i]
print(p)
