import math
# Algortimo Juros simples

'''

C = float(input("Digite o capital inicial: "))  #Armazena o capital
i = float(input("Digite a taxa de juros: "))    #Armazena a taxa de juros
n = float(input("Digite o prazo: "))            #Armazena o prazo

def calcula_juros():    #Função responsavel pelo calculo de juros
    j = C*i*n           #Formula para calcular os juros
    return j            #retorna o juro calculado

print(calcula_juros())  #mostra na tela o juro calculado

'''

# Algoritmo para calcular media

'''

def calcula_media():

    N1 = float(input("digite a primeira nota: "))

    while N1 > 10 or N1 < 0:
        N1 = float(input("digite uma nota maior ou menor que 10: "))

    N2 = float(input("digite a segunda nota: "))

    while N2 > 10 or N2 < 0:
        N2 = float(input("digite uma nota maior ou menor que 10! "))

    Med = float((N1 + N2) / 2)

    print("sua média é:", Med)

calcula_media()

'''

# Algoritmo calculo da força resultante

'''

def calcula_forca_resultante():
    F1 = float(input("digite F1: "))    # Armazena o valor da primeira força
    F2 = float(input("digite F2: "))    # Armazena o valor da segunda força
    CosN = float((input("digite o Cosseno: "))) # Armazena o valor do cosseno
    Cos = math.cos(math.radians(CosN))          # Calcula o cosseno do valor

    FR =math.sqrt ((F1*F1)+(F2*F2)+(2*F1*F2*Cos))
    print("Força resultante = ",FR)
#FR = (F1*(1/2)+F2(1/2)+2*F1*F2*Cos)*(1/2)
calcula_forca_resultante()

'''

#Algoritmo questão 4

'''

def calcula_valor_futuro():

    n = int(input("Digite o valor de n: "))     #Armazena o valor de n e transforma para um número inteiro
    x = float(input("Digite o valor de x: "))   #Armazena o valor de x
    i = 0   #Cria a variavel responsavel pela contagem
    y = 0   #Cria a variavel responsavel pela contagem do loop

    while y<=n:     #Equanto o y for menor que o valor digitado, calcular o valor atualizado
        xn = i*x    #Expressão matematica para calcular o valor final
        y += 1      #Incremento do y
        i += 2      #Incremento do i
    else:
        print(xn)   #Caso não entre no loop, mostrar na tela o valor final

calcula_valor_futuro()  #Chamada de função

'''

#Questão Sugerida pelo professor cris resolvida

'''

a = float(input("Digite o valor inicial: "))
r = 2
dias = int(input("Digite a quantidade de dias: "))
vetor = []

i = 0
while i <dias:
    ax = a*(r**i)
    vetor.append(ax)
    i += 1

soma = sum(vetor)
print("Vetor com os valores: ",vetor)
print("Somatorio do vetor: ", soma)

'''

#Equação de segundo grau

'''

a,b,c = float(input("Digite o valor de a: ")) , float(input("Digite o valor de b: ")) , float(input("Digite o valor de c: "))

def calcula_delta(a,b,c):
    d = (b**2) - (4*a*c)
    return d

def calcula_x1(a,b,c):
    x1 = (-b + ((calcula_delta(a,b,c)) ** 0.5) ) / 2 * a    #calculando raiz utilizando exponencial
    return x1

def calcula_x2(a,b,c):
    x2 = (-b - (math.sqrt(calcula_delta(a,b,c)))) / 2 * a   #calculando raiz utilizando a biblioteca math
    return x2


delta = calcula_delta(a,b,c)
raiz1 = calcula_x1(a,b,c)
raiz2 = calcula_x2(a,b,c)

print("Delta =" + str(delta) + "\nPrimeira raiz: " + str(raiz1) + "\nSegunda raiz: " + str(raiz2))

'''

#Programa pra calcular fatorial
'''

n = int(input('Digite um numero para calcular seu fatorial: '))
f = 1

for c in range (1, n):
    f = f*n
    n -= 1

print("Seu fatorial ", f) 

'''