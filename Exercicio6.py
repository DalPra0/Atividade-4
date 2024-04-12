numeros_no_intervalo = 0
numeros_fora_do_intervalo = 0

for _ in range(10):
    numero = float(input("Digite um número: "))
    
    if 10 <= numero <= 20:
        numeros_no_intervalo += 1
    else:
        numeros_fora_do_intervalo += 1

print(f"Números no intervalo [10, 20]: {numeros_no_intervalo}")
print(f"Números fora do intervalo [10, 20]: {numeros_fora_do_intervalo}")
