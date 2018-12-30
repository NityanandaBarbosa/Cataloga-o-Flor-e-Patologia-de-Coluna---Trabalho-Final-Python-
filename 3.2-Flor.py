import random
from time import sleep
import os

def proc(n):
    arquivo = open('iris.dat', 'r')
    geral = []
    ivirgi = []
    ivers = []
    iset = []
    global porcentagem
    global cporcent
    global k
    for i in arquivo:
        info = i.split(',')
        contagem = 0
        x = []
        dist = []
        for i in info:
            if contagem <= 3:
                i = float(i)
                x.append(i)
                if contagem == 3:
                    for j in range(4):
                        n=(usuario[j]-x[j])**2
                        dist.append(n)
                    n1=0
                    n2=0
                    for x in dist:
                        n1+=x
                    n2=n1**(1/2)
                    geral.append(n2)
            if contagem == 4:
                if (i == 'Iris-virginica\n'):
                    ivirgi.append(n2)
                elif (i == 'Iris-setosa\n'):
                    iset.append(n2)
                elif (i == 'Iris-versicolor\n'):
                    ivers.append(n2)
            contagem += 1
    geral = sorted(geral)
    ivirgi = sorted(ivirgi)
    ivers = sorted(ivers)
    iset = sorted(iset)
    SIvirg = 0
    SIvers = 0
    SIset = 0

    while(k-1 >= len(geral)):
        print('k extrapola o o número de amostras')
        k=int(input('Valores de k na checagem\n'))

    for i in range(k):
        if geral[i] in ivirgi:
            SIvirg += 1
        elif geral[i] in ivers:
              SIvers += 1
        elif geral[i] in iset:
            SIset += 1
    check2=[]
    if SIvirg >= SIvers:
        if SIvirg>=SIset:
            check2.append('Iris-virginica\n')
    if SIvers >= SIvirg:
        if SIvers>= SIset:
            check2.append('Iris-versicolor\n')
    if SIset >= SIvirg:
        if SIset>=SIvers:
            check2.append('Iris-setosa\n')

    provacheck=[]
    provacheck.append(random.choice(check2))
    if escolha <= 2:
        print('Os dados da flor inserida, mostram que ela é :',random.choice(provacheck))
    if escolha==3:
        if usuario[4] in provacheck:
            porcentagem+=1
        cporcent += 1
    arquivo.close()

escolha = 0
while(escolha!=4):
    k=0
    print('1-Usuario da informações em um única linha\n2-Usuario  da informações de cada vez\n3-Calibragem\n4-Sair\n')
    escolha=int(input('Digite a opção\n'))

    if(escolha==1):
        usuario = []
        x=input('Insira as informações da flor\n')
        x=x.split(',')
        k=int(input('Valores de k na checagem\n'))
        for i in x:
            a=float(i)
            usuario.append(a)
        proc(k)
    if(escolha==2):
        usuario = []
        k=int(input('Valores de k na checagem\n'))
        for i in range(4):
            a = float(input('Insira os dados\n'))
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
            info = i.split(',')
            contagem = 0
            usuario = []
            tamanho+=1
            for i in info:
                if contagem <= 3:
                    i = float(i)
                    usuario.append(i)
                if contagem == 4:
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