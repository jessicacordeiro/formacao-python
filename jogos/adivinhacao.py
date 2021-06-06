print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 13

chute_str = input("Digite um número de sua preferência: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

if(numero_secreto == chute):
    print("Você acertou! *-*")
else:
    print("Você errou! T-T ")

print("Fim de jogo.")