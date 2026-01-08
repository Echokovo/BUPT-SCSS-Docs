import hashlib

dic = ""  # 遍历表
# dic += "0123456789"
dic += "QWERTYUIOPASDFGHJKLZXCVBNM"
dic += "qwertyuiopasdfghjklzxcvbnm"


target = \
"a35406b8720479039b686e4fa344875a"  # 目标 md5 值

for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                t = str(a) + str(b) + str(c) +str(d)
                hash = hashlib.md5(t.encode(encoding='UTF-8')).hexdigest()
                if hash[:len(target)] == target.lower():
                    print(t)
                    break