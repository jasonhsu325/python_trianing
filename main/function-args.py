#多數的預設資料
def power(base,exp):
    print(base**exp)
power(3,2)
#使用參數名稱對應
def divide(n1,n2):
    print(n1/n2)
divide(n1=8,n2=4)
divide(n2=4,n1=2)
#無限(不定)參數資料
def avg(*ns):
    sum=0
    for n in ns:
        sum=sum+n
        print(sum/len(ns))
avg(3,4)
avg(57,68,27)
