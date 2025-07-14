menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair


=> """

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
LIMITE_SAQUES = 3

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
   if saldo < valor:
      print("Erro! Não há saldo suficiente para o saque")
   elif valor > limite:
      print("Erro! Valor do saque excede limite")
   elif numero_saques >= limite_saques:
      print("Erro! Numero de saques diário execedido")
   elif valor > 0:
      saldo -= valor
      numero_saques += 1
      extrato += f"Saque: R$ {valor:.2f}\n"
      print(f"Saque de R${valor:.2f} realizado com sucesso!")
   else:
      print("Erro! O valor do saque é invalido")

   return saldo, extrato

def depositar(saldo, valor, extrato, /):
   if valor > 0:
      saldo += valor
      extrato += f"Depósito: R$ {valor:.2f}\n"
   else:
      print("Erro! O valor do depósito não pode ser menor ou igual a 0")
   return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
   print("\n================ EXTRATO ================")
   print("Não foram realizadas movimentações." if not extrato else extrato)
   print(f"\nSaldo:\t\tR$ {saldo:.2f}")
   print("==========================================")

while True:
   opcao = input(menu)

   if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))

      saldo, extrato = depositar(saldo, valor, extrato)

   elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))

      saldo, extrato = saque(saldo=saldo, valor=valor, extrato= extrato, limite= limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)

   elif opcao == "e":
      exibir_extrato(saldo, extrato= extrato)

   elif opcao == "q":
      break

   else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")

