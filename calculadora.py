#!/usr/bin/env python3
"""
Calculadora simples em Python.
Realiza soma, subtração, multiplicação e divisão entre dois números.
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("não é possível dividir por zero.")
    return a / b


def ler_numero(mensagem):
    """Pede um número ao usuário até que ele digite um valor válido."""
    while True:
        valor = input(mensagem).replace(",", ".")
        try:
            return float(valor)
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 10 ou 2.5).")


def main():
    print("==============================")
    print("     CALCULADORA EM PYTHON    ")
    print("==============================")

    num1 = ler_numero("Digite o primeiro número: ")
    num2 = ler_numero("Digite o segundo número: ")

    print("\nEscolha a operação:")
    print("1 - Soma (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")
    opcao = input("Opção: ").strip()

    operacoes = {
        "1": ("+", somar),
        "2": ("-", subtrair),
        "3": ("*", multiplicar),
        "4": ("/", dividir),
    }

    if opcao not in operacoes:
        print("Opção inválida!")
        return

    simbolo, funcao = operacoes[opcao]
    try:
        resultado = funcao(num1, num2)
        print(f"Resultado: {num1:g} {simbolo} {num2:g} = {resultado:.2f}")
    except ZeroDivisionError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
