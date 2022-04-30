#User using Visual Studio Code
#User using Git feature from Visual Studio Code


telebook={'Jivin':'85000-00003'}
for y1 in range(2):
    n7,p7=(str(input('Enter The Name  : '))),(str(input('Enter The Phone Number  : ')))
    telebook[n7]=p7
sh1=str(input('Name of th contact you want to find Phone Number  \n >>>  '))
print(telebook.get(sh1))
