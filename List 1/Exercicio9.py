#author: Braian

print('')
print('Exercício 1 - Escolher 3 numeros e o programa mostra o menor entre eles')
print('')
x = float(input("Digite o primeiro numero: "))
y = float(input("Digite o segundo numero: "))
z = float(input("Digite o terceiro numero: "))

if x < y < z:
    print('')
    print("O menor numero dentre os escolhidos é", x)
elif y < x < z:
    print('')
    print("O menor numero dentre os escolhidos é", y)
elif z < y < x:
    print('')
    print("O menor numero dentre os escolhidos é", z)
