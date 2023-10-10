for i in range(1,11):
    for j in range (1,11):
        print("%3d"%(i*j),end=" ")# this "%3d"% (i*j) is for space 3 digit number
    print(" ")
# even number one to hundred
start,end=1,100
print("even number")
for i in range(start,end+1):
    if i % 2==0:
        print(i, end=" ")
#
start,end=1,100
print("/n")
print("odd number")
for i in range (start,end+1):
    if i % 2 !=0:
        print(i,end=" ")
#print number divisible by 5&7 between 1 to 100
for i in range(1,1000):
    if i%5==0 and i%7==0:
        print(i)
# print number divisible by 5or7 between 1 to 100
for i in range(1,1000):
    if i%5==0 or i%7==0:
        print(i)
