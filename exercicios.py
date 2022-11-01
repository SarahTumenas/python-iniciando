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

