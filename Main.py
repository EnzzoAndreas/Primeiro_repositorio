
from Calculadora.operacoes_simples import somar, subtrair, multiplicar

if __name__ == "__main__":
    
    opcao = -1
    while opcao != 4:
        print('\ncalculadora GIT')
        print('=' * 20)
        print('1 - Somar')
        print('2 - Subtração')
        print('Multiplicação')
        print('4 - Sair')
        print('=' * 20)
        opcao = int(input('Opção: '))

        if opcao == 1:
            operador1 = int(input('Operador 1: '))
            operador2 = int(input('Operador 2: '))
            resultado = somar(operador1, operador2)
            print(f'Resultado: {resultado}')

        elif opcao == 2:
            operador1 = int(input('Operador 1: '))
            operador2 = int(input('Operador 2: '))
            resultado = subtrair(operador1, operador2)
            print(f'Resultado: {resultado}')
        elif opcao == 3:
            operador1 = int(input('Operador 1: '))
            operador2 = int(input('Operador 2: '))
            resultado = multiplicar(operador1, operador2)
            print(f'Resultado: {resultado}')
        elif opcao == 4:
            print('Obrigado por usar nossa Calculadora GIT')
        else:
            print('Opção INVALIDA, por favor tente novamente')