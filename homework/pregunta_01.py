"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

# Importamos pandas para manejar estructuras de datos tipo DataFrame
import pandas as pd

# Importamos re (expresiones regulares) para procesar texto y extraer información estructurada
import re


def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requerimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.
    """
    
    ruta = "files/input/clusters_report.txt"

    with open(ruta, encoding="utf-8") as f:
        lines = f.readlines()

    # Eliminamos encabezados
    content = ''.join(lines[4:])

    # Unimos todas las líneas y separamos bloques por cluster usando regex
    bloques = re.split(r"\n\s+(?=\d+\s{2,})", content.strip())

    datos = []

    for bloque in bloques:
        # Remover saltos de línea y unir en una sola línea
        bloque_unido = ' '.join(bloque.splitlines()).strip()

        # Usar expresión regular para extraer campos
        match = re.match(
            r"^\s*(\d+)\s{2,}(\d+)\s{2,}([\d,]+)\s?%\s{2,}(.*)$", bloque_unido
        )

        if match:
            cluster = int(match.group(1))
            cantidad = int(match.group(2))
            porcentaje = float(match.group(3).replace(',', '.'))
            palabras = match.group(4)

            # Limpiar espacios y puntos finales
            palabras = re.sub(r"\s+", " ", palabras).strip().rstrip('.')

            datos.append({
                "cluster": cluster,
                "cantidad_de_palabras_clave": cantidad,
                "porcentaje_de_palabras_clave": porcentaje,
                "principales_palabras_clave": palabras
            })

    df = pd.DataFrame(datos)

    return df
