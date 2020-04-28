def inicio():

    '''STORSZ System Version 1.0'''

    print('Sistema de registro de estudiantes')
    print()
    print('Opciones')
    print()
    print('1 - Registrar estudiantes')
    print('2 - Consultar estudiante')
    print('3 - Borrar estudiante')
    print()


def registro_Estudiante():

    nombre_Estudiantes = []
    edad_Estudiantes = []
    curso_Alumno = []

    numstudent = int(input('Inserte el numero de estudiantes que vas a registrar: '))
    print()


    if numstudent > 199:

        print(' "No es recomendable insertar tantos estudiantes de un tiron, vayamos por partes!" ')
        print()
        new = input('Quieres intentarlo de nuevo? Si o NO:')
        print()
        new = new.lower()
        if new == 'si':
            registro_Estudiante()

    else:

        for x in range(numstudent):

            nombre = input('Inserte el nombre: ')

            if nombre in nombre_Estudiantes:
                denuevo = input('El nombre ya existe, Quieres intentarlo de nuevo? ')
                denuevo = denuevo.lower()
                if denuevo == 'si':
                    registro_Estudiante()
                if denuevo == 'no':
                    break


            edad = int(input('Inserte su edad: '))
            if edad <= 0 or edad >= 150 :
                print('Inserte su verdadera edad')

            curso = int(input('Inserte su curso: '))
            if curso > 10:
                print('Nivel no permitido')


            else:
                nombre_Estudiantes.append(nombre)
                edad_Estudiantes.append(edad)
                curso_Alumno.append(curso)
                print(f'Estudiantes registrados {nombre_Estudiantes}')
                print(f'Edades {edad_Estudiantes} ')
                print(f'Cursos {curso_Alumno}')



inicio()
opt = int(input('Inserte la opcion que desea: '))

if opt == 1:
    registro_Estudiante()





