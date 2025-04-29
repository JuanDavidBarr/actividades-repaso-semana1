#1. Un usuario ingresa una contraseña. Verifica si la contraseña es igual a "1234".
contraseña_usuario = input("Ingrese su contraseña: ")
if contraseña_usuario == "1234":
    print("Acceso concedido")
else:
    print("Contraseña incorrecta")

    
#2. Pide un color favorito. Si no es "rojo", muestra "Ese no es el color que esperaba".
color_usuario = input("Ingrese su color favorito: ")
if color_usuario != "rojo":
    print(f"{color_usuario} no es el color que esperaba")
else:
    print("Rojo también es mi color favorito!")

    
#3. Un programa pide la edad de una persona. Si es mayor de 18, puede votar.
edad_usuario = int(input("Ingrese su edad: "))
if edad_usuario >= 18:
    print("Usted puede votar")
else:
    print("Usted no puede votar")

    
#4. Pide una temperatura. Si es menor a 0 grados, muestra "Hace frío".
temperatura_usuario = float(input("Ingrese la temperatura: "))
if temperatura_usuario < 0:
    print("Hace frío")
else:
    print("No está haciendo tanto frío")


#5. Pide dos números. Si ambos son mayores que 0, muestra "Ambos son positivos".
numero_1, numero_2 = int(input("Ingrese el número 1: ")), int(input("Ingrese el número 2: "))
if numero_1 > 0 and numero_2 > 0:
    print("Ambos números son positivos")
else:
    print("Al menos uno de ellos es negativo")

    
#6. Pide la hora. Si es menor que 12 o mayor que 18, muestra "No es hora de trabajar".
hora_usuario = int(input("Ingrese la hora en formato 24h: "))
if hora_usuario < 12 or hora_usuario > 18:
    print("No es hora de trabajar")
else:
    print("Es hora de trabajar")


#7. Pregunta si una persona tiene licencia y si lleva casco. Si no tiene licencia o no lleva casco, no puede conducir.
tiene_licencia, tiene_casco = input("Tiene usted licencia de conducción? (Si/No): "), input("Tiene usted casco? (Si/No): ")
if tiene_casco.lower() != "si" or tiene_licencia.lower() != "si":
    print("No puede conducir")
else:
    print("Puede conducir")


#8. Pregunta si una persona terminó su tarea. Si no terminó, mostrar "Debes terminar la tarea".
termino_tarea = input("Terminaste la tarea?(Si/No): ")
if termino_tarea.lower() != "si":
    print("Debes terminar la tarea")
else:
    print("Felicitaciones, ya terminaste")

    
#9. Pide una nota (0-10). Muestra si perdio, aprobado o sobresaliente.
nota_usuario = int(input("Ingrese su nota del (entre 1 y 10): "))
if nota_usuario < 7:
    print("Reprobó")
elif nota_usuario >= 7 and nota_usuario < 9:
    print("Aprobó")
elif nota_usuario >= 9 and nota_usuario <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida")

    
#10. Pide la edad y clasifica: niño, adolescente, adulto, anciano.
edad_usuario = int(input("Ingrese edad: "))
if edad_usuario < 13:
    print("Niño")
elif edad_usuario >= 13 and edad_usuario < 18:
    print("Adolescente")
elif edad_usuario >= 18 and edad_usuario < 60:
    print("Adulto")
else:
    print("Anciano")

    
#11. Crea una lista vacía y permite al usuario añadir 3 nombres.
lista = []
elementos_lista = range(3)
for n in elementos_lista:
    lista.append(input("Ingrese un nombre: "))
    
print(lista)


#12. Dada una lista de frutas, pide al usuario una fruta que quiera eliminar.
lista_frutas = ["mango", "guanabana", "papaya", "fresa"]
print(f"Lista de frutas {lista_frutas}")
fruta_eliminar = input("Ingrese la fruta que desea eliminar: ")
if fruta_eliminar in lista_frutas:
    lista_frutas.remove(fruta_eliminar.lower())
    print(f"Lista actualizada {lista_frutas}")
else:
    print(f"{fruta_eliminar} no se encuentra en la lista")

    
#13. Eliminar el último elemento de una lista.
lista_frutas = ["mango", "guanabana", "papaya", "fresa"]
print(f"Lista {lista_frutas}")
largo_lista = len(lista_frutas)
lista_frutas.remove(lista_frutas[largo_lista - 1])
print(f"Lista actualizada {lista_frutas}")


#14. Ordenar una lista de números de menor a mayor.
Lista_numeros = [8, 6, 9, 1, 7, 3, 5]
print(f"Lista con números desordenados {Lista_numeros}")
Lista_numeros.sort()
print(f"Lista con números ordenados {Lista_numeros}")


#15. Ordenar una lista de palabras alfabéticamente y luego al revés.
lista_frutas = ["mango", "guanabana", "papaya", "fresa"]
print(f"Lista sin orden alfabético {lista_frutas}")
lista_ordenada = sorted(lista_frutas)
print(f"Lista ordenada en orden alfabético {lista_ordenada}")
lista_ordenada.reverse()
print(f"Lista ordenada alfabéticamente pero al revés {lista_ordenada}")


#16. Buscar si un número existe en una lista y encontrar su posición.
lista = [5, 25, 85, 63, 45, 20, 0]
numero = int(input("Ingrese un número: "))
if numero in lista:
    posicion_numero = lista.index(numero)
    print(f"La posición de {numero} es {posicion_numero}")
else:
    print(f"El número {numero} no se encuentra en la lista")

    
#17. Contar cuántas veces aparece un nombre en la lista.
lista = ["juan", "pedro", "juan", "camilo", "mario"]
nombre_verificar = input("Ingrese el nombre que quiere verificar: ")
if nombre_verificar in lista:
    veces_aparece = lista.count(nombre_verificar)
    print(f"{nombre_verificar} aparece {veces_aparece} vez/veces")
else:
    print(f"{nombre_verificar} no está en la lista")


#18. Agregar un número en una posición específica.
Lista = [1, 2, 3, 4]
print(Lista)
numero_ingresar = int(input("Ingrese el número que desee ingresar: "))
posición = int(input("Ingrse la posición donde lo desea ingresar: "))
Lista.insert(posición, numero_ingresar)
print(Lista)


#19. Pide 5 números y crea una lista solo con los pares.
numero_1, numero_2, numero_3, numero_4, numero_5 = int(input("Ingrese un número: ")), int(input("Ingrese un número: ")), int(input("Ingrese un número: ")), int(input("Ingrese un número: ")), int(input("Ingrese un número: "))
lista_numeros = [numero_1, numero_2, numero_3, numero_4, numero_5]
lista_pares = []
for n in lista_numeros:
    if n % 2 == 0:
        lista_pares.append(n)
print(lista_pares)


#20. Combinar dos listas de palabras.
lista_1 = ["arroz", "sol", "mar", "martes"]
lista_2 = ["pepino", "burro", "dado", "nombre"]
print(f"Lista 1 antes de ser combinada con la lista 2 {lista_1}")
lista_1.extend(lista_2)
print(f"Lista 1 después de ser combinada con la lista 2 {lista_1}")




    


    
