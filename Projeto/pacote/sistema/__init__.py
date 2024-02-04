from pacote.interface import *


def ArquivoExiste(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except:
        arq = open(arquivo, 'wt+')
        print(f'\033[1;32m{arquivo} criado com sucesso\033[m')    
    finally:
        arq.close()
        

def CriarRegistro(arquivo, nome='<desconhecido>', produto='<desconhecido>', valor=''):
    try:
        arq = open(arquivo, 'at')
    except:
        print('\033[1;31mERRO! ao adicionar os dados, reinicie o programa e tente novamente\033[m')
    else:
        try:
            arq.write(f'{nome};{produto};{valor}\n')
        except:
            print('\033[1;31mERRO ao adicionar orçamento\033[m')
        else:
            print('\033[1;32mOrçamento adicionado com sucesso\033[m')
            arq.close()

    
def MostrarRegistros(arquivo):
    try:
        arq = open(arquivo, 'rt')
    except:
        print('\033[1;31mERRO ao abrir o arquivo, reinicie o programa e tente novamente\033[m')
    else:
        titulo('ORÇAMENTOS')
        print(f'{'Nº':<5}{'Nome':15}{'Prod.':15}{'Preço'}')
        for i, linha in enumerate(arq):
            dados = linha.split(';')
            dados[2] = dados[2].replace('\n', '')
            print(f'{i:<5}{dados[0]:15}{dados[1]:15}R${dados[2]}') 
        arq.close()


def ApagarDado(arquivo, cliente):
    try:
        arq = open(arquivo, 'r')
        dados = arq.readlines()
    except:
        print('\033[1;31mERRO ao abrir o arquivo, reinicie o programa e tente novamente\033[m')
    else:
        remover = ' '
        for i, l in enumerate(dados):
            if i == cliente:
                remover = l
                try:
                    dados = [dado for dado in dados if remover not in dado]
                except:
                    print('\033[1;31mERRO ao abrir o arquivo, reinicie o programa e tente novamente\033[m')
                else:
                    try:
                        arq = open(arquivo, 'w')
                        arq.writelines(dados)
                    except:
                        print('\033[1;31mERRO ao abrir o arquivo, reinicie o programa e tente novamente\033[m')
                    else:
                        print('\033[1;32mOrçamento excluido com sucesso\033[m')


    