#Programinha para jogar na loteria e descobrir o número da sorte com somente 3 tentativas
numero = int(input("Digite um número para ganhar: "))

numero_sorte = 7

for i in range(3):
    
    if numero == 7:
        print('Você Acertou!!')
        break
    
    elif numero > numero_sorte:
        print("Você erro! Tente um número menor!")
        
    else:
        print("Você errru! Tente um número maior!") 
