import os
import sqlite3
import msvcrt

def buscaralumno(nombre):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "colegio.db")
    row=[]
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        rows = cursor.execute(f'SELECT * FROM Alumnos WHERE nombre = "{nombre}"')
        row = list(rows)
    return row

def crearalumno(id, nombre, apellido):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    db_path = os.path.join(BASE_DIR, "colegio.db")
    with sqlite3.connect(db_path) as db:
        cursor = db.cursor()
        cursor.execute(f'INSERT INTO Alumnos(id,nombre,apellido) VALUES({id},"{nombre}","{apellido}")')

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')    

def main():
    clearConsole()
    print("1. ver alumno")
    print("2. ingresar alumno")
    print("cualquier otra numero finaliza")
    
    opc = int(input("digite una opcion: "))
    match opc:
        case 1:
            clearConsole()
            print("*** VER ALUMNO ***")
            nombre = input("digite un nombre: ")
            alumno = buscaralumno(nombre)
            print(f'id: {alumno[0][0] }  -  nombre: {alumno[0][1]}  -  apellido: {alumno[0][2] }')
            print("Presione una tecla para continuar...")
            msvcrt.getch()
            main()
        case 2:
            clearConsole()
            print("*** CREAR ALUMNO ***")
            id = int(input("inserte id: "))
            nombre = input("agregue el nombre: ")
            apellido = input("agregue el apellido: ")
            crearalumno(id, nombre, apellido)
            print("Presione una tecla para continuar...")
            msvcrt.getch()
            main()
        case _:
            pass


if __name__ == "__main__":
    main()
