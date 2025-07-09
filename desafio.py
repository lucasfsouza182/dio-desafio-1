menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0

while True:
    opcao = input(menu)

    if opcao == "d":
       valor = float(input("Informe o valor do depósito: "))

       if valor > 0:
        saldo += valor
       else:
          print("Erro! O valor do depósito não pode ser menor ou igual a 0")

    elif opcao == "s":

    elif opcao == "e":

    elif opcao == "q":

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")