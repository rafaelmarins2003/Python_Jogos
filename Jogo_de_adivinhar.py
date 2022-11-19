def jogar_adivinhacao():
    import random
    print("**********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("**********************************")

    numero_secreto = round(random.random() * 100)
    if numero_secreto == 0:
        numero_secreto = round(random.random() * 100)
    rodada = 1
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facíl  (2) Médio  (3) Difícil")

    nivel = int(input("Defina o nivel de dificuldade: "))
    while nivel != 1 or nivel != 2 or nivel != 3:
        if nivel == 1:
            tentativas = 10
            tent_aux = 10
            break
        if nivel == 2:
            tentativas = 7
            tent_aux = 7
            break
        if nivel == 3:
            tentativas = 5
            tent_aux = 5
            break
        else:
            nivel = int(input("Defina o nivel de dificuldade: "))

    while tentativas > 0:
        print("Rodada {} de {}".format(rodada, tent_aux))
        chute = int(input("Digite o seu numero(entre 1 e 100): "))
        print("Você digitou: ", chute)
        if numero_secreto == chute:
            print("Você acertou")
            break
        else:
            if numero_secreto > chute:
                print("Você errou, o numero secreto é MAIOR que {}".format(chute))
                tentativas = tentativas - 1
                pontos = pontos - abs(numero_secreto - chute)
            if numero_secreto < chute:
                print("Você errou, o numero secreto é MENOR que {}".format(chute))
                tentativas = tentativas - 1
                pontos = pontos - abs(numero_secreto - chute)
        rodada = rodada + 1

    print("O numero screto era : {}".format(numero_secreto))
    print("Pontuação: {} de 1000".format(pontos))
    print("Fim de jogo")


    if(__name__ == "__main__"):
        jogar_adivinhacao()
