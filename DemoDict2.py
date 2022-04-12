#DemoDict2.py

from re import A


phone={"kim":"1111","lee":"2222"}
print("kim" in phone)
print("kang" not in phone)
p=phone
print(id(phone),id(p))


#깊은복사
a = [100,200,300]
b = a[:]
a[0]=101
print(a)
print(b)
print(id(a),id(b))