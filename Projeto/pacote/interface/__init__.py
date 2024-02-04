def leiaint(n):
    while True:
        try:
            opcao = int(input(n))
        except:
            print('\033[1;31mERRO!, digite uma opção válida!\033[m')   
        else:
            return opcao


def leiadinheiro(msg):
    while True:
        leitor = str(input(msg)).replace(',', '.').strip()
        try:
            a = float(leitor)
        except:
            print('\033[1;31mINVÁLIDO!, digite um valor válido\033[m')
        else:
            return leitor


def linha():
    return print('='*80)


def titulo(msg):
    linha()
    print(f'{msg:^80}')
    linha()


def menu(lista):
    titulo('GESTÃO')
    for i, info in enumerate(lista):    
        print(f'{i+1} - {info}')
    linha()
    opc = leiaint('Opção: ')
    return opc