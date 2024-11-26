"""
EJERCICIO:
- Implementa un sistema para gestionar una biblioteca de libros desde la terminal.
- Permite realizar operaciones como añadir libros, buscar, actualizar y eliminar.
- Cada libro debe tener un título, un autor, y un año de publicación.
- Implementa validaciones para asegurarte de que los datos sean correctos:
  - El título no puede estar vacío.
  - El año debe ser un número y no puede ser mayor al año actual.
DIFICULTAD EXTRA (opcional):
- Permite listar los libros ordenados por título o año de publicación.
- Proporciona una opción para buscar libros por autor.
"""

from datetime import datetime

def library_manager():
    library = []

    def get_valid_title():
        """Solicita un título válido (no vacío)."""
        while True:
            title = input("Introduce el título del libro: ").strip()
            if title:
                return title
            else:
                print("El título no puede estar vacío.")

    def get_valid_author():
        """Solicita un autor válido (no vacío)."""
        while True:
            author = input("Introduce el autor del libro: ").strip()
            if author:
                return author
            else:
                print("El autor no puede estar vacío.")

    def get_valid_year():
        """Solicita un año de publicación válido."""
        current_year = datetime.now().year
        while True:
            year = input(f"Introduce el año de publicación (hasta {current_year}): ").strip()
            if year.isdigit() and 0 < int(year) <= current_year:
                return int(year)
            else:
                print(f"Año no válido. Debe ser un número entre 1 y {current_year}.")

    def add_book():
        """Añade un libro a la biblioteca."""
        title = get_valid_title()
        author = get_valid_author()
        year = get_valid_year()
        library.append({"title": title, "author": author, "year": year})
        print(f"Libro '{title}' añadido con éxito.")

    def search_book():
        """Busca un libro por título."""
        title = get_valid_title()
        results = [book for book in library if title.lower() in book["title"].lower()]
        if results:
            print("Libros encontrados:")
            for book in results:
                print(f"- {book['title']} de {book['author']} ({book['year']})")
        else:
            print("No se encontraron libros con ese título.")

    def update_book():
        """Actualiza los datos de un libro."""
        title = get_valid_title()
        for book in library:
            if title.lower() == book["title"].lower():
                print(f"Actualizando libro: {book['title']} de {book['author']} ({book['year']})")
                book["author"] = get_valid_author()
                book["year"] = get_valid_year()
                print("Libro actualizado con éxito.")
                return
        print("No se encontró un libro con ese título.")

    def delete_book():
        """Elimina un libro de la biblioteca."""
        title = get_valid_title()
        for book in library:
            if title.lower() == book["title"].lower():
                library.remove(book)
                print(f"Libro '{title}' eliminado con éxito.")
                return
        print("No se encontró un libro con ese título.")

    def list_books():
        """Lista todos los libros ordenados."""
        if not library:
            print("La biblioteca está vacía.")
            return

        print("\n1. Ordenar por título")
        print("2. Ordenar por año de publicación")
        option = input("Selecciona una opción: ").strip()

        if option == "1":
            sorted_library = sorted(library, key=lambda x: x["title"].lower())
        elif option == "2":
            sorted_library = sorted(library, key=lambda x: x["year"])
        else:
            print("Opción no válida. Mostrando sin ordenar.")
            sorted_library = library

        for book in sorted_library:
            print(f"- {book['title']} de {book['author']} ({book['year']})")

    def menu():
        """Muestra el menú y retorna la opción seleccionada."""
        print("\n1. Añadir libro")
        print("2. Buscar libro por título")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Listar libros")
        print("6. Salir")
        return input("Selecciona una opción: ")

    while True:
        option = menu()

        match option:
            case "1":
                add_book()
            case "2":
                search_book()
            case "3":
                update_book()
            case "4":
                delete_book()
            case "5":
                list_books()
            case "6":
                print("Saliendo del sistema de biblioteca.")
                break
            case _:
                print("Opción no válida. Elige una opción del 1 al 6.")

library_manager()
