
secreto = "perfume"
digitadas = []
chances = 3 

while True:
    if chances < 1:
        print("Acabou suas chances!")
        break

    letra = input("Digite uma letra ")
    if len(letra) > 1:
        print("Digite uma letra apenas")
    elif letra.isdigit():
        print("Não digite números, apenas letras")
        continue
    digitadas.append(letra)

    if letra in secreto:
        print(f"A letra {letra} tem na palavra secreta")

    else:
        print("Letra não existe na palavra secreta")
        digitadas.pop()

    secreto_temporario = ""
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += "*"
    print(secreto_temporario)

    if secreto_temporario == secreto:
        print(f"Parabéns!! A palavra é {secreto_temporario}")
        break
    else:
        print(f"A palavra secreta é {secreto_temporario}")
    
    if not letra in secreto:
        chances -= 1 
    print(f"Você tem {chances} tentativas")
    print()
