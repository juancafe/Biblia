# En Python 3.x Leo y despliego contenido de un .txt
fh = open("biblia.txt", "r")
# Inicializo Contadores 
countl = 0
countw = 0
palabras=dict()
# Recorro las lineas
for linea in fh:
    # Despliego linea
    # print(linea.strip())
    # Cuento lineas
    countl = countl + 1
    if countl==1000:
        break
    # Separo linea en palabras
    linea=linea.split()
    # Recorro cada palabra en la linea
    for palabra in linea:
        #print(palabra)
        # Acumulo palabras
        palabras[palabra]=palabras.get(palabra,0)+1
        countw=countw+1

print(countl,"Lineas")
print(countw,"Palabras")
print('Total Palabras distintas:',len(palabras))
print('Total Palabras distintas:',len(palabras.keys()))
print('Total Palabras:',palabras)
# Ordeno Diccionario
sorted_dict = {} # dict1 = {1: 1, 2: 9, 3: 4}
sorted_keys = sorted(palabras, key=palabras.get)  # [1, 3, 2]

for w in sorted_keys:
    sorted_dict[w] = palabras[w]

print(sorted_dict) # {1: 1, 3: 4, 2: 9}

