# DemoList.py

from re import A


colors = ["red","blue","green"]

print(len(colors))
print(colors)
print(colors[0])
print(type(colors))

#디버깅(코드를 검사할 때)
#중단점(Break Point)를 먼저 지정
#Step By Step(F11)
for item in colors:
    print(item)

colors.append("white")
colors.append("pink")
print(colors)
colors.insert(1,"yellow")
print(colors)
print(colors.index("blue"))
print(colors.count("red"))

colors += ["red"]
print(colors)
colors += "red"
print(colors)

#set를 연습
a={1,2,3,3}
b={3,4,4,5}
print(a)
print(b)
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))

tp=(1,2,3)
print(tp)
print(type(tp))
print(len(tp))
print(tp[0])

#함수정의 (*보통은 하나의 값을 리턴)
def calc(a,b):
    return a+b, a*b

print(calc(3,4))

