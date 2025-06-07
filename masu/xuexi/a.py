#1
"""salary=list(map(int,input("").split(' ')))
ave=sum(salary)/10
print("%.2f"%ave)
#print("低于平均工资的员工为：")
for i in range(0,10):
        if (salary[i]<ave):
                print("%d %d"%(i+1,salary[i]))"""
#2兔子
"""n = int(input())
if n==1 or n==2:
    print(1)
else:
    a,b =1,1
    for i in range(2,n):
        a,b =b,a+b
    print(b)"""
#3字符转数字assmll3
"""s = input("")
ls = []
for c in s:
    ls.append(str(ord(c)))
print(",".join(ls))"""
#4字符串重复4
"""list1=list(eval(input()))
for i in list1:
        if list1.count(i)>=2:
                print('yes')
                break;
else:print('no')"""

"""list1=list(eval(input()))
for i in list1:
    if list1.count(i)>=2:
        print(1)
        break"""
#5工作时间
"""num = input()
x=eval(input())
s=3000
if x<88:
        s=x*20
elif x>176:
        s +=(176*20+(x-176)*20*1.3)
else:
        s+=x*20
print(s)"""
#6圆的面积体积
"""PI = 3.1415926
r,h = eval(input())
print("%.2f %.2f"%(2*PI*r**2+2*PI*r*h,PI*r**2*h))"""
#7不能被7整除和被3正常的数
"""n = eval(input())
for i in range(n):
    if i % 7 !=0 and i %3==0:
        print(i,end=' ')"""
#8实数输出整数和小数8
"""n = eval(input())
a = int(n)
b =round(n - a,2)
print(a,format(b,'.2f'))"""
#9水三瓶空换一瓶
"""n = eval(input())
total = n
empty = n

while empty >=3:
    new = empty // 3
    total += new
    empty = empty % 3 +new
print(total)"""
#10判断闰年
"""year = int(input())
if(year % 400 == 0) or (year % 4== 0 and year % 100 !=0):
    print('YES')
else:
    print('NO')"""
#11找对应数
"""if __name__ == '__main__':
    for i in range(2000,2501):
        z = int(str(i)[::-1])
        if z == i *4:```````
            print(i)
            break"""
#12一元二次方程的根
"""a,b,c = map(float,input().split(','))
d = b ** 2 - 4 * a * c
if d > 0:
    root1 = (-b + d ** 0.5) / (2 * a)
    root2 = (-b - d ** 0.5) / (2 * a)
    if root1 < root2:
       root1,root2=root2,root1
    print("{0:.2f} {1:.2f}".format(root1,root2))
else:
    print("NO")"""
#13逆序
"""n = int(input())
m=n
s=0
while n !=0:
    s = s * 10 + n % 10
    n //= 10
print(s)"""
#14函数 s(n)=1+2+3+4+n
def sum(n):
    s=0
    for i in range(n+1):
        s +=i
    return s
n =int(input())
print(sum(n))
#15三个数比大小
"""a,b,c = eval(input())
max_num = max(a,b,c)
min_num = min(a,b,c)
print(f"{max_num} {min_num}")"""
#16键是否存在D = {"name":"zhangsan","sex":"M","address":"Nanjing","phone":"123456"}
"""D = {"name":"zhangsan","sex":"M","address":"Nanjing","phone":"123456"}
key = input()
if D.get(key) !=None:
    print(1)
else:
    print(0)"""
#17求s=a+aa+aaa+aaaa.....
"""t = 0
s = 0
a = int(input(''))
for i in range(6):
    t = t * 10 + a
    s = s + t
print(s)"""
#18铁球密度7.86
"""PI = 3.1415926
r = eval(input())
print("%.2f %.2f"%(4*PI*r**2,4/3*PI*r**3*7.86))"""
#19s=1*2*3*4*5......
"""if __name__ == '__main__':
    s = 0
    for i in range(1,98):
        s +=i * (i+1)*(i+2)
    print(s)"""
#20素数
n = int(input())
"""if n < 2:
    print("no")
else:
    for i in range(2,int(n**0.5)+1):
        if n % i ==0:
            print("NO")
            exit()
    print("YES")"""
#21成绩
"""score = int(input())
if score >100 or score<0:
    print("wrong score")
elif score>=90:
    print("优")
elif score>=80:
    print("良")
elif score>=70:
    print("中")
elif score>=60:
    print("及格")
else:
    print("不及格")"""
#22 函数
"""def count(string, c):
    count = 0
    for i in range(len(string)):
        if string[i] == c:
            count += i
    return count

a = input()
b = input()
print(count(a,b))"""
#23字符阿萨small
"""n =input().strip()
print(','.join(str(ord(c)) for c in n))"""
#24
"""s="学而时习之,不亦说乎?有朋自远方来,不亦乐乎?人不知而不愠,不亦君子乎?"
m = s.count(',')+s.count('?')
n = len(s)-m
print("汉字个数为{},标点符号个数{}。".format(n,m))"""
#25最大值，最小值的和排序
"""num = list(map(int,input().split(' ')))
print(max(num),min(num),sum(num))
print(sorted(num))"""
#26元音字母个数
"""str = input()
n=0
for i in str:
    if i =='a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
        n = n + 1
print(n)"""
