#隨機模組
import random
#隨機選取
data=random.choice([1,5,8,6,3])
print(data)
data2=random.sample([5,7,6,2,8,5],3)
print(data2)
#隨機調換順序
data=[1,5,7,6,32]
random.shuffle(data)
print(data)
#隨機取的亂數
data=random.random()
print(data)
data=random.uniform(0.0,1.0) #0.0~1.0之間的隨機亂數
print(data)
#取的常態分配亂數
data=random.normalvariate(100,10) #平均數100,標準差10,得到的資料多在90~110之間
print(data)