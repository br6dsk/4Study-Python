palavras = [] #Vetor pra adicionar palavras
vogais = ['a', 'e', 'i', 'o', 'u'] #Vetor mostrando as vogais
for i in range(5): #repetição 
	palavra = input(' \nDigite uma palavra: ') #O usuario envia uma palavra
	if palavra[0] in vogais: #condição
		palavra = palavra.upper() #função pra por  a palavra maiuscula
		palavras.append(palavra) #função pra adicionar no vetor
	else:
		palavras.append(palavra) 
print(palavras) #printando o vetor