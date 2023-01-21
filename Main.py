if __name__ == "__main__":
    
    opcao = -1
    while opcao != 3:
        print('\ncalculadora GIT')
        print('=' * 20)
        print('1 - Somar')
        print('2 - Subtração')
        print('3 - Sair')
        print('=' * 20)
        opcao = int(input('Opção: '))

        if opcao == 1:
            print('Opção Somar')
        elif opcao == 2:
            print('Opção Subtrair')
        elif opcao == 3:
            print('Obrigado por usar nossa Calculadora GIT')
        else:
            print('Opção INVALIDA, por favor tente novamente')