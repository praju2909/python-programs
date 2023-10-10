num= int(input("enter the number:"))
def isprime(num):
    for n in range(2,int(num**0.5)+1):
        if num%n==0:
            return True
        return False
    print("this is prime number ",num,isprime(num))
print("this is not prime number ",num,isprime(num))

num=int(input("enter the number:"))
if num>1:
    for i in range(2,num):
        if (num%i)==0:
            print(num,"is not a prime number")
            print(i,"time",num//i,"is",num)
            break
        else:
            print(num,"is prime number")
else:
    print(num,"is not prime number")