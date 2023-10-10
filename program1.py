#WAP to find max number between two number
no1= 89
no2=95
if no1>no2:
    print(no1,"is maximum")
else:
    print(no2,"is maximum")
print()
# WAP to check if number is even or odd (use % method)
no= 87
if no%2==0:
    print(no,"is even")
else:
    print(no,"is odd")
print()
#WAP TO FIND YEAR IS LEAP YEAR  OR NOT (YEAR%4==0 AND YEAR%100!=0 OR YEAR%400==0)
year=2026
if year%4==0 and year%100!=0 or year%400==0:
    print(year,"is leap year")
else:
    print(year,"is not leap year")
print()
#WAP to find largest number of three number
a= 78
b= 45
c=984
if a>b and a>c:
    largest=a
if b>a and a>c:
    largest=b
if c>a and c>b:
    largest=c
    print(largest, "is largest number between three number")
print()
#WAP to iterate the first 10  number and in each iteration print the sum of current number and privious number
privious_num=0
for i in range(10):
    sum=privious_num+i
    privious_num=i
    print('current num',i, 'privious num',privious_num,'sum is:',sum)
