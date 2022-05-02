#User using Visual Studio Code
#User using Git feature from Visual Studio Code


#using_if_elif_conditional
num=int(input(' Enter a number (between 0..999)  :  '))
if num<0:
    print(' Invalid Entry . Valid Range is 0..999. ')
elif num<10:
    print(' -- Single Digit Number is Entered --')
elif num<100:
    print(' -- Double Digit Number is Entered --')
elif num<=999:
    print(' -- Triple Digit Number is Entered --')
else:
    print(' Invalid Entry . Valid Range is 0..999. ')

