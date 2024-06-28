#Programinha para jogar na loteria e descobrir o número da sorte com somente 3 tentativas


numero_sorte = 7

for i in range(3):
    
    while True:
        try:
            numero = int(input("Digite um número para ganhar: "))
            break
        
        except ValueError:
            print("Valor Errado! Pedi um número!")
            
        
    if numero == 7:
        print('Você Acertou!!')
        break
        
    elif numero > numero_sorte:
        print("Você erro! Tente um número menor!")
            
    else:
        print("Você errou! Tente um número maior!") 

