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

