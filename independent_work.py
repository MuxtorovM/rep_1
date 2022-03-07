import random as r
answer = input('wanna play with me the game "guess number"?(y-yes/n-no)\n')
if answer == 'y':
    answer = input('so, I will guess your thougt number, are you ready?(y-yes/n-no)\n')
    if answer == 'y':
        a=1
        b=10
        value = ''
        while value != 'y':
            num = r.randint(a,b)
            value = input(f'is your thougt nuber  { str(num) } ?\nyes-y, greater than number-g, less than number-l\n')
            if value == 'g':
                b = num
            elif value == 'l':
                a = num
            else:
                break