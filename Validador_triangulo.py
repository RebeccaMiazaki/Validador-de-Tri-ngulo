# Validador triangulo

#Apresentação..
print('\n\t\t\t -- Validador de Triângulo -- \n\n')

#Entrada
a = int(input('Informe o lado A: '))
b = int(input('Informe o lado B: '))
c = int(input('Informe o lado C: '))

#Processamento e Saída
if a < (b + c) and c < (a + b):
    print(f'\n\n {a}, {b} e {c} formam um Triângulo!')

else:
    print('\n\n Não é um Triângulo.')