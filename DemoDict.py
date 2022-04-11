# DemoDict.py

from turtle import color


a=(1,2,3)
b=list(a)
print(b)
b.append(4)
print(b)

#e딕셔너리 연습
color ={"apple":"red","banana":"yellow"}
print(type(color))
print(color["apple"])

device = {"아이폰":5, "아이패드":10, "윈도우":20}
print(device["아이폰"])

device["맥북"]=15

device["아이폰"]=6

for item in device.items():
    print(item)