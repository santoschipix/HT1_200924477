import os
# alfabeto
alfabeto = {'1': 0,'0': 1 }
# creación de la matriz de estados
matrizbinariosimpar = []  # 1, 0
matrizbinariosimpar.append([1, 0])  # S0
matrizbinariosimpar.append([2, 2])  # S1
matrizbinariosimpar.append([3, 3])  # S2
matrizbinariosimpar.append([2, 2])  # S3
# estado de aceptación
aceptacion = [3]
# navegación del estado (e) actual con el valor (v)
def mueve(e, v):
    v = alfabeto[v]
    return matrizbinariosimpar[e][v]

mientras = True
os.system("clear")
print("****************************************************")
print("Santos Geovani Chipix Llamas - 200924477")
print("****************************************************")
print("AFD que acepta cadenas de números binarios impares "
      "\ncon más de 2 dígitos y que inicien con 1")
print("****************************************************")
print("\t\t\tHoja de trabajo 1")

while mientras:
    inicial = 0
    cadena = input("\nIngrese la cadena a validar: ")
    if cadena == "":
        mientras = False
        break;
    for i in cadena:
        inicial = mueve(inicial, i)

    if inicial in aceptacion:
        print("La cadena ", cadena, " Es válida")

    else:
        print("La cadena ", cadena, " Es inválida")
