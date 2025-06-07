# str = input()
# n=0
# for i in str:
#     if i =='a' or i == 'e' or i == 'i' or i == 'o' or i =='u':
#         n = n + 1
# print(n)
"""
【问题描述】水仙花数是一个3位数，它的每位数字的3次幂之和等于它本身。例如：153是水仙花数。（1^3 + 5^3+ 3^3= 153）

【输入形式】一个3位整数
【输出形式】xxx是水仙花数 / xxx不是水仙花数
【样例输入】153
【样例输出】153是水仙花数

【样例输入】133
【样例输出】133不是水仙花数
"""
num = eval(input())
a = num // 100
b = num // 100 % 10
c = num % 10

if a ** 3 and b ** 3 and c ** 3 == num:
    print("{}是水仙花数".format(num))
else:
    print("{}不是水仙花数".format(num))