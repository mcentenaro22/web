# Guía para agregar y editar obras

No hace falta saber programar ni instalar nada. Sólo un editor de texto
(sirve el Bloc de notas / TextEdit, pero anda mejor con [VS Code](https://code.visualstudio.com/),
que es gratis). **Nunca toques la carpeta `assets/` ni el `index.html` de la
raíz** — con eso alcanza para no romper nada.

## Agregar una obra nueva

**1. Duplicá la carpeta plantilla.**
Copiá `proyectos/_plantilla-proyecto/` y pegala dentro de `proyectos/` con un
nombre nuevo, todo en minúscula, sin espacios ni tildes ni ñ — por ejemplo
`proyectos/deposito-rosario/`. Ese nombre de carpeta es el "slug" de la obra.

**2. Poné los archivos de la obra adentro de esa carpeta:**
- El archivo `.ifc` → renombralo a `modelo.ifc` (así como está, sin cambiar el nombre).
- Las fotos/renders → adentro de `galeria/`, con estos nombres exactos:
  `01.jpg`, `02.jpg`, `03.jpg`... (podés usar `.png` en vez de `.jpg` si es lo
  que tenés, pero mantené la numeración `01`, `02`, `03`).
- Si tenés un PDF de planos para ofrecer de descarga, ponelo como `ficha-planos.pdf`
  (opcional).

**3. Editá el texto de la obra.**
Abrí el `index.html` que quedó adentro de tu carpeta nueva y buscá los
bloques marcados con `<!-- TINCHO: ... -->` (usá Ctrl+F / Cmd+F y buscá
"TINCHO"). Ahí vas a encontrar, ya armado, dónde cambiar:
- El título de la obra (aparece en 3 lugares: `<title>`, el `<h1>` y el `<meta description>`)
- La bajada / resumen corto
- Los datos técnicos (tipo, peso, dimensiones, superficie, normativa, perfilería)
- El texto de "El desafío" (podés borrar todo ese bloque `<div class="desafio">...</div>` si no aplica)

No hace falta tocar nada del bloque del visor 3D (`<div data-ifc-viewer...>`)
salvo que hayas puesto el `.ifc` con otro nombre.

**4. Agregá la obra al home.**
Abrí `data/proyectos.json` con el editor de texto. Es una lista de bloques
como este — copiá uno entero, pegalo antes del `]` final, separalo con una
coma y cambiá los datos:

```json
{
  "slug": "deposito-rosario",
  "titulo": "Depósito Rosario",
  "categoria": "Nave Industrial",
  "resumen": "Una frase corta que resuma la obra.",
  "imagen": "proyectos/deposito-rosario/galeria/01.jpg",
  "meta": ["40 tn", "1.200 m²"]
}
```

`"slug"` tiene que ser exactamente el nombre de la carpeta que creaste en el
paso 1. `"meta"` son los 1-3 datos cortos que se ven en la tarjeta (podés
dejar sólo uno, o ninguno con `[]`).

**Importante:** `proyectos.json` es un archivo con formato estricto — si te
falta o te sobra una coma, el home deja de cargar los proyectos. Si dudás,
copiá un bloque entero existente y sólo cambiá los valores, sin tocar las
comillas ni las llaves `{ }`.

**5. Subí los cambios a GitHub** (arrastrando los archivos nuevos al repo, o
con `git add` / `git commit` / `git push` si usás la terminal). El sitio se
actualiza solo, 1-2 minutos después de subir.

## Editar una obra que ya existe

Es el mismo paso 3 y 4, pero sobre la carpeta que ya está en `proyectos/` en
vez de duplicar la plantilla.

## Sacar una obra del home (sin borrarla)

Borrá (o comentá) su bloque en `data/proyectos.json`. La carpeta y la página
de la obra van a seguir existiendo, sólo que no va a aparecer en el home.

## Si algo se rompe

- El home no muestra ninguna obra → seguramente hay un error de formato en
  `data/proyectos.json` (una coma de más/menos). Fijate el último bloque que
  editaste.
- El visor 3D no carga → confirmá que el archivo se llama exactamente
  `modelo.ifc` y está en la misma carpeta que el `index.html` de la obra.
  El visor sólo funciona si el sitio se ve por internet (GitHub Pages) o con
  un servidor local — **no** abriendo el `index.html` con doble clic desde
  el explorador de archivos.
