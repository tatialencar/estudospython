import os

class Calculadora:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2

    def somar(self):
        return self.numero1 + self.numero2

    def subtrair(self):
        return self.numero1 - self.numero2

    def multiplicar(self):
        return self.numero1 * self.numero2

    def dividir(self):
        if self.numero2 != 0:
            return self.numero1 / self.numero2
        else:
            return "Erro: divisão por zero"

# Programa principal
print("🔢 Calculadora Python - Orientada a Objetos (Google Colab)")


n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

calc = Calculadora(n1, n2)
opcao = ""

while opcao != "5":
    os.system('cls' if os.name == 'nt' else 'clear')
 # limpa antes de mostrar o menu

    print("🔢 Calculadora Python (Google Colab)")
    print("Números escolhidos: ", n1, "e", n2)
    print("\nEscolha a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")

    print("\n🔎 Resultado:")
    if opcao == "1":
        print("Soma:", calc.somar())
    elif opcao == "2":
        print("Subtração:", calc.subtrair())
    elif opcao == "3":
        print("Multiplicação:", calc.multiplicar())
    elif opcao == "4":
        print("Divisão:", calc.dividir())
    elif opcao == "5":
        print("👋 Saindo da calculadora... até logo!")
    else:
        print("❌ Opção inválida. Tente novamente.")

    # Pausa antes de repetir, mas sem limpar a tela após o ENTER
    if opcao != "5":
       n1 = float(input("Digite o primeiro número: "))
       n2 = float(input("Digite o segundo número: "))

       calc = Calculadora(n1, n2)
       opcao = ""
       os.system('cls' if os.name == 'nt' else 'clear')