#break
n=0
while n<5:
    if n==3:
        break
    print(n)#印出迴圈中的n
    n=n+1
print("最後的n:",n)#印出迴圈結束的n

#continue
for x in [0,1,2,3]:
    if x%2==0:
        continue
    print(x)
    n=n+1
print("最後的n:",n)

#else
sum=0
for n in range(1,11):
    sum+=n
else:
    print(sum)

#綜合範例: 找出整數的平方根
n=int(input("輸入一個正整數:"))
for i in range(n):
    if i*i==n:
        print("整數平方根",i)
        break #用break強制結束,不會執行else
else:
    print("沒有整數平方根")

