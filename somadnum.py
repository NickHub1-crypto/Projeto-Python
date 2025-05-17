print("Soma dos números")
num1 = int(input("Digite um numero:"))
num2 = int(input("Digite outro numero:"))
soma = num1 + num2
print("A soma do numero {} + {} é = {}".format(num1, num2, soma))
if num1 > num2:
    print("O número {} e maior que o numero {}".format(num1, num2))
elif num1 < num2:
    print("O número {} e maior que o numero {}".format(num2, num1))
else:
    print("Os números são iguais!")