# Este programa simula uma calculadora simples
# que realiza operações de soma, subtração, multiplicação e divisão.
# Ele continua em execução até que o usuário decida sair.

def soma_valor(nr1, nr2):
    """
    Função para somar dois números e retornar o resultado.
    """
    return nr1 + nr2

def subtrai_valor(nr1, nr2):
    """
    Função para subtrair dois números e retornar o resultado.
    """
    return nr1 - nr2

def dividir_valor(nr1, nr2):
    """
    Procedimento para dividir dois números e imprimir o resultado.
    """
    if nr2 != 0:
        resultado = nr1 / nr2
        print(f"O resultado da divisão é: {resultado}\n")
    else:
        print("Erro: Divisão por zero não é permitida.\n")

def multiplicar_valor(nr1, nr2):
    """
    Procedimento para multiplicar dois números e imprimir o resultado.
    """
    resultado = nr1 * nr2
    print(f"O resultado da multiplicação é: {resultado}\n")

# Variáveis
opcao = "0"
nr1 = 0.0
nr2 = 0.0

# Loop principal do programa
while opcao != "X":
    # Menu
    print("Escolha uma opção:")
    print("+")
    print("-")
    print("/")
    print("*")
    print("X - Sair")
    opcao = input().upper()

    if opcao not in ["X"]:
        try:
            nr1 = float(input("Qual o primeiro numero: "))
            nr2 = float(input("Qual o segundo numero: "))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.\n")
            continue

    if opcao == "+":
        resultado = soma_valor(nr1, nr2)
        print(f"O resultado da soma é: {resultado}\n")
    elif opcao == "-":
        resultado = subtrai_valor(nr1, nr2)
        print(f"O resultado da subtração é: {resultado}\n")
    elif opcao == "/":
        dividir_valor(nr1, nr2)
    elif opcao == "*":
        multiplicar_valor(nr1, nr2)
    elif opcao != "X":
        print("Opção inválida. Tente novamente.\n")

print("Programa encerrado.")