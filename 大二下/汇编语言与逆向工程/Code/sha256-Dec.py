import hashlib

dic = ""
# dic += "0123456789"
dic += "QWERTYUIOPASDFGHJKLZXCVBNM"
# dic += "qwertyuiopasdfghjklzxcvbnm"


target = \
"a3abe5e290d0bcc3c82ad572837b5d8d"  # 目标 sha256 值

for a in dic:
    for b in dic:
        for c in dic:
            for d in dic:
                t = str(a) + str(b) + str(c) +str(d)
                hash = hashlib.sha256(t.encode(encoding='UTF-8')).hexdigest()
                if hash[:len(target)] == target.lower():
                    print(t)
                    break