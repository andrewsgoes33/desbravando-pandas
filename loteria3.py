#Programinha para jogar na loteria e descobrir o número da sorte com somente 3 tentativas


def valida_entrada():
    
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 15 para ganhar: "))
            
        except ValueError:
            print("Valor Errado! Pedi um número!")
            continue
        
        if numero > 1 and numero < 15:
            return numero
        
        else:
            print("Entre com um número válido.")
            

numero_sorte = 7

for i in range(3):
    
    numero = valida_entrada()
        
    if numero == 7:
        print('Você Acertou!!')
        break
        
    elif numero > numero_sorte:
        print("Você erro! Tente um número menor!")
            
    else:
        print("Você errou! Tente um número maior!") 

