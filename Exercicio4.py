soma_idades = 0
contador_idades = 0

while True:
    try:
        idade = int(input("Digite uma idade (ou -1 para gerar a media): "))
        
        if idade == -1:
            break
        
        if idade < 0:
            print("Idade inválida. Por favor, insira uma idade positiva.")
            continue
        
        soma_idades += idade
        contador_idades += 1
    
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")

if contador_idades > 0:
    media_idades = soma_idades / contador_idades
    print(f"A média das idades é: {media_idades}")
else:
    print("Nenhuma idade válida foi inserida.")
