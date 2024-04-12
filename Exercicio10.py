lista = [2, 4, 7, 2, 3, 3, 1, 0, 2, 6]

frequencia = {}

for numero in lista:
    if numero in frequencia:
        frequencia[numero] += 1
    else:
        frequencia[numero] = 1

numero_mais_frequente = max(frequencia, key=frequencia.get)
frequencia_maxima = frequencia[numero_mais_frequente]

print(f"Dada a lista {lista}, o número que se repete mais vezes é {numero_mais_frequente}, que aparece {frequencia_maxima} vezes.")
