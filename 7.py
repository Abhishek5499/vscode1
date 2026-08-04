for i in range(5):
      for j in range(i):
       print('*',end='')

      print('\n')    



n=5
for i in range(n):
    space = " "*i
    star = "*" *(n-i)

    print(space + star)   


letter ='ABCDE'

for i in range(1,6):
    for j in range(i):
        print(letter[j] ,end="")
    print()   
    

