#Celsius e Fahrenheit

total_celsius = 0

while True:
    celsius = float(input("Digite a quantidade de graus celsius ou 0 para parar o loop!: "))
    if celsius == 0:
        break
    total_celsius += celsius
    print(f"\nAqui está o registro de celsius: {celsius}\n")

print(f"\nA soma de todos os celsius deu: {total_celsius}c!")
fahrenheit = ((total_celsius * 9) / 5) + 32
print(f"A conversão para fahrenheit ficou de: {fahrenheit}f!")
