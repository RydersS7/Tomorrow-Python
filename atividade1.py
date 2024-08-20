import math

# Solicita ao usuário o comprimento dos catetos
cateto_oposto = float(input("Digite o comprimento do cateto oposto: "))
cateto_adjacente = float(input("Digite o comprimento do cateto adjacente: "))

# Calcula o comprimento da hipotenusa
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

# Exibe o resultado
print(f"O comprimento da hipotenusa é: {hipotenusa:.2f}")
