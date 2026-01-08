s = ""  # 待解密字符串 
ans = ""
a = 21
b = 7
MOD = 26
for i in range(len(s)):
    x = (a * (ord(s[i]) - b)) % MOD
    ans += chr(x)
print(ans)