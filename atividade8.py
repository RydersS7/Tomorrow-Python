#Tabuada com calculadora

operações = str(input("\nSelecione a sua operação para prosseguir: [+], [-], [*], [/]: "))


while True:
     
 
  if operações == "+":
     
     print("\nEssa é a tabuada de soma!")
     soma = int(input("\nDigite um número para prosseguir ou digite 0 para sair do laço: "))

     if soma == 0:
       print("\nEncerrando o programa...")
       break
         
     print("-" * 65)
     print("\n") 

     for i in range(1, 11):
      tabuada = soma + i
      print(f"{soma} + {i} = {tabuada}")
      

  elif operações == "-":
      
     print("\nEssa é a tabuada de subtração!")
     sub = int(input("\nDigite um número para prosseguir ou digite 0 para sair do laço:"))
     
     if sub == 0:
       print("\nEncerrando o programa...")
       break
     
     print("-" * 65)
     print("\n")

     for i in range(1, 11):
      tabuada = sub - i
      print(f"{sub} - {i} = {tabuada}")

  elif operações == "*":
      
     print("\nEssa é a tabuada de multiplicação!")
     mult = int(input("\nDigite um número para prosseguir ou digite 0 para sair do laço: "))
     
     if mult == 0:
       print("\nEncerrando o programa...")
       break
     
     print("-" * 65)
     print("\n")

     for i in range(1, 11):
          
      tabuada = mult * i
      print(f"{mult} x {i} = {tabuada}")
    
  elif operações == "/":
     print("\nEssa é a tabuada de divisão!")
     div = float(input("\nDigite um número para prosseguir ou digite 0 para sair do laço: "))
     
     if div == 0:
       print("\nEncerrando o programa...")
       break
     
     print("-" * 65)
     print("\n")

     for i in range(1, 11):
      tabuada = div / i
      print(f"{div} % {i} = {tabuada:.2f}")

  else:
    print("Operação inválida, tente novamente!")
