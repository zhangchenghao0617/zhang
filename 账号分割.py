import math
# separate()把存放有所有账号的文档，分成n个小文档，方便放到服务器，或者放到云手机上养号。
def separate(read_path,write_path,n):  #第一个参数是总文档的路径，第二个参数是把分成的小文档放到哪的路径；第三个参数是要分成多少个小文档
    with open(read_path,encoding='utf-8',mode='r')as f_r:
        lines = len(f_r.readlines())  #取整个文件的行数.
        f_r.seek(0)                   #光标到最开始
        a = 1
        for i in range(0,len(f_r.readlines()),math.ceil(lines/n)):
            f_r.seek(0)
            list = f_r.readlines()[i:i+math.ceil(lines/n)]
            b = 0
            for j in list:
                with open(write_path+"/"+'%s.txt' %(a), encoding='utf-8', mode='a')as f_a:
                    if b == 0:
                        f_a.write(j.strip())
                    else:
                        f_a.write('\n'+j.strip())
                    b+=1
            a+=1
    return '已经分割成%s个文件，每个文件%s个账号' %(n,math.ceil(lines/n))
print(separate(r'D:\Desktop\账号汇总.txt',r'D:\Desktop',4))