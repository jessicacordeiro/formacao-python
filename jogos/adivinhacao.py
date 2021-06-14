print("**********************************")
print("Bem vindo ao jogo de Adivinhação!")
print("**********************************")

numero_secreto = 13
total_tentativas = 3

for rodada in range(1, total_tentativas + 1):
    print("Tentativa {} de {}".format(rodada, total_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ")
    print("Você digitou ", chute_str)
    chute = int(chute_str)

    if(chute < 1 or chute > 100):
        print("Opção incorreta, para encontrar o número secreto tem que digitar um valor entre 1 e 100!")
        continue

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou! *-*")
        break
    else:
        if(maior):
            print("Você errou! O seu chute foi maior que o número secreto. T-T")
        elif(menor):
            print("Você errou! O seu chute foi menor que o número secreto. T-T")

print("Fim de jogo.")