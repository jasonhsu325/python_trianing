#集合的運算
s1={3,4,5}
print(10 not in s1)
s2={1,2,3}
s3={2,3,4,5,6}
s4=s2&s3 #&交集: 取兩個集合中相同的資料
print(s4)
s5=s2|s3 #|聯集: 取兩個集合中所有的資料, 但不重複取
print(s5)
s6=s3-s2 #-差集:從s3中減去和s2重複的部分
print(s6)
s7=s2^s3 #^反交集:取兩個集合中,不重疊的部分
print(s7)
s=set("Hello") #set(字串)
print(s) #把字串拆解成集合
print("H" in s)
print("a" in s)

#字典的運算
dic={"apple":"蘋果","bug":"蟲"}
print(dic["apple"])
dic["apple"]="小蘋果"
print(dic["apple"])
print("apple" in dic) #判斷key是否存在
print("taste" in dic)
del dic["apple"] #刪除字典中的健值對(key-value pair)
print(dic)
dic={x:x*3 for x in [3,4,5]}
print(dic)