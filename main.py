"""
Este script realiza una búsqueda en Archive.org utilizando la librería `internetarchive`, 
filtra los resultados que contienen 'chile' en su identificador, 
y descarga los archivos PDF relacionados a "Club Nintendo" en un directorio especificado.

El proceso incluye un retraso entre descargas para evitar bloqueos de la API.
"""
import time

from pathlib import Path
from internetarchive import search_items, get_item

# Inicializar arreglo de resultados filtrados
filtered_results = []
output_dir = Path("/tmp/Club Nintendo")  # Directorio donde se guardarán los archivos
DELAY = 2  # Retraso en segundos entre descargas

# Realizar búsqueda de "Club Nintendo"
for item in search_items('title:Club Nintendo'):
    # Verificar que el título y el identificador existan
    identifier = item.get('identifier')  # Recuperar el identificador
    if "chile" in identifier.lower():
        filtered_results.append(identifier)

# Mostrar la cantidad de resultados filtrados
print(f"Cantidad de resultados filtrados: {len(filtered_results)}")

# Proceso de descarga
# Crear el directorio
try:
    output_dir.mkdir(parents=True, exist_ok=True)
    print(f"Directorio creado en: {output_dir}")
except Exception as e:
    print(f"Error al crear el directorio: {e}")

for index, item_id in enumerate(filtered_results, start=1):
    print(f"[{index}/{len(filtered_results)}] Descargando el item: {item_id}")
    try:
        item = get_item(item_id)
        # Filtrar y descargar solo archivos .pdf que no contengan '_text' en su nombre
        files = item.files
        for file in files:
            if file['name'].endswith('.pdf') and '_text' not in file['name']:
                # Descargar el archivo .pdf si no tiene '_text' en el nombre
                item.download(glob_pattern=file['name'], destdir=output_dir, verbose=True)
                print(f"✔ Descarga completada para: {file['name']}")
    except Exception as e:
        print(f"❌ Error al descargar {item_id}: {e}")
    # Retraso entre descargas
    time.sleep(DELAY)

print("🎉 Todas las descargas han finalizado.")
