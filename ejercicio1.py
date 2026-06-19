print("----Bienvenido al sistema de registro médico!----")
while True:
    try:
        cantidad_medicos=int(input("Cuántos médicos desea registrar: "))
        if cantidad_medicos <=0:
            print("¡Registro médico inválido! Por favor, ingrese un número positivo para continuar.")
        else:
           break
    except:
         print("¡Registro médico inválido! Por favor, ingrese un valor numérico para continuar.")        
medico_residentes=0
medico_especialistas=0

for i in range(cantidad_medicos):
    while True:
        print("----Registro por médico: ----")
        #Solicitar nombre del médico
        nombre_medico=input(f"Ingrese el nombre del médico {i+1} (6 caracteres o más, No debe incluir espacios):  ")
        if (len(nombre_medico) < 6 ) or (" " in nombre_medico):
         print("¡Registro médico inválido! El nombre del médico debe tener al menos 6 caracteres y no debe contener espacios. Por favor, intente nuevamente.")
        else:
            break
   

    while True:
        try:
            años_experiencia = int(input(f"Ingrese los años de experiencia clínica del médico {i + 1}: "))   
            if años_experiencia <= 0:
               print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
            else:
                if años_experiencia >= 5:
                    medico_residentes += 1
                else:
                    medico_especialistas += 1
                break
        except:
            print("¡Error clínico! Ingresa un número entero positivo para la experiencia.")
print(f"¡El hospital cuenta con {medico_especialistas} Especialistas Senior y {medico_residentes} Residentes Junior! ¡Sistema listo para operar!")
