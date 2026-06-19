    
maxlibros=120
stocklibros=120
historial_prestamos=0
print("¡Bienvenido al sistema de gestión de préstamos de la Biblioteca Central! \n")
while True:
    print("===MENÚ PRINCIPAL===\n")
    print("1.	Libros disponibles")
    print("2.	Realizar préstamo")
    print("3.	Devolver préstamo")
    print("4.	Historial de préstamos")
    print("5.	Salir \n") 

    try:
        opcion = int(input("Seleccione una opción (1-5): \n"))
        if opcion < 1 or opcion > 5:
            print("¡Opción inválida! Por favor, seleccione una opción entre 1 y 5.")
        else:

            if opcion == 1:
                print("-----Libros disponibles:-----\n")
                print(f"Actualemnte, hay  {stocklibros} libros disponibles en la biblioteca.")
            elif opcion == 2:
                print("-----Realizar préstamo:-----\n")
                try:
                    numperstamo = int(input("Ingrese el número de libros a prestar: \n"))
                    if numperstamo < 1:
                        print("¡Número de libros inválido! Por favor, ingrese un número positivo para el préstamo.")
                    elif numperstamo > stocklibros:
                        print(f"¡No hay suficientes libros disponibles! Actualmente, hay {stocklibros} libros en stock.")
                    else:
                        prestamo=120-stocklibros
                        historial_prestamos+=1
                        print(f"Préstamo realizado con éxito. Quedan {prestamo} libros disponibles.")
                except:
                    print("¡Entrada inválida! Por favor, ingrese un número entero para el préstamo.")
            elif opcion == 3:
                print("-----Devolver préstamo:-----")
                try:
                    num_devolucion=int(input("Ingrese el número de libros a devolver: \n "))
                    if num_devolucion < 1:
                        print("¡Número de libros inválido! Por favor, ingrese un número positivo para la devolución.")  
                    elif num_devolucion > (maxlibros - stocklibros):
                        print(f"¡No se pueden devolver más libros de los prestados! Actualmente, hay {maxlibros - stocklibros} libros prestados. \n")
                    else:
                        stocklibros += num_devolucion
                        historial_prestamos-=1
                        print(f"Devolución realizada con éxito. Actualmente, hay {stocklibros} libros disponibles.\n")    
                except:
                    print("¡Entrada inválida! Por favor, ingrese un número entero para la devolución.")
                
                
            elif opcion == 4:
                print("-----Historial de préstamos:-----\n")
                print(f"Actualmente, hay {historial_prestamos} préstamos activos en la biblioteca."      )

            elif opcion == 5:
                print("¡Gracias por usar el sistema de biblioteca! ¡Hasta luego!")
                break                
    except:
        print("¡Opción inválida! Por favor, seleccione un número entre 1 y 5 para continuar.")
            
            
