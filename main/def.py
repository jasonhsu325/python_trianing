#定義函式
from tkinter import N


def multiply(n1,n2): #若沒有呼叫,就不會執行
    print(n1*n2)
    return 10 #回傳的數值
#呼叫函式
multiply(3,4)
multiply(10,8)
#回傳值
value=multiply(3,4)
print(value)

#函式可用來做程式的包裝:同樣的邏輯可以重複利用
def calculate(max):
    sum=0
    for x in range(1,max+1):
        sum=sum+x
    print(sum)

calculate(10)
calculate(20)