from pacote.interface import *
from pacote.sistema import *
from time import sleep


usuario = str(input('Nome do arquivo: ')).strip()
sleep(1)
arquivo = f'{usuario}.txt'
ArquivoExiste(arquivo)

escolhas = ['\033[1;33mCadastrar novo orçamentos\033[m', '\033[1;33mOrçamento\033[m', 
            '\033[1;33mEditar orçamentos\033[m', '\033[1;31mSair do sistema\033[m']
while True:
    escolha = menu(escolhas)
    sleep(1)
    if escolha == 1:
        titulo('NOVO ORÇAMENTO')
        nome = str(input('Identificação: ')).strip()
        produto = str(input('Produto vendido: '))
        valor = leiadinheiro('Valor: R$')
        CriarRegistro(arquivo, nome, produto, valor)
        sleep(1)
    elif escolha == 2:
        MostrarRegistros(arquivo)
        sleep(1)
    elif escolha == 3:
        titulo('EDITAR ORÇAMENTOS')
        try:
            cliente = leiaint('Qual orçamento deseja excluir (N. do orçamento): ')
            ApagarDado(arquivo, cliente)
            sleep(1)
        except:
            print('\033[1;31mERRO!, Orçamento não encontrado\033[m')
            sleep(1)
    elif escolha == 4:
        sleep(1)
        titulo('\033[1;31mSAINDO DO SISTEMA... ATE LOGO!\033[m')
        break
    else:
        titulo('\033[1;31mOPÇÃO NÃO ENCONTRADA!\033[m')
        sleep(1)