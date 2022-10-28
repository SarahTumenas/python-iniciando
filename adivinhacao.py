print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 13

chute = input("Digite o seu número: ")

print("Você digitou ", chute)

numero_chute = int(chute)

if (numero_secreto == numero_chute):
    print("Você acertou!!")
else:
    print("Você errou!")
