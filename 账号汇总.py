import os
# summary()方法是把云手机注册的txt文件汇总到一个文档里

def summary(read_path,write_path):   #第一个参数是云手机下载下来的N个文档路径，第二个是生成汇总文档放到那个文件里的路径
    files = os.listdir(read_path)
    a = 0
    for file in files:
        with open(read_path+"/"+file,encoding='utf-8', mode='r')as f:
            content = f.read()
            with open(write_path, encoding='utf-8', mode='a') as f_a:
                if a == 0:
                    f_a.write(content.strip())
                else:
                    f_a.write('\n'+content.strip())
        a+=1
    with open(write_path, encoding='utf-8', mode='r')as f_r:
        return '一共有%s个账号' %(len(f_r.readlines()))
print(summary(r'D:\Desktop\汇总',r'D:\Desktop\账号汇总.txt'))