#Conversor de metros para milimetros e centimetros

while True:
  metros = float(input("\nDigite a quantidade de metros para ser convertido ou digite 0 para encerrar o laço: "))

  if metros == 0:
     break
  
  else:
   centimetros = metros * 100
   milímetros = metros * 1000

   print("\nAqui está a sua conversão:")
   print(f"\n{metros:.2f} metros é igual a {centimetros:.2f} centímetros!")
   print(f"{metros:.2f} metros é igual a {milímetros:.2f} milímetros!")
