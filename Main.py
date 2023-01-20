if __name__ == "__main__":
    
    opcao = -1
    while opcao != 2:
        print('calculadora GIT')
        print('=' * 20)
        print('1 - Somar')
        print('2 - Sair')
        print('=' * 20)
        opcao = int(input('Opção: '))

        if opcao == 1:
            print('Opção Somar')
        elif opcao == 2:
            print('Obrigado por usar nossa Calculadora GIT')