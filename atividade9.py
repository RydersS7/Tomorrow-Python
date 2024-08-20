#Conversor de moedas

print("\n!!Bem vindo ao conversor de moedas!!")
print("-" * 36)


while True:

  real = float (input("\nDigite o seu valor em real ou digite 0 para sair do laço: "))

  if real == 0:
    print("\nEncerrando o programa...")
    break

  else:
    dolar = real / 5.66
    print(f"\nO valor {real:.2f}$ equivale a {dolar:.2f} dólar!")
