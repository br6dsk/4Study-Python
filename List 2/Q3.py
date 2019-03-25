from random import randint  #Importando bibioteca 
try: 
	import numpy as r      #Função try, para tentativa de importação da biblioteca
except:							#se o python não conseguir importar a biblioteca 
	print(" \nImporte a biblioteca numpy")      #O programa printa uma mensagem mandando importar
x = 0
user_input = str(input(' \nDeseja gerar uma matriz identidade? S/N → '))   #Pergunta se deseja gerar a matriz 
user_input = user_input.capitalize()    #função pra possibilitar o usuario digitar S maiusculo ou minusculo 
if user_input == 'S':    ##condição se ele digitar "s"
	while 1:						#repetição para a matriz
						#0            #1               #2
		matriz = [[randint(0,3),randint(0,10),randint(0,10)],   #0         
				[randint(0,10),randint(0,8),randint(0,10)], 	 #1			#Matriz que gera numeros aleatórios
				[randint(0,9),randint(0,10),randint(0,6)]]	 #2
		
		if matriz[0][0] == matriz[1][1] == matriz[2][2]:				#Condição para capturar a matriz identidade
			print(r.matrix(matriz))									#printar a matriz identidade
			x += 1											#contador pra travar o programa quando achar a Matriz
		elif x == 1:
			break													#break pra travar o codigo
else:
	print(' \nPrograma fechado')								#Condição caso a pessoa digite 'N', pra não gerar a matriz

		
