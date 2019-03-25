print('')
print('Impar ou Par?')
print('')
num = int(input("Digite um numero impar ou um numero par: "))
impar = num%2
if impar ==1:
    print('')
    print("O resto do numero", num, "e", impar, "entao", num, "e impar.")
elif impar != 1:
    print('')
    print("O numero", num, "nao e impar porque o resto nao e 1.")
