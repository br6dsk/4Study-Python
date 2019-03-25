#Import math, para importar uma biblioteca matemática.
import math 
v = [] #Vetor onde será adicionado os numeros
n = 0 #Numero de valores
soma = 0
while True: #Repetição sempre verdadeira com uma condição 
	num = int(input(' \nDigite um numero: '))
	if num == -1: #Condição pra quebrar a repetição
		break
	n+=1
	v.append(num) #função pra adicionar o numero digitado pelo usuario no vetor
	m = sum(v)/n #obtenção da média
	dp = math.sqrt(((num-m)**2)/n) #formula de desvio padrão
print(f' \nO vetor é {v}') #printando o vetor
print(f' \nA media é {m}') #printando a media
print(f' \nO desvio padrão é {dp}') #printando o desvio padrão


