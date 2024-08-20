#Calcular a area de uma parede e o quantidade de tinta necessária para pintá-la

largura = float(input("Digite a largura da parede: "))
altura = float(input("Digite a altura da parede: "))

area = largura * altura 

print(f"\nA área da sua parede é de {area:.2f} metros quadrados!")

tinta = area / 2
print(f"\nPra isso você precisará de {tinta} litros de tinta!")
