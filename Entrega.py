biblioteca = {

    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

def agregar_libro(biblioteca):
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación: "))
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    return biblioteca
    agregar_libro(biblioteca)
    print(biblioteca)

biblioteca = {

    "Cien años de soledad": {"autor": "Gabriel García Márquez", "año": 1967, "disponible": True},
    "1984": {"autor": "George Orwell", "año": 1949, "disponible": True},
    "El principito": {"autor": "Antoine de Saint-Exupéry", "año": 1943, "disponible": False}
}

def agregar_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    año = int(input("Ingrese el año de publicación: "))
    biblioteca[titulo] = {"autor": autor, "año": año, "disponible": True}
    print("Libro agregado exitosamente.")

def prestar_libro():

    titulo = input("Ingrese el título del libro a prestar: ")
    if titulo in biblioteca:
        biblioteca[titulo]["disponible"] = False
        print("Libro prestado.")
    else:
        print("El libro no se encuentra en la biblioteca.")
def devolver_libro():
    titulo = input("Ingrese el título del libro a devolver: ")
    if titulo in biblioteca:
        biblioteca[titulo]["disponible"] = True
        print("Libro devuelto.")
    else:
        print("El libro no se encuentra en la biblioteca.")

def mostrar_libros():
    for titulo, info in biblioteca.items():
        print(f"Título: {titulo}")
        print(f"Autor: {info['autor']}")
        print(f"Año: {info['año']}")
        print(f"Disponible: {info['disponible']}")
        print("-" * 20)

def buscar_por_año():
    año_buscado = int(input("Ingrese el año de publicación: "))
    print(f"Libros publicados en {año_buscado}:")
    for titulo, info in biblioteca.items():
        if info['año'] == año_buscado:
            print(f"Título: {titulo}")
            print(f"Autor: {info['autor']}")
            print("-" * 20)
while True:
    print("\nMenú:")
    print("1. Agregar un nuevo libro")
    print("2. Prestar un libro")
    print("3. Devolver un libro")
    print("4. Ver todos los libros")
    print("5. Buscar libros por año")
    print("6. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == '1':
        agregar_libro()
    elif opcion == '2':
        prestar_libro()
    elif opcion == '3':
        devolver_libro()
    elif opcion == '4':
        mostrar_libros()
    elif opcion == '5':
        buscar_por_año()
    elif opcion == '6':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
