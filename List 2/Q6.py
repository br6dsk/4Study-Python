string_1 = input(" \nDigite a primeira palavra: ")  #variavel com uma input pra digitar a primeira palavra
string_2 = input(" \nDigite a segunda palavra: ") #variavel com uma input pra digitar a segunda palavra
string_3 = []
if len(string_1) < len(string_2): #condição pra ver se a primeira string é maior que a segunda
	for i in range(len(string_1)): #repetição para contagem das letras
		if string_1[i] in string_2: #condição pra ver se as letas da primeira string estão contidas na segunda string
			string_3.append(string_1[i]) #função pra adicionar as letras da primeira string na string gerada pelo programa
else:
	for i in range(len(string_2)):  #repetição pra cntagem da string 2
		if string_2 in string_1:  #condição pra ver se a string 2 ta na string 1
			string_3.append(string_2[i]) #condição pra adicionar as letras da string2 na string 3
string_4 = ' '.join(string_3)
print(string_4)