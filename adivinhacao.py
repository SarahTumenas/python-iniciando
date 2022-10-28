print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 13
total_de_tentativas = 3


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

