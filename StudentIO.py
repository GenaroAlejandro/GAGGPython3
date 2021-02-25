import pickle
from IDestudiante import estudiante as est

def registro(file):
    print("Introduce el nombre del estudiante:")
    nombre = input()
    estudiante = est(nombre)
    registro = pickle.dump(estudiante, file)
    return registro

def lectura(file):
    file.seek(0)
    unpickler = pickle.Unpickler(file)
    read_estudiante = unpickler.load()
    print(f'El nombre del estudiantes es: {read_estudiante.getDatos()}')

def actualizar(file,rename):
    file.seek(0)
    unpickler = pickle.Unpickler(file)
    rename_estudiante = unpickler.load()
    rename_estudiante.setDatos(rename)
    print(f"Nombre actualizado: {rename_estudiante.getDatos()}")


if __name__ == '__main__':
    for i in range(5):
        with open('Estudiantes.db','ab+') as file:
            # Registro
            reg = registro(file)
            # Lectura
            lectura(file)
            # Actualizar
            print("Por que valor lo deseas actualizar?:")
            rename = input()
            actualizar(file,rename)



    """
    for i in range (5):
        print(f'Ingrese el nombre del estudiante {i+1}:')
        nombre = input()
        print(f'Ingrese el correo del estudiante {i+1}:')
        correo = input()
        e = est(nombre, correo)
        with shelve.open("students.db") as estudiante:
            estudiante[nombre] = e

    with shelve.open("students.db") as estudiante:
        for os in estudiante:
            print(f'{os}:{objeto_shelve}')
    """
