import random




minha_idade = 26
idade_namorado = 25
if(minha_idade == idade_namorado):
    print('temos idades iguais')
else:
    print('temos idades diferentes')

numero1 = 10
numero2 = 10
if(numero1 == numero2):
    print("São números iguais")

idade1 = 10
idade2 = int("20")
print(idade1 + idade2)

nome = "Nico"
sobrenome = "Steppat"
print(nome + sobrenome)
print("*******************************************************")

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome)
print("*******************************************************")

nome = "Nico"
sobrenome = "Steppat"
print(nome, sobrenome, sep="_")
print("*******************************************************")

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

if (idade > 18):
    print("Você é maior de idade.")
else:
    if (idade < 12):
        print("Você é uma criança.")
    elif (idade >= 12):
        print("Você é um adolescente.")
print("*******************************************************")

idade_str = input("Digite sua idade: ")
idade = int(idade_str)

maior_idade = idade > 18
crianca     = idade < 12
adolescente = idade > 12

print("*******************************************************")

usuario = input("Informe o usuário do sistema!")

if(usuario == "Flávio"):
    print("Seja bem-vindo Flávio!")
elif(usuario == "Douglas"):
    print("Seja bem-vindo Douglas!")
elif(usuario == "Nico"):
    print("Seja bem-vindo Nico")
else:
    print("Usuário não identificado!")

print("*******************************************************")
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 2
    if(contador == 5):
        contador = contador + 2

print("*******************************************************")

dia_ini = 24
dia_fim = 28
mes = "fevereiro"
ano = 2017

print("Em {} o Carnaval acontece em {} do dia {} até o dia {}".format(ano, mes, dia_ini, dia_fim))

print("*******************************************************")
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 1
print("xxxx")
for contador in range(1, 11):
    print(contador)

print("*******************************************************")
contador = 1
while(contador <= 10):
    print(contador)
    contador = contador + 3
print("xxxx")
for contador in range(1, 11, 3):
    print(contador)


print("*******************************************************")

i = 1
while(i <= 7):
    print(i)
    i = i + 1
    if(i == 5):
        break
print("*******************************************************")

for i in range(1, 8):
    if(i == 5):
        continue
    print(i)
print("*******************************************************")

print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))

print("*******************************************************")
print("R$ {:7.1f}".format(1000.12))
print("R$ {:07.2f}".format(4.11))
print("*******************************************************")
nome = 'Matheus'
print(f'Meu nome é {nome}')
print(f'Meu nome é {nome.lower()}')

print("*******************************************************")



aleatorio = random.randrange(10)
print(aleatorio)
print("*******************************************************")

sorteado = random.randrange(1, 4)

print(sorteado)

if sorteado == 1:
    print("Paulo")
elif sorteado == 2:
    print("Juliana")
else:
    print("Tamires")
print("*******************************************************")
numero1= random.seed(100)
print(numero1)
numero2 = random.randrange(1, 101)
print(numero2)

print("*******************************************************")

pontos_perdidos = abs(21 - 32) / 3     #dividindo por três
print(pontos_perdidos)

x = 3 // 2
print(x)
print("*******************************************************")
def soma(a, b):
    return a + b

s = soma(3, 4)
print(s)
print("*******************************************************")

def executa():
    print("Executando a")

if(__name__ == "__main__"):
    executa()

print("*******************************************************")
a = "Cavalo"
b = "Calopsita"
print("{} e {}".format(b, a))

print("*******************************************************")

nome = "clarice"
nome.capitalize()
print(nome) ## continua como clarice e não Clarice como ela esperava

nome = "clarice"
nome = nome.capitalize()
print(nome)

palavra = "alura"
palavra.upper()
print(palavra) #qual é o resultado?

palavra1 = "alura"
palavra1 = palavra.upper()
print(palavra1) #qual é o resultado?

print("*******************************************************")

# coding: utf-8
frutas = ['Banana', 'Maca', 'Pera', 'Uva', 'Melancia', 'Jamelão']

fruta_pedida = input('Qual é a fruta que deseja consultar ?')

if(fruta_pedida in frutas):
    print ('Sim, temos a fruta.')
else:
    print ('Não temos a fruta.')

print("*******************************************************")

precos = [1525,1120,1464,1200,1330,1356,1312,1531,1232, 1234,1250,1114,1553,1147,1303,1296,1309,1404,1479,1376,1152,1440,1038,1018,1291,1388,1577,1115,1488,1494,1254,1230,1122,1396,1208,1356,1549,1116,1443,1075,1536,1542,1036,1015,1020,1217,1484,1032,1390,1026]
print(min(precos))

print("*******************************************************")

funcionarios = ['Astrid','Flavia','Talia', ... ,'Mauricio', 'Waldemar', 'Marina']
print(funcionarios)
print(len(funcionarios))

print("*******************************************************")

## Restante do código que gera a lista de colocação...


colocacao = ['Drible da Emoção', 'Bruxos como Ronaldinho', 'Só golaço', '3x1 não é goleada']

campeao = colocacao[0]

print(' O grande campeão do torneio é o time ' + campeao)
#Resultado:  O grande campeão do torneio é o time Bruxos como Ronaldinho

print("*******************************************************")
valores = [ 0, 0, 0, 1, 2, 3, 4]
print(valores.count(0))

letras_acertadas = ['_','_','_','_','_','_']
letras_faltando = str(letras_acertadas.count('_'))
print( 'Ainda faltam acertar {} letras'.format(letras_faltando))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva', 'Maçã', 'Uva']
print(frutas.index('Uva'))

frutas = ['Banana', 'Morango', 'Maçã', 'Uva']


fruta_buscada = 'Melancia'
if fruta_buscada in frutas:
    print(frutas.index(fruta_buscada))
else:
    print('Desculpe, a {} não está na lista frutas'.format( fruta_buscada))

print("*******************************************************")

lista = [11122233344, 22233344455, 33344455566]
print(lista)
lista.append(11122233344) #funciona!
print(lista)

colecao = {11122233344, 22233344455, 33344455566}
print(colecao)
colecao.add(44455566677) #vai adicionar pois não existe ainda
print(colecao)

for cpf in colecao:
     print(cpf)

pessoa1 = ("Nico", 39)
pessoa2 = ("Flavio", 37)
pessoa3 = ("Marcos", 30)

instrutores = [pessoa1, pessoa2, pessoa3]

print(instrutores)
print(instrutores[1][1])


instrutores = {'Nico' : 39, 'Flavio': 37, 'Marcos' : 30}
print(instrutores['Flavio'])

print("*******************************************************")

total = 0
palavra = "python rocks!"
acabou = False
while (not acabou):
    acabou = (total == len(palavra))
    total = total + 1
print(total - 1)

passos = 0
while (passos<10):
  passos += 1
print(passos)

print("*******************************************************")

frutas = ["maçã", "banana", "laranja", "melancia"]

#lista = []
#for fruta in frutas:
#    lista.append(fruta.upper())
lista = [fruta.upper() for fruta in frutas]
print(lista)

print("*******************************************************")
inteiros = [1,3,4,5,7,8]
print(inteiros)
quadrados = [n*n for n in inteiros]
print(quadrados)

print("*******************************************************")
arquivo = open('pessoas.txt', 'r')
linha = arquivo.readline()
print(linha)


arquivo1 = open('palavras.txt','r')
linhas = arquivo1.readline()
print(linhas)
linhas = arquivo1.readline()
print(linhas)

arquivo = open('palavras.txt','r')
conteudo = arquivo.read()
print(conteudo)
conteudo = arquivo.read()
print(conteudo)

print("*******************************************************")
logo = open('palavras.txt', 'r')
data = logo.read()
logo.close()

with open("palavras.txt") as arquivo:
    for linha in arquivo:
        print(linha)
print("*******************************************************")
# declara a função
def imprime_mensagem():
    print("Olá")

# chama a função
imprime_mensagem()

print("*******************************************************")

def soma_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero + segundo_numero)

def subtrai_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero - segundo_numero)

def multiplica_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero * segundo_numero)

def divide_dois_numeros(primeiro_numero, segundo_numero):
    print(primeiro_numero / segundo_numero)

print("*******************************************************")



