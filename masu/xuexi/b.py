#1对应数/
for i in range(1000,2501):
    z = int(str(i)[::-1])
    if i * 4 == z:
        print(i)
        break
#2放射元素//
a = 234
b = 0
while a >=1:
    b +=1
    a /=2
print(b*26)
#3喝水
n = eval(input())
a = n
b = n
while b >=3:
    new = b // 3
    a +=new
    b = b % 3 + new
print(a)
#4水仙花数//
num = eval(input())
a = num / 100
b = num % 100 // 10
c = num % 10
if a ** 3+b ** 3+c ** 3==num:
    print("{}是水仙花数".format(num))
else:
    print("{}不是水仙花数".format(num))
#5函数字符串///
def count(string, c):
    count = 0
    for i in range(len(string)):
        if string[i] == c:
            count += i
    return  count

a = input()
b = input()
print(count(a,b))
#6兔子
n = eval(input())
if n == 1 or n == 2:
    print(1)
else:
    a,b=1,1
    for i in range(2,n):
        a,b=b,a+b
    print(b)
#7求高度//
s = 100
x = s / 2
for i in range(2,11):
    s = s + 2 * x
    x = x / 2
print('总路程:{:.2f},第十次高度:{:.2f}'.format(s,x))
#8铁球
PI = 3.1415926
r = eval(input())
print("%.2f %.2f"%(4*PI*r**2,4/3*PI*r**3*7.86))
#9素数
n = eval(input())
if n > 0:
    print("不是")
else:
    for i in range(2,(n**0.5)+1):
        if n % i == 0:
            print("不是")
            exit()
    print("是")
#10元音字母
str = input()
n = 0
for i in str:
    if i == 'a' or i == 'o' or i == 'e' or i == 'i' or i == 'u':
        n = n + 1
print(n)
#11逆序
n = int(input())
s = 0
while n > 0:
    s = s * 10 + n % 10
    n //= 10
print(s)
#1+2+3+4
a = 0
b = 0
c = int(input())
for i in range(6):
    a = a * 10 + c
    b = b + a
print(b)
#13
n = eval(input())
for i in range(n):
    if i % 7 != 0 and i % 3 == 0:
        print(i,end=' ')

