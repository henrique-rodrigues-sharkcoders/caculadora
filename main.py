from math import sqrt
while True:
    print("1-soma")
    print("2-subtração")
    print("3-multiplicação")
    print("4-divisão")
    print("5-potenciação")
    print("6-resto")
    print("7-sair")
     op = int(input("Escolha a operação que deseja: "))

    if op == 1:
        n1 = int(input("Escolhe o primeiro número: "))
        n2 = int(input("Escolhe o segundo número: "))
        print(n1 + n2)
    elif op == 2:
        n1 = int(input("Escolhe o primeiro número: "))
        n2 = int(input("Escolhe o segundo número: "))
        print(n1 - n2)
    elif op == 3:
        n1 = int(input("Escolhe o primeiro número: "))
        n2 = int(input("Escolhe o segundo número: "))
        print(n1 * n2)
    elif op == 4:
        n1 = int(input("Escolhe o primeiro número: "))
        n2 = int(input("Escolhe o segundo número: "))
        print(n1 / n2)
    elif op == 5:
        n1 = int(input("Escolhe o primeiro número: "))
        n2 = int(input("Escolhe o segundo número: "))
        print(n1 ** n2)
    elif op == 6:
        n1 = int(input("Escolhe o primeiro número: "))
        n2 = int(input("Escolhe o segundo número: "))
        print(n1 % n2)
    elif op == 7:
        exit()
    else:
        print("operação inválida.")
