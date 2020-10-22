import os
with open('test.txt',encoding='utf-8',mode='wb') as f:
    f.write('a')
    print(f.tell())
    # f.seek(-1 ,os.SEEK_END)
    # print(f.tell())