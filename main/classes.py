#定義類別,與類別屬性
#定義一個類別IO,有兩個屬性 supportedSrcs和read
class IO:
    supportedSrcs=["console","file"]
    def read(src):
        if src not in IO.supportedSrcs:
            print("Not supported")
        else:
            print("Read from",src)
#適用類別
print(IO.supportedSrcs)
IO.read("file")
IO.read("internet")