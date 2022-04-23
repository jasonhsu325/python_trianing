#有序列可變動的列表 List
grade=[12,68,17,25,18]
print(grade)
print(grade[0])
print(grade[3])
grade[0]=55 #把55放到列表中的第一個位置
print(grade)
print(grade[1:4])
grade[1:4]=[] #連續刪除
print(grade)
grade=grade+[12,33] #列表串接
print(grade)
lenght=len(grade)
print(lenght) #取的列表的長度

data=[1,2,3],[4,5,6]
print(data[0][0])
data[0][0:2]=[3,3,3]
print(data[0])
#有序不可變動的列表 Tuple
data=(3,4,5)
print(data[0:2])
#操作與List一樣
data[0]=5 #錯誤: Tuple不可變動
print(data)