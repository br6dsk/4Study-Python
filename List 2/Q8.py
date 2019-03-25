frase = str(input(' \nDigite uma frase: ')) #Usuario digita a frase
letra = str(input(' \nQual letra deseja ver?: ')) #Usuario digita a letra 
print('A letra "{}" aparece {} vezes'.format(letra,frase.count(letra))) #função pra contar quantas vezes aparece a letra escolhida
