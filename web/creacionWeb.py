import json
import os

# --- Configuraciones ---
# Obtiene la ruta del directorio donde se encuentra el script actual
directorio_actual = os.path.dirname(os.path.abspath(__file__)) 
RUTA_JSON = os.path.join(directorio_actual, 'catalogo\catalogo.json')
DIRECTORIO_SALIDA = os.path.join(directorio_actual, 'productos')
RUTA_SCRIPT_JS = '../js/producto.js'
RUTA_CSS = '../style.css'
IMAGEN_DEFAULT = '../image/imgNoEncontrada.png' # Usamos la de fallback si no hay URL

# --- Plantilla HTML ---
PLANTILLA_HTML = """
<!doctype html>
<html lang="es">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
  
  <link rel="stylesheet" href="{RUTA_CSS}">
  
  <title>Detalle: {NOMBRE_PRODUCTO}</title>
</head>
<body class="container my-5">
    <div class="row">
        <div class="col-md-6">
            <img src="{URL_IMAGEN}" class="img-fluid rounded shadow-sm" alt="{NOMBRE_PRODUCTO}" id="producto-img">
        </div>
        
        <div class="col-md-6">
            <h1 class="display-4 mb-3">{NOMBRE_PRODUCTO}</h1>
            <hr>
            <p class="lead"><strong>Tipo:</strong> {TIPO}</p>
            <p class="lead"><strong>Piedra:</strong> {PIEDRA}</p>
            <p class="lead"><strong>ID:</strong> {ID}</p>
            
            <h2 class="h4 mt-4">Comentarios:</h2>
            <p>{COMENTARIO}</p>
            
            <button id="comprar-btn" class="btn btn-lg btn-success mt-4">Añadir al Carrito</button>
            <a href="../index.html" class="btn btn-lg btn-secondary mt-4 ms-2">Volver al Catálogo</a>
        </div>
    </div>

    <script src="{RUTA_SCRIPT_JS}"></script>
    <script>
        // Si la imagen falla en cargar, usa la imagen de fallback
        document.getElementById('producto-img').onerror = function() {{
            this.src = '{IMAGEN_DEFAULT}';
        }};
    </script>
</body>
</html>
"""
# --- Fin de la Plantilla HTML ---

def generar_paginas():
    """Lee el JSON y genera un archivo HTML para cada producto."""
    
    # 1. Crear el directorio de salida si no existe
    if not os.path.exists(DIRECTORIO_SALIDA):
        os.makedirs(DIRECTORIO_SALIDA)
        print(f"Directorio de salida '{DIRECTORIO_SALIDA}' creado.")

    # 2. Cargar datos del JSON
    try:
        with open(RUTA_JSON, 'r', encoding='utf-8') as f:
            productos = json.load(f)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {RUTA_JSON}.")
        return
    except json.JSONDecodeError:
        print(f"Error: El archivo {RUTA_JSON} no es un JSON válido.")
        return

    # 3. Iterar y generar archivos
    contador_archivos = 0
    for producto in productos:
        # Extraer datos, usando el índice [0] como requiere tu formato JSON
        id_prod = str(producto.get('id', [None])[0])
        tipo = producto.get('tipo', ['N/A'])[0]
        nombre = producto.get('nombre', ['Sin Nombre'])[0]
        piedra = producto.get('piedra', ['N/A'])[0]
        comentario = producto.get('comentario', [''])[0]
        url_imagen = producto.get('url', IMAGEN_DEFAULT) # Usa el URL del JSON o el default
        
        # Validar ID
        if id_prod == 'None':
            print(f"Advertencia: Se saltó un producto sin ID. {producto}")
            continue

        # Crear el nombre del archivo
        nombre_archivo = os.path.join(DIRECTORIO_SALIDA, f"{id_prod}.html")
        
        # Formatear la plantilla con los datos del producto
        contenido_html = PLANTILLA_HTML.format(
            ID=id_prod,
            TIPO=tipo,
            PIEDRA=piedra,
            NOMBRE_PRODUCTO=nombre,
            COMENTARIO=comentario,
            URL_IMAGEN=url_imagen,
            RUTA_SCRIPT_JS=RUTA_SCRIPT_JS,
            RUTA_CSS=RUTA_CSS,
            IMAGEN_DEFAULT=IMAGEN_DEFAULT
        )

        # Escribir el archivo HTML
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(contenido_html)
        
        contador_archivos += 1
        break # Quitar este break para procesar todos los productos

    print(f"\n--- Proceso Finalizado ---")
    print(f"Se generaron {contador_archivos} páginas de detalle en la carpeta '{DIRECTORIO_SALIDA}'.")
    print("¡Listo para subir a producción!")

if __name__ == "__main__":
    generar_paginas()