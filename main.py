##Sistema Bancário

saldo = 2000
limite_de_saques = 3
saque_maximo = 500
extrato = []

while True:
    opt = int(input('''
    ***** Banco Itander ***** 
    Escolha uma opção
    1 - Depósito
    2 - Saque
    3 - Extrato
    0 - Sair
    *************************
    '''))
    
    match opt:
        case 1:
          deposito = float(input("Valor do depósito: "))
          if deposito < 1:
            print("O depósito não pode ser negativo ou igual a 0")
          else:
            saldo = saldo + deposito
            extrato.append(f"{saldo - deposito} + {deposito} = {saldo}")
            print("Depósito realizado com sucesso \n")
                    
        case 2:
            saque = float(input("Valor do saque: "))

            if limite_de_saques != 0:
                if saldo < saque:
                    print("Saldo insuficiente")
                elif saque > saque_maximo:
                    print(f"O valor máximo de saque é de {saque_maximo}")
                elif saque < 1:
                    print("O saque não pode ser negativo ou igual a 0")
                else:
                    saldo = saldo - saque
                    limite_de_saques = limite_de_saques - 1
                    extrato.append(f"{saldo + saque} - {saque} = {saldo}")
                    print("Saque realizado com sucesso")
            else:
                print("Você fez seus 3 saques diários")

        case 3:
            print(f"Seu saldo: R${saldo}")

            if len(extrato) == 0:
                print("Sem registros no extrato")
            else:
                print("Seu extrato é: ")
                for i in extrato:
                    print(f"{i}")

        case 0:
            print("Saindo do sistema")
            break
          
        case _:
            print("opção inválida \n")
