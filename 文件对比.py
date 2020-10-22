with open('../../Desktop/文件对比/tk.txt', encoding='utf-8') as f_tk,\
        open('../../Desktop/文件对比/zc.txt', encoding='utf-8') as f_zc,\
            open('../../Desktop/文件对比/没有TK.txt', encoding='utf-8', mode='a') as f_a:

    tk = f_tk.read()
    for line in f_zc.readlines():
        if line in tk:
            continue
        else:
            f_a.write(line)

