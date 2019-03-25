#author: Braian
print('')
print("Juros, montante e etc")
print('')
valor = float(input("Valor principal investido: "))
dias = int(input("Dias investido: ")) 
form = valor*(1+((10.5/365)*dias))
print("")
print("Seu montante é de: R$%.2f" %form)
