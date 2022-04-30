#User using Visual Studio Code
#User using Git feature from Visual Studio Code


tp1 = (3, 4, 1, 5, 8, 2)
lit2 = list(tp1)
ln3 = len(lit2)
for h1 in range(ln3):
    for h2 in range(ln3):   
        if(lit2[h1]<lit2[h2]):
            temp = lit2[h1]
            lit2[h1] = lit2[h2]
            lit2[h2] = temp
tp1 = tuple(lit2)
print("Output of tuple to list approach : {}".format(tp1))
