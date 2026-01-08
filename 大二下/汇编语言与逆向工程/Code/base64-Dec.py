import base64
s = "c2FkYXNmc2E="  # 待解密字符串
print(base64.b64decode(s).decode("utf-8"))