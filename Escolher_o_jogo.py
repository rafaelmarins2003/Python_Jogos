import Jogo_da_Forca
import Jogo_de_adivinhar
print("==================")
print("Escolha o seu jogo")
print("==================")

print("(1) Forca  (2) Adivinhação")

jogo = int(input("Qual jogo? "))

if(jogo == 1):
    print("Jogo da forca")
    Jogo_da_Forca.jogar_forca()
if(jogo == 2):
    print("Jogo de adivinhação")
    Jogo_de_adivinhar.jogar_adivinhacao()