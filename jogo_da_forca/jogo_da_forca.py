from visual import visual_dict
import random
from email.encoders import encode_noop

def random_palavra():
    with open("palavras.txt", encoding='utf8') as arquivo:
        txt = arquivo.readlines()
        lista_palavras = [palavra.replace("\n","").upper() for palavra in txt]
    return random.choice(lista_palavras)

def iniciar_jogo():
    palavra_secreta = random_palavra()
    letras_palavra = set(palavra_secreta)
    palpites = set()
    acertos = set()
    tentativas = 7

    while len(letras_palavra) > 0 and tentativas > 0:
        print(f"Descubra a palavra secreta! {palavra_secreta}")
        
        painel = [letra if letra in acertos else '_' for letra in palavra_secreta]
        print(" ".join(painel))
        print(f'Tentativas: {tentativas}')

        if len(palpites)> 0:
            print(f"Letras já escolhidas: {' '.join(palpites)}")

        chute = input("Escolha uma letra: ").upper()

        if chute in palpites:
            print("Você já escolheu essa letra antes! Escolha outra!")
        elif chute in letras_palavra:
            acertos.add(chute)
            letras_palavra.remove(chute)
        else:
            print(f"A palavra secreta não contém a letra {chute}")
            tentativas -= 1
            print(visual_dict[tentativas])

        palpites.add(chute)
    
    if tentativas==0:
        print(f"Você perdeu! A palavras secreta era: {palavra_secreta}")
    else:
        print(f"Parabéns, você acertou a palavra secreta: {palavra_secreta}")

iniciar_jogo()