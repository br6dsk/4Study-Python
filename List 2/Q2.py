



lista = [1, 2, 3, 4] #Vetor com os numeros
lista.append(0) #abre espaço para inserir o novo elemento
pos = int(input(' \nDigite a posição: ')) #input pra enviar a posição do numero
for i in range(len(lista)-1, pos-1, -1): #substiuição dos numeros 
	lista[i] = lista[i-1]
lista[pos] = int(input('digite o numero: ')) #input pra digitar o numero
print(lista) 


