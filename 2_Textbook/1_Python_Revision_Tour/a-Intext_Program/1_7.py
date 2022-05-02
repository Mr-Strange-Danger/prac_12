#User using Visual Studio Code
#User using Git feature from Visual Studio Code


#using_repeated_addition
num1,num2,prdt=int(input(' Enter first number   :  ')),int(input(' Enter second number  :  ')),0
cnt=num1
while cnt>0:
    cnt,prdt=cnt-1,prdt+num2
print(' The Product of',num1,'and',num2,'is',prdt)

