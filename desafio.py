menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar Usuário
[c] Criar Conta
[q] Sair


=> """

saldo = 0
limite = 500
numero_saques = 0
extrato = ""
usuarios = []
contas = []
LIMITE_SAQUES = 3
AGENCIA = "0001"

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):
   if saldo < valor:
      print("Erro! Não há saldo suficiente para o saque")
   elif valor > limite:
      print("Erro! Valor do saque excede limite")
   elif numero_saques >= limite_saques:
      print("Erro! Número  de saques diário execedido")
   elif valor > 0:
      saldo -= valor
      numero_saques += 1
      extrato += f"Saque: R$ {valor:.2f}\n"
      print(f"Saque de R${valor:.2f} realizado com sucesso!")
   else:
      print("Erro! O valor do saque é invalido")

   return saldo, extrato,  numero_saques

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

def cria_usuario(usuarios):
   cpf = input("Informe o CPF do usuário: ")

   usuarios_cadastrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]

   if usuarios_cadastrados:
      print('Usuário já cadastrado')
      return

   nome = input("Informe o nome completo: ")
   data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
   endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

   usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
   print("Usuário cadastrado com sucesso!")

def cria_conta(agencia, usuarios, contas):
   cpf = input("Informe o CPF do usuário: ")

   usuarios_cadastrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]   

   if not usuarios_cadastrados:
      print('Usuário não encontrado!')
      return
   
   numero_conta = len(contas) + 1
   conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuarios_cadastrados[0]}
   contas.append(conta)
   print("Conta criada com sucesso!")



while True:
   opcao = input(menu)

   if opcao == "d":
      valor = float(input("Informe o valor do depósito: "))

      saldo, extrato = depositar(saldo, valor, extrato)

   elif opcao == "s":
      valor = float(input("Informe o valor do saque: "))

      saldo, extrato, numero_saques = saque(saldo=saldo, valor=valor, extrato= extrato, limite= limite, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)

   elif opcao == "e":
      exibir_extrato(saldo, extrato= extrato)
   elif opcao == "u":
      cria_usuario(usuarios)
   elif opcao == "c":
      cria_conta(AGENCIA, usuarios, contas)

   elif opcao == "q":
      break

   else:
      print("Operação inválida, por favor selecione novamente a operação desejada.")

