#author: brndsk
print("")
print("Altura máxima de um projétil")
print("")
hi = int(input("Qual altura inicial?: "))
vi = int(input("Qual velocidade inicial?: "))
t = float(input("Qual o tempo?: "))
g = 9.8
h=hi+vi*t-(g*t**2)/2
print('A altura maxima foi %.2f'%h)
