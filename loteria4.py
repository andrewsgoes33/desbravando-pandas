#Programinha para jogar na loteria e descobrir o número da sorte com somente 3 tentativas
#

def check_input():
    
    while True:
        try:
            numero = int(input("Digite um número entre 1 e 15 para ganhar: "))
            return numero
        
        except ValueError:
            return "Não é aceito letras :/ Digite um número correto!"
        
def check_range(numero):
    
    if 1 <= numero <= 15:
        return numero
    else:
        return print("Valor incorreto, digite números entre 1 e 15 somente!!")

def valida_entrada():
    
    while True: 
        numero = check_input()
    
        if type(numero) != int:
            print(numero)
            continue
        
        if check_range(numero):
            return numero
         

numero_sorte = 7
tentativas = 0

for i in range(3):
    
    numero = valida_entrada()
        
    if numero == 7:
        print('Você Acertou!! Parabéns!!!!')
        break
        
    elif numero > numero_sorte:
        tentativas = tentativas + 1
        if tentativas == 3:
            print("Acabaram suas tentativas! GAME OVER")
        else:    
            print("Você errou! Tente um número menor!")
            
    else:
        tentativas = tentativas + 1
        if tentativas == 3:
            print("Acabaram suas tentativas! GAME OVER")
        else:    
            print("Você errou! Tente um número Maior!")
        
    
        
    
