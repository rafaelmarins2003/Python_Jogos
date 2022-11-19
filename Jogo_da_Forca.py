def jogar_forca():

    abertura_jogo()

    palavra_secreta = "baleia".upper()
    acertos = letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(acertos)

    while not enforcou and not acertou:

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            chute_correto(chute, acertos, palavra_secreta)
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in acertos
        print(acertos)

    if acertou:
        print("Você ganhou!")
    else:
        print("Você perdeu!")
    print("Fim de jogo")

    if(__name__ == "_main__" ):
        jogar_forca()



def abertura_jogo():
    print("$$$$$$$$$$$$$$$")
    print("$Jogo da forca$")
    print("$$$$$$$$$$$$$$$")

def letras_acertadas(palavra):
    return ["_" for letra in palavra]

def chute_correto(chute, acertos, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if (chute == letra):
            acertos[index] = letra
        index += 1