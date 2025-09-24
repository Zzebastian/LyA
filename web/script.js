// Variable global para almacenar todos los productos
let productos = [];
let productosFiltrados = []; // Almacena el resultado del filtro actual
let productosMostrados = 0; // Contador de productos mostrados

const PRODUCTOS_POR_CARGA = 20; // Define cuántos productos se muestran por tanda

// URL de la imagen de fallback
const IMG_NO_ENCONTRADA_URL = "./image/imgNoEncontrada.png";

// Función principal para cargar el catálogo
async function generarCatalogo(url) {
  try {
    const respuesta = await fetch(url);
    const datos = await respuesta.json();

    // Asigna los datos (el array completo) a la variable global
    productos = datos;
    productosFiltrados = [...productos]; // Inicialmente, todos los productos están filtrados

    // Genera la vista inicial
    generarProductos(productosFiltrados);

    // Asigna los escuchadores de eventos a los menús desplegables
    asignarEventListeners();

    // Añade el escuchador de eventos para el scroll
    window.addEventListener('scroll', cargarMasProductos);

  } catch (error) {
    console.error("Error al cargar el catálogo:", error);
  }
}

// Función para generar las tarjetas de producto en el HTML
function generarProductos(listaDeProductos) {
  const contenedor = document.getElementById("catalogo-container");
  contenedor.innerHTML = ""; // Limpia el contenedor antes de agregar nuevos productos
  productosMostrados = 0; // Reinicia el contador de productos mostrados

  if (listaDeProductos.length === 0) {
    contenedor.innerHTML = "<p class='text-center fs-4 text-muted'>No se encontraron productos que coincidan con los filtros.</p>";
    return;
  }

  // Agrega la primera tanda de productos
  agregarProductos(listaDeProductos);
}

// Nueva función para agregar productos de forma incremental
function agregarProductos(listaDeProductos) {
  const contenedor = document.getElementById("catalogo-container");
  const finDeCarga = Math.min(productosMostrados + PRODUCTOS_POR_CARGA, listaDeProductos.length);

  for (let i = productosMostrados; i < finDeCarga; i++) {
    const producto = listaDeProductos[i];
    // Accede a los valores dentro de los arrays del JSON
    const id = producto.id[0];
    const tipo = producto.tipo[0];
    const nombre = producto.nombre[0];
    const piedra = producto.piedra[0];
    const comentario = producto.comentario[0];
    const url_imagen = producto.url;

    // Crea la tarjeta de forma programática para usar el evento 'onerror'
    const colDiv = document.createElement('div');
    colDiv.className = 'col-sm-6 col-md-4 col-lg-3 mb-4';

    const cardDiv = document.createElement('div');
    cardDiv.className = 'card h-100 shadow-sm';

    const img = new Image();
    img.className = 'card-img-top';
    img.alt = nombre;
    img.src = url_imagen;
    
    // Aquí está el cambio clave: si la imagen no se carga, usa la de fallback
    img.onerror = () => {
        img.src = IMG_NO_ENCONTRADA_URL;
    };

    const cardBody = document.createElement('div');
    cardBody.className = 'card-body d-flex flex-column';
    cardBody.innerHTML = `
        <h5 class="card-title">${nombre || 'Sin nombre'}</h5>
        <p class="card-text text-muted">Tipo: ${tipo}</p>
        <p class="card-text text-muted">Piedra: ${piedra || 'N/A'}</p>
        <p class="card-text comentario-text">${comentario || ''}</p>
        <a href="#" class="btn btn-primary mt-auto">Agregar</a>
        <a href="#" class="btn btn-primary mt-auto">Comprar</a>
    `;

    cardDiv.appendChild(img);
    cardDiv.appendChild(cardBody);
    colDiv.appendChild(cardDiv);

    contenedor.appendChild(colDiv);
  }
  
  productosMostrados = finDeCarga;
}

// Función que se dispara al hacer scroll
function cargarMasProductos() {
  const { scrollTop, scrollHeight, clientHeight } = document.documentElement;

  // Si el usuario ha llegado al final de la página
  if (scrollTop + clientHeight >= scrollHeight - 100) { // El "100" es un margen
    // Detiene la carga si ya se mostraron todos los productos filtrados
    if (productosMostrados < productosFiltrados.length) {
      agregarProductos(productosFiltrados);
    }
  }
}

// Función para asignar los eventos a los menús desplegables
function asignarEventListeners() {
  const menuTipo = document.getElementById("filtroTipo");
  const menuPiedra = document.getElementById("filtroPiedra");

  // Escuchador de eventos para el menú de Tipo
  menuTipo.addEventListener("click", (evento) => {
    const valorSeleccionado = evento.target.getAttribute("data-value");
    const textoBoton = evento.target.textContent;

    document.getElementById("dropdownTipo").textContent = textoBoton;

    filtrarYGenerar(valorSeleccionado, obtenerFiltroActual("piedra"));
  });

  // Escuchador de eventos para el menú de Piedra
  menuPiedra.addEventListener("click", (evento) => {
    const valorSeleccionado = evento.target.getAttribute("data-value");
    const textoBoton = evento.target.textContent;

    document.getElementById("dropdownPiedra").textContent = textoBoton;

    filtrarYGenerar(obtenerFiltroActual("tipo"), valorSeleccionado);
  });
}

// Función para obtener el filtro que no ha sido modificado
function obtenerFiltroActual(tipoFiltro) {
  if (tipoFiltro === "tipo") {
    return document.getElementById("dropdownTipo").getAttribute("data-value") || "todos";
  } else {
    return document.getElementById("dropdownPiedra").getAttribute("data-value") || "todas";
  }
}

// Función principal de filtrado
function filtrarYGenerar(filtroTipo, filtroPiedra) {
  // Realiza el filtrado inicial sobre todos los productos
  let nuevaListaFiltrada = productos;

  if (filtroTipo && filtroTipo !== "todos") {
    nuevaListaFiltrada = nuevaListaFiltrada.filter(producto =>
      producto.tipo[0].toLowerCase() === filtroTipo.toLowerCase()
    );
  }

  if (filtroPiedra && filtroPiedra !== "todas") {
    nuevaListaFiltrada = nuevaListaFiltrada.filter(producto =>
      producto.piedra[0].toLowerCase() === filtroPiedra.toLowerCase()
    );
  }

  // Actualiza la variable de productos filtrados para que el scroll la use
  productosFiltrados = nuevaListaFiltrada;
  
  // Limpia el catálogo y genera solo la primera tanda de productos
  generarProductos(productosFiltrados);
}