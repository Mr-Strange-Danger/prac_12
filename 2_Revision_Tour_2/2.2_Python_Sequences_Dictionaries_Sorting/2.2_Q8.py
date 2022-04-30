#User using Visual Studio Code
#User using Git feature from Visual Studio Code


telebook={'Jivin':'85000-00003'}
for ui in range(3):
    nm=str(input('Enter The Name  : '))
    ph=str(input('Enter The Phone Number  : '))
    telebook[nm]=ph
shnm=str(input('Name of th contact you want to find Phone Number : \n >>>  '))
print(telebook.get(shnm))