print("Calculadora Simples")
numero1 = 0
numero2 = 0
numero3 = 0
resultado = 0
operacao = ' '

while True:
    numero1 = int(input('Digite o número 1:'))
    operacao = input('Digite a operacao: ')
    numero2 = int(input('Digite o numero 2: '))
    numero3 = int(input('Digite o numero 3: '))

if operacao == ' + ':
    resultado = numero1 + numero2 + numero3
elif operacao == ' - ':
    resultado = numero1 - numero2 - numero3
elif operacao == ' / ':
    resultado = numero1 / numero2 / numero3
elif operacao == ' * ':
    resultado = numero1 * numero2 * numero3
else:
    resultado = "Operação Inválida"

print(str(numero1) + ' ' + str(operacao) + ' ' + str(numero2) + '=' + str(numero3) + str (resultado))