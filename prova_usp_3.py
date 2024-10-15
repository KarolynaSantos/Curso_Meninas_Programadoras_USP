def binary_extraction_par(lista, elementos, meio):
  
  lista_final = []
  lista_final.append(lista[meio])

  elemento = 1

  while True:
    if len(lista_final) == elementos:
      break
    
    lista_final.append(lista[meio - elemento])

    if len(lista_final) == elementos:
      break

    lista_final.append(lista[meio + elemento])

    elemento +=1
  
  return lista_final

def binary_extraction_impar(lista, elementos, meio):
  
  lista_final = []
  lista_final.append(lista[meio])

  elemento = 1

  while True:
    if len(lista_final) == elementos:
      break
    
    lista_final.append(lista[meio + elemento])

    if len(lista_final) == elementos:
      break

    lista_final.append(lista[meio - elemento])

    elemento +=1
  
  return lista_final

def binary_extraction(entrada, elementos):

  lista_inicial = [int(x) for x in entrada.split(' ')]

  meio = int(len(lista_inicial) / 2)
  if elementos == 0:
    resultado = []
  elif len(lista_inicial) % 2 == 0:
    resultado = binary_extraction_par(lista_inicial, elementos, meio)
  else:
    resultado = binary_extraction_impar(lista_inicial, elementos, meio)
  
  print(lista_inicial)
  print(resultado)

# recebendo a lista
# entrada = input()

valores = input()
elementos = int(input())
binary_extraction(valores, elementos)