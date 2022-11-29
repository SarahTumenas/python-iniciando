import random



print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

#numero_secreto = round(random.random() * 100) # 0.0 1.0
numero_secreto = random.randrange(1, 101)
total_de_tentativas = 0

print("Qual o nível de dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Define o nível: "))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2):
    total_de_tentativas = 10
else:
    total_de_tentativas = 5



for rodada in range(1, total_de_tentativas + 1):
    print("Tentativas {} de {} ".format(rodada, total_de_tentativas))
    chute = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute)
    numero_chute = int(chute)

    if(numero_chute < 1 or numero_chute > 100):
        print("Você  deve digitar um número entre 1 e 100")
        continue

    acertou = numero_chute == numero_secreto
    chute_maior = numero_chute > numero_secreto
    chute_menor = numero_chute < numero_secreto

    if (acertou):
        print("Você acertou!!")
        break
    else:
        if(chute_maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto")

print("Fim do jogo!")

