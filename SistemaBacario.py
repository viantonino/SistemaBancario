"""Desafio: Criar um sistema bancário
Criar um sistema bancário com as operações: sacar, depositar, e visualizar extrato.
Valor interio e positivo: o sistema não pode permitir valores negativos
As informações precisam estár armezenadas para exibir extrato.

Saque: 3 saques diarios com limite máximo de R$500,00 por saque.c

Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será posssivel sacar o dinheiro por falta de saldo. 
Todos os saques devem ser armazenados em uma variavel e exibidos na operação de extrato

Extrato: essa operação deve listar todos os depositos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. 
Os valores devem ser exibidos utilizando o formato R$xxx.xx """


menu = """""

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numro_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        deposito = float(input("Informe o valor do seu depósito:"))

        if deposito > 0:
            saldo += deposito
            extrato += f"Depósito: R${deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("O valor inserido é inválido! Tente novamente.")


    elif opcao == '2':
        saque = float(input("Informe o valor do seu saque:"))

        # 3 saques diarios com limite máximo de R$500,00 por saque.

        UltrapassouSaques = numro_saques >= LIMITE_SAQUES
        UltrapassouLimite = saque > limite

        #Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será posssivel sacar o dinheiro por falta de saldo. 

        UltrapassouSaldo = saque > saldo

        
        if UltrapassouSaques:
            print('Limite diário excedito! Tente novamente 24 horas após o ultimo saque.')
        elif UltrapassouLimite:
            print("Não é possivel realizar saques maiores que R$500,00! Tente novamente.")
        elif UltrapassouSaldo:
            print("Saldo Insuficiente!")
        elif saque > 0:
            saldo -= saque
            numro_saques += 1
            extrato += f"Saque: R${saque:.2f}\n"
            print("Saque realizado com sucesso!")
            
    elif opcao == '3':
        print("Extrato:_______________")

        if not extrato:
            print("Não foram realizadas movimentações nessa conta.")
        else:
            print(extrato)

        print(f"\nSaldo: R$ {saldo:.2f}")
        print("_______________________")
        

    elif opcao == '4':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")