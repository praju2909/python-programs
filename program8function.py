#WAP a program to create a function that takes two arguments, name and age , and print their values 
def sample(name,age):
    print(name, age )

sample(name='sara',age=20)
#WAP a program to create function func1() to accept a variable length and print their value.
def func1(*args):
    for i in args:
        print(i)
func1(20,40,60)
func1(80,100)
#WAP to create function calculation( ) such that it can accept two variables and calculate addition and substraction .
#also, it must return both addition and substraction in a single return call .
def calculation(a,b):#solution 1
    addition = a+b
    substraction = a-b
    return addition,substraction
res= calculation(40,10)
print(res)
def calculation(a,b):#solution2
    return a+b,a-b
res=calculation(40,10)
print(res)