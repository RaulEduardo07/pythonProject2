#Sistema que simula uma calculadora

print("Bem vindo(a)s a calculadora!")

#entrada de dados

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
operação = input("+, -, *, /: ")

if(operação == '+'):
    resultado = numero1 + numero2

elif(operação == '-'):
    resultado = numero1 - numero2

elif(operação == '*'):
    resultado = numero1 * numero2
else:
    resultado = numero1 / numero2

print("Resultado: ", resultado)