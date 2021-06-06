print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 13

chute_str = input("Digite um número de sua preferência: ")

print("Você digitou ", chute_str)

chute = int(chute_str)

acertou = chute == numero_secreto
maior   = chute > numero_secreto
menor   = chute < numero_secreto

if(acertou):
    print("Você acertou! *-*")
else:
    if(maior):
        print("Você errou! O seu chute foi maior que o número secreto. T-T")
    elif(menor):
        print("Você errou! O seu chute foi menor que o número secreto. T-T")

print("Fim de jogo.")