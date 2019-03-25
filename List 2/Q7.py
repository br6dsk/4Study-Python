def remove_repetidos(lista): #função definida pra remover numero repetido
    vetor = []
    for i in lista:
        if i not in vetor: #condição pra verificar se o "i"(numero) está no "vetor"
            vetor.append(i) #Se não tiver, o "i"(numero) é adicionado!
    return vetor #Aqui ele retorna  a função
lista = [1, 1, 2, 1, 3, 4, 3, 6, 7, 6, 7, 8, 10 ,9] #lista de numeros repetidos
lista = remove_repetidos(lista) #aplicando a função criada
print (lista) #printando a lista