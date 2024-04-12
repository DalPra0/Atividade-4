import time

while True:
    numero = int(input("Digite um número inteiro entre 1 e 10: "))
    
    if 1 <= numero <= 10:
        break
    else:
        print("Valor inválido. Por favor, insira um número entre 1 e 10.")

print(f"Tabuada de {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    time.sleep(0.1)
