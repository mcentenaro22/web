# Portfolio — Martín Centenaro

Sitio estático (sin build, sin npm) listo para GitHub Pages: `index.html` es la
home y no hace falta tocarlo para agregar obras nuevas — ver **GUIA.md** para
el mantenimiento del día a día.

## Subir a GitHub Pages

Esta carpeta ya es un repositorio git local (con un commit inicial hecho).
Para subirla:

1. Creá un repositorio vacío en GitHub (público, o privado con GitHub Pro/Team — Pages gratis requiere público). **No** le tildes "Add a README" para que quede vacío.
2. Desde una terminal, parado en esta carpeta:
   ```bash
   git remote add origin https://github.com/<usuario>/<repo>.git
   git branch -M main
   git push -u origin main
   ```
   (o subí los archivos arrastrándolos desde la web de GitHub, si preferís no usar la terminal).
3. En el repo: **Settings → Pages → Build and deployment → Source: Deploy from a branch**, rama `main`, carpeta `/ (root)`. Guardar.
4. Esperá 1-2 minutos y el sitio va a estar en `https://<usuario>.github.io/<repo>/`.

Ya incluye un archivo `.nojekyll` (necesario porque hay carpetas que arrancan
con `_`, como `_plantilla-proyecto`, y sin ese archivo GitHub Pages las ignora).

## Formulario de contacto

El formulario usa [FormSubmit](https://formsubmit.co/) (gratis, sin backend
propio) apuntando a `mcentenaro2@gmail.com`. **El primer envío real** que
llegue va a pedir una confirmación por email única vez (FormSubmit manda un
mail de activación) — hay que abrirlo y confirmar para que los siguientes
mensajes lleguen directo a la bandeja de entrada.

## LinkedIn

LinkedIn no permite embeber el feed de un perfil personal en otro sitio (sólo
lo permite para páginas de empresa). Lo que se embebió es la credencial
oficial de perfil ("Profile Badge"), más un link directo al perfil. Si en
algún momento LinkedIn habilita algo más, se puede ajustar en
`index.html`, sección `#contacto`.

## Estructura

```
index.html              ← home (no tocar para agregar obras)
data/proyectos.json     ← qué tarjetas aparecen en el home — SÍ se edita
assets/                 ← CSS, JS y librerías del visor 3D (no tocar)
proyectos/<obra>/       ← una carpeta por obra, con su index.html, galería e IFC
proyectos/_plantilla-proyecto/  ← copiar esta carpeta para agregar una obra nueva
```

Ver **GUIA.md** para el paso a paso de agregar/editar una obra.
