# Validador triangulo

#Apresentação
print('\n\t\t\t -- Validador de Triângulo -- \n\n')

#Entrada
a = int(input('Informe o lado A: '))
b = int(input('Informe o lado B: '))
c = int(input('Informe o lado C: '))

#Processamento e Saída
if a < (b + c) and b < (a+b) and c < (a + c):
    print(f'\n\n {a}, {b} e {c} formam um Triângulo!')

if a == (b+c) or b == (a+c) or == c(a+b)
    print(f'\n\n {a} , {b} e {c} é um triangulo equilaterio')

if a == b  or b == a or != c(a+b)
    print('\n\n {a} , {b} e {c} é um triangulo isósceles')

if  a != (b+c)  or b != (a+c) or != c(b+a)
    print('f \n\n {a}, {b} e {c} é um triangulo escaleno')

else:
    print('\n\n não é um traingulo ')

