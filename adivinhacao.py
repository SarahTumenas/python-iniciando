print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 13

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

print("Fim do jogo!")
