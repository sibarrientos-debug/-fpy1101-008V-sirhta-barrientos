def menu_principal():
    print("===MENÚ PRINCIPAL===")
    print("1.	Libros disponibles")
    print("2.	Realizar préstamo")
    print("3.	Devolver préstamo")
    print("4.	Historial de préstamos")
    print("5.	Salir") 

maxlibros=120
stocklibros=120

while True:
    menu_principal()
    try:
        opcion = int(input("Seleccione una opción (1-5): "))
        if opcion < 1 or opcion > 5:
            print("¡Opción inválida! Por favor, seleccione una opción entre 1 y 5.")
        else:

            if opcion == 1:
                print("-----Libros disponibles:-----")
                print(f"Actualemnte, hay  {stocklibros} libros disponibles en la biblioteca.")
            elif opcion == 2:
                print("-----Realizar préstamo:-----")
                try:
                    numperstamo = int(input("Ingrese el número de libros a prestar: "))
                    if numperstamo < 1:
                        print("¡Número de libros inválido! Por favor, ingrese un número positivo para el préstamo.")
                    elif numperstamo > stocklibros:
                        print(f"¡No hay suficientes libros disponibles! Actualmente, hay {stocklibros} libros en stock.")
                    else:
                        stocklibros -= numperstamo
                        print(f"Préstamo realizado con éxito. Quedan {stocklibros} libros disponibles.")
                except:
                    print("¡Entrada inválida! Por favor, ingrese un número entero para el préstamo.")
            elif opcion == 3:
                print("-----Devolver préstamo:-----")
                try:
                    num_devolucion=int(input("Ingrese el número de libros a devolver: "))
                except:
                    print("¡Entrada inválida! Por favor, ingrese un número entero para la devolución.")
                
                if num_devolucion < 1:
                    print("¡Número de libros inválido! Por favor, ingrese un número positivo para la devolución.")  
                elif num_devolucion > (maxlibros - stocklibros):
            elif opcion == 4:
                print("-----Historial de préstamos:-----")
            elif opcion == 5:
                print("¡Gracias por usar el sistema de biblioteca! ¡Hasta luego!")
                break                
    except:
        print("¡Opción inválida! Por favor, seleccione un número entre 1 y 5 para continuar.")
            
            
