#儲存檔案
file=open("data.txt",mode="w")#開啟
file.write("Hello File")#操作
file.close()#關閉
#測試中文
file=open("chinese",mode="w",encoding="utf8")
file.write("我要上清大工科")
file.close()
#最佳寫法
with open("test",mode="w",encoding="utf8") as file:
    file.write("python最讚")