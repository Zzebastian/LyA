import json, csv, os

# Obtiene la ruta del directorio donde se encuentra el script actual
directorio_actual = os.path.dirname(os.path.abspath(__file__)) 
# O copia la ruta de acceso a la carpeta donde se encuentren los archivos

# Construye las rutas completas usando el directorio actual O COPI
ruta_json = os.path.join(directorio_actual, 'catalogo.json')
ruta_csv = os.path.join(directorio_actual, 'catalogo.csv')
print(ruta_json)

productos = []
# 4. Leer el archivo CSV e insertar los datos
with open(ruta_csv, 'r', encoding='utf-8') as archivo_csv:
    lector_csv = csv.reader(archivo_csv)
    # Ignora la primera fila que contiene los encabezados.
    next(lector_csv) 
    
        
    # Itera sobre cada fila del CSV
    for fila in lector_csv:
        # Asegúrate de que la fila tenga 6 columnas
        try:
            id_producto = int(fila[0])
            
            if len(fila) == 6:
                # Crea la URL de la imagen a partir del ID (fila[0])
                url_imagen = f"./LyA/web/img/{fila[0]}.png"
            
                # Crea una tupla con los datos en el orden correcto para la base de datos.
                # CSV: id, Tipo, Nombre, Piedra, Comentario
                # JSON: id, tipo, nombre, piedra, comentario, imagen_url
                prod= {}
                prod["id"] = id_producto,    # id
                prod["tipo"] = fila[1],    # tipo
                prod["nombre"] = fila[2],    # nombre
                prod["piedra"] = fila[3],    # piedra
                prod["comentario"] = fila[4],    # comentario
                prod["url"] = "./image/pulsera.png" #url_imagen  # imagen_url
                productos.append(prod)
        except:
            print(fila)
            continue

with open(ruta_json, 'w') as outfile:
                    archivo = json.dump(productos,outfile)

print("Base de datos creada exitosamente desde el archivo CSV.")