import os


def main():
    print('CALCULADORA ')
    print('')
    op = ''
    contador = 1
    ativo = True
    resul = 0

    while op != '+' and op != '-' and op != '*' and op != '/':
        op = str(input('Digite qual operacao deseja utlizar +-*/'))

        if not op:
            exit()
        if op != '+' and op != '-' and op != '*' and op != '/':
            print('OPERACAO INVALIDA! TENTE NOVAMENTE')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('Digite um numero para ser calculado, se quiser sair da calculadora aperte enter sem digitar nada')

    while ativo == True:
        if op == '+':
            while contador >= 1:
                print(resul)
                n = str(input())
                os.system('cls' if os.name == 'nt' else 'clear')
                if not n :
                    ativo = False
                    contador = 0
                    main()
                else:
                    n = int(n)
                    resul += n
                    contador += 1
        elif op == '-':
            while contador >= 1:
                print(resul)
                n = str(input())
                os.system('cls' if os.name == 'nt' else 'clear')
                if not n:
                    ativo = False
                    contador = 0
                    main()

                else:
                    n = int(n)
                    resul -= n
                    contador += 1
        elif op == '*':
            while contador >= 1:
                print(resul)
                n = str(input())
                os.system('cls' if os.name == 'nt' else 'clear')
                if not n:
                    ativo = False
                    contador = 0
                    main()
                if resul == 0:
                    n = int(n)
                    resul = n
                else:
                    n = int(n)
                    resul *= n
                    contador += 1
        elif op == '/':
            while contador >= 1:
                print(resul)
                n = str(input())
                os.system('cls' if os.name == 'nt' else 'clear')
                if not n:
                    ativo = False
                    contador = 0
                    main()
                elif n == '0':
                    print('ERRO! DIVISAO POR ZERO')
                    continue
                if resul == 0:
                    n = int(n)
                    resul = n
                else:
                    n = int(n)
                    resul /= n
                    contador += 1
if __name__ == "__main__":
    main()
