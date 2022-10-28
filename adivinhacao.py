print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 13
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas ):
    print("Tentativas: ", rodada, " de: ", total_de_tentativas)
    chute = input("Digite o seu número: ")
    print("Você digitou ", chute)
    numero_chute = int(chute)

    acertou = numero_chute == numero_secreto
    chute_maior = numero_chute > numero_secreto
    chute_menor = numero_chute < numero_secreto

    if (acertou):
        print("Você acertou!!")
    else:
        if(chute_maior):
            print("Você errou! Seu chute foi maior que o número secreto")
        elif(chute_menor):
            print("Você errou! Seu chute foi menor que o número secreto")
    rodada = rodada + 1

print("Fim do jogo!")

