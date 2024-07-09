#Program to swap the value of 2 variable without using any 3 variable
"""a= 23
b= 24
c=21"""
"""a ^=b # a=a+b 
b ^=a #b=a-b
a ^=b #a=a-b
print(a)
print(b)
#with using 3 variable
x=23
y=56
z=x
x=y
y=z
print(x)
print(y)"""
#swap three numbers
"""a=a+b+c
b=a-(b+c)
c=a-(b+c)
a=a-(b+c)
print(a)
print(b)
print(c)"""
#sum of integer
"""a=12
b=13
print(a+b)"""
#Product of integer
"""a=2
b=3
print(a*b)"""
#Reverse of a number
"""a= 123434
c=0
while a>0:
 b=a%10
 c=c*10+b
 a=a//10
print(c)"""
#Sum
"""num=234 
Sum = sum(int(digit) for digit in str(num))
print(Sum)
or 
while a>0:
 b=a%10
sum=sum+b
a=a//10"""
#product
"""num = 234
product = 1
while (num != 0): 
        product = product * (num % 10) 
        num = num // 10
print(product)"""
#Palindrome
"""a=int(input())
t=a
c=0
while a>0:
    b=a%10
    c=c*10+b
    a=a//10
if(t==c):
    print("palindrome")
else:
    print("  notpalindrome")"""
#spy
"""a=int(input())
t=a
sum=0
while a>0:
    b=a%10
    sum=sum+b
    a=a//10
product = 1

while t> 0: 
        product = product * (t % 10) 
        t = t // 10
if(sum==product):
     print("spy")
else:
     print("not spy")"""
#armstrong
"""num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")"""
#even odd
"""n = int(input("Enter a number: "))
if(n%2==0):
    print("even")
else:
    print("odd")"""
#leap year
"""n = int(input("Enter a number: "))
if(n%400==0):
    print("leap year")
elif(n%4==0 and n%100 !=0):
    print("leap year")
else:
    print("not a leap year")"""



     


