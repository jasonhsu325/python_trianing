#字串運算
s="hello"
print(s)
t="Hello" "World"
print(t)    #字串串接
r="Hello\nWorld"
print(r)    #\n換行
z="""Hello

World"""
print(z)    #"""  """直接換行
i="Hello"*3
print(i)    #字串重複

#字串會對內部的字元編號, 從0開始
o="hello"
print(o[0])
print(o[2])
print(o[1:4])  #取的子字串
print(o[1:])   #從1開始往後輸出
print(o[:4])   #除4以外輸出