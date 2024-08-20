import random

n1 = (input("Digite o primeiro nome: "))
n2 = (input("Digite o segundo nome: "))
n3 = (input("Digite o terceiro nome: "))
n4 = (input("Digite o quarto nome: "))

nomes = [n1, n2, n3, n4]


#random.shuffle sorteia uma ordem dos nomes dentro da lista

sorteado = random.choice(nomes)
print(f"\nO nome sorteado foi: {sorteado}!")
