#User using Visual Studio Code
#User using Git feature from Visual Studio Code


#using_net_if_statement
num=int(input(' Enter a number (between 0..999)  :  '))
if num<0 or num>999:
    print(' Invalid Entry . Valid Range is 0..999. ')
else:
    if num<10:
        print(' -- Single Digit Number is Entered --')
    else:
        if num<100:
            print(' -- Double Digit Number is Entered --')
        else:
            if num<=999:
                print(' -- Triple Digit Number is Entered --')
    
    
