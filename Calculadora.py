import calculos
import os
import time

def limpar_tela():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

while True:
    limpar_tela()

    try:
        operacao = int(input('''-------Calculadora Python -------
    
    1. Adição
    2. Subtração
    3. Multiplicação
    4. Divisão
    
Digite a operação matemática que deseja: '''))

        if operacao not in [1, 2, 3, 4]:
            print("\nOperação inválida! Escolha entre 1 e 4.")
            time.sleep(1)
            limpar_tela()
            continue

        limpar_tela()
        time.sleep(1)
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        match operacao:
            case 1:
                resultado = calculos.adicao(n1, n2)
            case 2:
                resultado = calculos.subtracao(n1, n2)
            case 3:
                resultado = calculos.multiplicacao(n1, n2)
            case 4:
                if n2 == 0:
                    print('\nValor inválido, o segundo valor da divisão não pode ser zero.')
                else:
                    resultado = calculos.divisao(n1, n2)

        time.sleep(1.5)
        repeticao = input('\nDeseja realizar uma nova operação? S ou N ')
        if repeticao.upper() == 'S' or repeticao.upper() == 'SIM':
            continue
        elif repeticao.upper() in ['NÃO', 'NAO', 'N']:
            print('Muito obrigado por usar nossa calculadora!')
            time.sleep(1.5)
            break

    except ValueError:
        print('\nValor inválido')