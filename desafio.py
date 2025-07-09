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

while True:
    opcao = input(menu)

    if opcao == "d":
       valor = float(input("Informe o valor do depósito: "))

       if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
       else:
          print("Erro! O valor do depósito não pode ser menor ou igual a 0")

    elif opcao == "s":
       valor = float(input("Informe o valor do saque: "))

       if saldo < valor:
          print("Erro! Não há saldo suficiente para o saque")

       elif valor > limite:
          print("Erro! Valor do saque excede limite")

       elif numero_saques == 3:
          print("Erro! Numero de saques diário execedido")

       elif valor > 0:
          saldo -= valor
          numero_saques += 1
          extrato += f"Saque: R$ {valor:.2f}\n"
          print(f"Saque de R${valor:.2f} realizado com sucesso!")
          
       else:
          print("Erro! O valor do saque é invalido")
          
    elif opcao == "e":
       print("\n================ EXTRATO ================")

       print(f"\nSaldo: R$ {saldo:.2f}")
       print("Não foram realizadas movimentações." if not extrato else extrato)
       print("==========================================")

    elif opcao == "q":
       break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")