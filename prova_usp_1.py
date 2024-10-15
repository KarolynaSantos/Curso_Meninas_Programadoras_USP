# recebendo a lista
entrada = input()
lista_inicial = [int(x) for x in entrada.split(' ')]
lista_final = []

print('-', lista_inicial)
print('+', lista_final)

for x in range(len(lista_inicial)):

  lista_final.append(min(lista_inicial))
  lista_inicial.remove(min(lista_inicial))

  print('-', lista_inicial)
  print('+', lista_final)