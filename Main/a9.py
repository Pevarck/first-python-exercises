number = int(input('\033[35mMe diga um número qualquer: '))
result = number % 2
if result == 0:
    print('\033[37mO número {} é \033[34mPAR'.format(number))
else:
    print('\033[37mO número {} é \033[34mÍMPAR'.format(number))