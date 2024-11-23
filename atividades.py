import time
from datetime import datetime

#1. Função: Saudação Escreva uma função chamada saudacao que receba um nome como argumento e imprima uma mensagem de boas-vindas.
print("Escreva uma função chamada saudacao que receba um nome como argumento e imprima uma mensagem de boas-vindas.")
time.sleep(3)

def saudação(nome):

    print("Boas-vindas "+ nome)

saudação(input("escreva seu nome: "))

#2. Função: Dobro de um Número Crie uma função que receba um número e retorne o dobro desse número.
print("\nCrie uma função que receba um número e retorne o dobro desse número.")
time.sleep(3)

def multi(num1):  

    dobro = int(num1) * 2
    return dobro

print(multi(input("escreva um número: ")))

#3. If/Else: Par ou Ímpar Escreva um programa que peça ao usuário um número e, em seguida, diga se o número é par ou ímpar.
print("\nEscreva um programa que peça ao usuário um número e, em seguida, diga se o número é par ou ímpar.")
time.sleep(3)

def imp(num1):

    if int(num1) % 2 == 0:
        print("é par")
    else:
        print("é ímpar")

imp(input("escreva um número: "))

#4. For: Contar até 10 Crie um programa que use um loop for para imprimir os números de 1 a 10.
print("\nCrie um programa que use um loop for para imprimir os números de 1 a 10.")
time.sleep(3)

def impress():

    lista=(1,2,3,4,5,6,7,8,9,10)

    for i in lista:
        time.sleep(0.25)
        print(i)

impress()

#5. While: Contagem Regressiva Escreva um programa que faça uma contagem regressiva de 5 até 1, usando um loop while.
print("\nEscreva um programa que faça uma contagem regressiva de 5 até 1, usando um loop while.")
time.sleep(3)

def loop():

    looping=5

    while looping != 0:
        print(looping)
        time.sleep(0.5)
        looping -= 1

loop()

#6. Lista: Imprimir Elementos Crie uma lista com 5 frutas e use um loop for para imprimir cada uma delas.
print("\nCrie uma lista com 5 frutas e use um loop for para imprimir cada uma delas.")
time.sleep(3)

def frutas():

    nham=("maçã", "banana", "abaixa aqui", "melãncia", "tomate")

    for i in nham:
        time.sleep(0.5)
        print(i)

frutas()

#7. Dicionário: Cores Favoritas Crie um dicionário com 3 pessoas e suas cores favoritas. Em seguida, peça o nome de uma pessoa e imprima a cor favorita dela.
print("\nCrie um dicionário com 3 pessoas e suas cores favoritas. Em seguida, peça o nome de uma pessoa e imprima a cor favorita dela.")
time.sleep(3)

def dicionalio():

    dicionário={
        'Gabriel': 'Gabriel, sua cor favorita é Azul',
        'joão': 'João, sua cor favorita é Vermelho',
        'larissa': 'Larissa, sua cor favorita é Amarelo',
        }
    print(dicionário["Gabriel"])
    print(dicionário["joão"])
    print(dicionário["larissa"])

dicionalio()

#8. Função: Somar Dois Números Escreva uma função que receba dois números como argumentos e retorne a soma deles.
print("\nEscreva uma função que receba dois números como argumentos e retorne a soma deles.")
time.sleep(3)

def vazio_roxo():

    Vermelho= input("Vermelho requisita um número: ")
    Azul= input("Azul pede por um número: ")

    roxo= int(Vermelho) + int(Azul)
    print("tecnica imaginária")
    time.sleep(1)

    print("Número roxo:")
    time.sleep(1)

    print(roxo)
    time.sleep(2)

vazio_roxo()

#9. If/Else: Verificar Maioridade Crie um programa que peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.
print("\nCrie um programa que peça a idade do usuário e informe se ele é maior de idade (18 anos ou mais) ou menor de idade.")
time.sleep(3)

def age():

    idade=input("fale sua idade: ")

    if int(idade) < 18:
        print("tem nem barba na fuça ainda")
    else:
        print("tapa clt")

age()

#10. Módulos: Mostrar Data Atual Use o módulo datetime para mostrar a data e a hora atual.
print("\nUse o módulo datetime para mostrar a data e a hora atual.")
time.sleep(2)

def hojemsm():
    
    agr = datetime.now()
    LitTexto = agr.strftime("%d/%m/%y %H:%M:%S")

    print(LitTexto)

hojemsm()