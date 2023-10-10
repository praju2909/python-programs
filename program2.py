# pattern print
num_row= 5
for i in range(0,num_row):
    for j in range(i+1):
        print("*",end="")
    print()
print()
#
num_row= 5
for i in range(0,num_row):
    for j in range(num_row,i,-1):
        print("*",end="")
    print()
print()
#
n= 5
for i in range(n):
    for j in range(i+1):
        print("",end=' ')
    for j in range(i,n):
        print("*",end="")
    print()
print()
#
n= 5
for i in range(n):
    for j in range(i,n):
        print("",end=' ')
    for j in range(i+1):
        print("*",end="")
    print()
print()
#
n= 6
for i in range(n):
    for j in range(i,n):
        print("",end=' ')
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
print()
#
n= 6
for i in range(n):
    for j in range(i+1):
        print("",end=' ')
    for j in range(i,n-1):
        print("*",end="")
    for j in range(i,n):
        print("*",end="")
    print()
print()
#number pattern
n=6
k=1
for i in range (n):
    for j in range(i+1):
        print("", end="")
    for j in range (i,n-1):
        print(k,end="")
    for j in range(i,n):
        print(k,end="")
    k+=1
    print()
#
n=6
k=1
for i in range (n):
    for j in range(i,n):
        print("", end="")
    for j in range (i):
        print(k,end="")
    for j in range(i+1):
        print(k,end="")
    k+=1
    print()
print()
#
num_row=5
k=1
for i in range(0,num_row):
    for j in range(i+1):
        print(k,end="")
    k+=1
    print()
print()
#num_row=5
k=1
for i in range(0,num_row):
    for j in range(num_row,i,-1):
        print(k,end="")
    k+=1
    print()
print()
#
n=5
k=1
for i in range(n):
    for j in range(i,n):
        print('',end=' ')
    for j in range(i+1):
        print(k,end='')
    k+=1
    print()
print()
#
n=5
k=1
for i in range(n):
    for j in range(i+1):
        print('',end=' ')
    for j in range(i,n):
        print(k,end='')
    k+=1
    print()
print()