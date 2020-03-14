import re
cadena = (open("c:/Users/Camil/Documents/semestre 7/inteligenica/DonQuijote.txt",mode="r",encoding="utf-8")).read()
print(cadena)
saltos=re.findall("\n",cadena) 
print("Los saltos de linea son:", len(saltos))
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print("Este es el conteo de las palabras:",word_count(cadena))