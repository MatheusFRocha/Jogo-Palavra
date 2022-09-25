# Lista em Python
# fatiamento
# append, insert, pop, del, clear, extend, +
# min, max
# range

# # l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# # l1.extend(l2)
# l2.insert(0, "banana")
# print(l2)
# l2.pop()
# print(l2)
#     0  1  2  3  4  5  6  7  8
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# print(max(l2))
# print(min(l2))

# l2 = list(range(0, 10))
# print(l2)

# l2 = ["string", True, 10, 10.3]

# for elem in l2:
#     print(f"O elem de {elem} é {type(elem)} e seu valor é {elem}")



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
