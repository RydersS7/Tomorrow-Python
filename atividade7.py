#Media ponderada

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print("\n")

peso1 = float(input("Digite o primeiro peso: "))
peso2 = float(input("Digite o segundo peso: "))
peso3 = float(input("Digite o terceiro peso: "))


media = ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)) / (peso1 + peso2 + peso3)

print(f"\nA media ponderada de ({nota1}, {nota2} e {nota3}) é:  \n\n{media:.2f}")
