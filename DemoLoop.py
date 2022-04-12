#DemoLoop.py

from ast import Continue


value = 5 
while value > 0:
    print(value)
    value -= 1

print("전체코드실행종료")

#반복구무능ㄹ 원하는만큼

for i in range(5):
    print(i)

lst = ["apple", 100, 3.14]
for item in lst:
    print(item, type(item))


#구구단 출력
for i in [2,3,4,5,6]:
    print("---{0}단---".format(i))
    for j in [1,2,3,4,5,6,7,8,9]:
        print("{0}*{1}={2}".format(i,j,i*j))



lst =[1,2,3,4,5,6,7,8,9,10]
for i in lst:
    if i > 5:
        break
    print("Item:{0}".format(i))

print("---conticue---")
for i in lst:
    if i % 2 == 0:
        continue
    print("Item:{0}".format(i))    


