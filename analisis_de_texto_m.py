import json


def obtener_texto():
    """Solicitar el nombre de un archivo .txt y leer su contenido"""
    while True:
        archivo_nombre = input("Por favor ingresa el nombre del archivo .txt para analizar: ").strip()
        try:
            with open(archivo_nombre, "r", encoding="utf-8") as archivo:
                texto = archivo.read().strip().lower()  # Lee el contenido del archivo
                if texto:
                    return texto
                else:
                    print("El archivo está vacío. Intenta con otro archivo.")
        except FileNotFoundError:
            print(f"No se encontró el archivo '{archivo_nombre}'. Intenta nuevamente.")
        except Exception as e:
            print(f"Ocurrió un error: {e}. Intenta nuevamente.")


def obtener_letras():
    """Solicita letras al usuario para contar en el texto y valida la entrada"""
    while True:
        try:
            cantidad = int(input("¿Cuántas letras deseas analizar? "))
            if cantidad <= 0:
                print("Debes ingresar al menos una letra.")
                continue
            letras = [input(f"Ingrese la letra {i + 1}: ").strip().lower() for i in range(cantidad)]
            return letras
        except ValueError:
            print("Ingresa un número válido.")


def analizar_texto(texto, letras):
    """Realiza el análisis del texto y devuelve los resultados"""
    texto_lista = texto.split()
    resultados = {
        "cantidad_palabras": len(texto_lista),
        "primer_letra": texto[0],
        "ultima_letra": texto[-1],
        "texto_invertido": " ".join(texto_lista[::-1]),
        "contar_letras": {letra: texto.count(letra) for letra in letras},
        "contiene_python": "python" in texto
    }
    return resultados


def guardar_resultados(resultados):
    """Guarda los resultados en un archivo JSON"""
    with open("analisis_texto.json", "w", encoding="utf-8") as archivo:
        json.dump(resultados, archivo, indent=4, ensure_ascii=False)
    print("\nResultados guardados en 'analisis_texto.json'.")


def main():
    texto = obtener_texto()  # Ahora obtiene el texto de un archivo
    letras = obtener_letras()  # Pide las letras a analizar
    resultados = analizar_texto(texto, letras)  # Analiza el texto

    print("\nResultados del análisis:")
    for clave, valor in resultados.items():
        print(f"{clave}: {valor}")

    guardar_resultados(resultados)  # Guarda los resultados en un archivo JSON


if __name__ == "__main__":
    main()

