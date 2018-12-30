import random
from time import sleep
import os

def proc(n):
    arquivo = open('coluna_test.dat', 'r')
    geral = []
    DH = []
    SL = []
    NO = []
    global porcentagem
    global cporcent
    global k
    for i in arquivo:
        info = i.split(' ')
        contagem = 0
        x = []
        dist = []
        for i in info:
            if contagem <= 5:
                i = float(i)
                x.append(i)
                if contagem == 5:
                    for j in range(6):
                        n=(usuario[j]-x[j])**2
                        dist.append(n)
                    n1=0
                    n2=0
                    for x in dist:
                        n1+=x
                    n2=n1**(1/2)
                    geral.append(n2)
            if contagem == 6:
                if (i == 'DH\n'):
                    DH.append(n2)
                elif (i == 'SL\n'):
                    SL.append(n2)
                elif (i == 'NO\n'):
                    NO.append(n2)
            contagem += 1
    geral = sorted(geral)
    DH = sorted(DH)
    SL = sorted(SL)
    NO = sorted(NO)
    SIDH = 0
    SISL = 0
    SINO = 0

    while(k-1 >= len(geral)):
        print('k extrapola o o numero de amostras')
        k=int(input('Valores de k na checagem\n'))

    for i in range(k):
        if geral[i] in DH:
            SIDH += 1
        elif geral[i] in SL:
              SISL += 1
        elif geral[i] in NO:
            SINO += 1
    check2=[]
    if SIDH >= SISL:
        if SIDH>=SINO:
            check2.append('DH\n')
    if SISL >= SIDH:
        if SISL>= SINO:
            check2.append('SL\n')
    if SINO >= SIDH:
        if SINO>=SISL:
            check2.append('NO\n')

    provacheck=[]
    provacheck.append(random.choice(check2))

    if escolha <= 2:
        print('Os dados da paciente inseridos, mostram que ele(a) é :',random.choice(provacheck))
    if escolha==3:
        if usuario[6] in provacheck:
            porcentagem+=1
        cporcent += 1
    arquivo.close()

escolha = 0
while(escolha!=4):
    k=0
    print('1-Usuario da informações em um única linha\n2-Usuario  da informações de cada vez\n3-Calibragem\n4-Sair\n\n\nOBS:\nDH = Hérnia de Disco\nSL = Espondilolistese\nNO = Normal\n')
    escolha=int(input('Digite a opção\n'))

    if(escolha==1):
        usuario = []
        x=input('Insira as informações do paciente\n')
        x=x.split(' ')
        k=int(input('Valores de k na checagem\n'))
        for i in x:
            a=float(i)
            usuario.append(a)
        proc(k)
    if(escolha==2):
        usuario = []
        k=int(input('Valores de k na checagem\n'))
        for i in range(6):
            a = float(input('Insira as informações do paciente :\n'))
            usuario.append(a)
        proc(k)
    if(escolha==3):
        porcentagem = 0
        cporcent = 0
        tamanho=0
        nome=input('diga o nome do arquivo\n')
        arquivo1 = open(nome,'r')
        k=int(input('Valores de k na checagem\n'))
        for i in arquivo1:
            info = i.split(' ')
            contagem = 0
            usuario = []
            tamanho+=1
            for i in info:
                if contagem <= 5:
                    i = float(i)
                    usuario.append(i)
                if contagem == 6:
                    usuario.append(i)
                    proc(k)
                contagem += 1
        if tamanho==cporcent:
            porcent = porcentagem * 100 / cporcent
            print(f'A taxa de acerto foi de {porcent}%')
        arquivo1.close()
    if(escolha==4):
        sleep(1)
        print('O programa será encerrado, até a proxima.')
        sleep(1)
    sleep(2)
    os.system('clear')
