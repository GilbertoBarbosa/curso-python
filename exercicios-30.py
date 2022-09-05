
# Exercício 1
numero = input("Digite um número inteiro: ")

if numero.isnumeric():
    resto = int(numero) % 2
    if resto == 0:
        print("O número {} é par".format(numero))
    else:
        print("O número {} é impar".format(numero))
else:
    print("{} não é número".format(numero))



# Exercício 2
horas = input("Que horas são? ")

h = int(horas[0:2])

if h <= 11:
    print("Bom dia")
elif h <= 17:
    print("Boa tarde")
else:
    print("Boa noite")


# Exercício 3
nome = input("Digite o seu primeiro nome: ")

tamanho = len(nome)

if tamanho <= 4:
    print("Seu nome é curto")
elif tamanho <= 6:
    print("Seu nome é normal")
else:
    print("seu nome é muito grande")

