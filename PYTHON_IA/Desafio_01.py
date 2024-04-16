print('Bom dia, bem vindo ao banco XXXX')
saldo = 0
saque_diario = 0
extrato = {'saque': [], 'deposito': []}
while True:
    print('''
    Opções de operação:
    Pressione [S] para efetuar saque
    Pressione [D] para deposito
    Pressione [E] para extrato
    pressione [Q] para sair
    ''')
    LIMITE_SAQUE = 500
    escolha = input('Digite sua operação escolhida: ').upper()
    if escolha not in 'SDEQ':
        print('Escolha invalida')

    if escolha == 'S':
        if saque_diario < 3:
            saque_diario += 1
            valor_saque = -float(input('Digite o valor para o saque: R$'))
            if (valor_saque * -1) > LIMITE_SAQUE:
                print('O valor da operação excede o limite de diário de saque.')
            elif valor_saque > saldo:
                print('O valor excede o valor de saldo.')
            else:
                saldo += valor_saque
                extrato['saque'].append(valor_saque)
                print(f'O saldo atual é R${saldo:.2f}')

        else:
            print('Limite de saque atingido.')


    if escolha == 'D':
        valor_deposito = float(input('Digite o valor do deposito: R$'))
        saldo += valor_deposito
        extrato['deposito'].append(valor_deposito)
        print(f'O saldo atual é R${saldo:.2f}')


    if escolha == 'E':
        if len(extrato) > 0:
            if len(extrato['deposito']) > 0:
                print('Os valores de depósito feitos na sua conta foram: ')
                for valor in extrato['deposito']:
                    print(f'R${valor:.2f}')
            else:
                print('Não houve depósitos na sua conta.')

            if len(extrato['saque']) > 0:
                print('E os valores de saque foram: ')
                for valor in extrato['saque']:
                    print(f'R${valor:.2f}')
            else:
                print('Não houve saques na sua conta.')
        else:
            print('Não há transações para exibir no extrato.')

        print(f'O saldo atual é de R${saldo:.2f}')
    if escolha == 'Q':
        print('Até outro dia. Saindo do sistema...')
        break
