# -*- coding: utf-8 -*-
"""Datos de las 13 obras + template de pagina de proyecto.
Este modulo es compartido por el generador que corre en el Mac del usuario."""
from string import Template

PROJECTS = [
    dict(folder="1141-ASTENGO", slug="nave-deportiva-astengo", ifc="1141-Nave.ifc",
         titulo="Nave deportiva Astengo", categoria="Nave Deportiva",
         resumen="Nave deportiva con pórticos de encuentros oblicuos, modelada íntegramente en BIM.",
         tipo="Nave Deportiva", peso="51 tn", ancho="33 m", largo="40 m", superficie="1.320 m²",
         alto="11,2 m", perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio="La geometría de la nave presenta pórticos con encuentros oblicuos.",
         pdf="1141-Nave.pdf"),
    dict(folder="473-FRAME", slug="frame", ifc="473-EDIFICIO.ifc",
         titulo="Frame", categoria="Edificio",
         resumen="Edificio en espacio reducido resuelto con paños modulares de tubo estructural.",
         tipo="Edificio", peso="42 tn", ancho="8,4 m", largo="8,8 m", superficie="73,9 m²",
         alto="18,2 m", perfileria="Tubo estructural", normativa="CIRSOC 301",
         desafio="Al estar en espacios reducidos y con perfilería de tubos rectangulares, se optó por generar paños modulares laterales y de piso. El montaje se resolvió soldando los paños de piso en obra y las vigas laterales nivel a nivel, dejando previstos los conectores para el hormigonado posterior.",
         pdf=None),
    dict(folder="666-KRESS", slug="kress", ifc="KRESS.ifc",
         titulo="Kress", categoria="Nave Industrial",
         resumen="Nave industrial de gran escala, con más de 3.900 m² de superficie cubierta.",
         tipo="Nave Industrial", peso="85 tn", ancho="71 m", largo="56 m", superficie="3.976 m²",
         alto="12,8 m", perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio=None, pdf=None),
    dict(folder="690-HARTMANN", slug="hartmann", ifc="HARTMANN.ifc",
         titulo="Hartmann", categoria="Nave Industrial",
         resumen="Nave emplazada entre muros existentes, con relevamiento y nube de puntos incorporados al modelo.",
         tipo="Nave Industrial", peso="11,5 tn", ancho="19 m", largo="38 m", superficie="722 m²",
         alto="7,6 m", perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio="La obra está emplazada entre muros existentes, lo que llevó a un relevamiento en obra y la incorporación de la nube de puntos al modelo. Los frontis llevan una cenefa reticulada armada con perfiles conformados.",
         pdf=None),
    dict(folder="694-BMX", slug="lanzadores-bmx", ifc="BMX.ifc",
         titulo="Lanzadores BMX", categoria="Torres y Rampas",
         resumen="Torres de largada para BMX conectadas por escaleras y entrepisos de rejilla.",
         tipo="Torres y rampas", peso="40 tn", ancho="8 m", largo="25 m", superficie="200 m²",
         alto="12 m", perfileria="Perfiles armados", normativa="CIRSOC 301",
         desafio="La obra de torres para largada de BMX se dividió en 3 partes: dos torres para dos lanzadores de 6 y 9 metros de altura, conectadas entre sí por un sistema de escaleras y entrepisos de rejilla. Las rampas se terminaron de consolidar con losetas prefabricadas.",
         pdf=None),
    dict(folder="696-NODO", slug="nodo", ifc="696-NODO.ifc",
         titulo="Nodo", categoria="Nave Industrial c/ Divisiones",
         resumen="Complejo de depósitos de 14.400 m², desarrollado y montado en 6 fases.",
         tipo="Nave industrial c/ divisiones", peso="270 + 410 tn", ancho="60 m", largo="240 m", superficie="14.400 m²",
         alto="11,3 m", perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio="Por el tamaño de la obra se optó por dividirla en 6 fases, lo que implicó dividir en 6 etapas la fabricación y el montaje. Dado que el fin de la obra era el alquiler de depósitos, se implementó un módulo divisorio tipo para poder generar espacios de distintas dimensiones.",
         pdf=None),
    dict(folder="699-AGD BANDERA", slug="agd-bandera", ifc="699-AGD BANDERA.ifc",
         titulo="AGD Bandera", categoria="Estación de Carga de Trenes",
         resumen="Torre soporte de silo, andén techado y pasarela de acceso para carga de vagones.",
         tipo="Estación de carga de trenes", peso="25 tn", ancho="6,4 m", largo="45 m", superficie="288 m²",
         alto="9 m", perfileria="Perfiles laminados tipo W", normativa="CIRSOC 301",
         desafio="Se planteó una torre soporte de silo para carga de vagones junto con un andén techado y una pasarela de acceso a los vagones, con escalera hacia el silo para tareas de mantenimiento.",
         pdf=None),
    dict(folder="702-MERCADO LIBRE", slug="meli-gualeguaychu", ifc="MELI.ifc",
         titulo="MELI Gualeguaychú", categoria="Nave Industrial / Depósito",
         resumen="Depósito industrial de 4.392 m² para Mercado Libre en Gualeguaychú.",
         tipo="Nave industrial / depósito", peso="72 tn", ancho="72 m", largo="61 m", superficie="4.392 m²",
         alto="9,6 m", perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio=None, pdf=None),
    dict(folder="10347-Nave 22x37", slug="nave-22x37", ifc="10347-Nave.ifc",
         titulo="Nave industrial chica 22×37", categoria="Nave Industrial",
         resumen="Nave industrial compacta de 814 m², resuelta con perfiles armados y conformados.",
         tipo="Nave industrial", peso="17 tn", ancho="22 m", largo="37 m", superficie="814 m²",
         alto="9 m", perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio=None, pdf=None),
    dict(folder="10386-Gobierno", slug="edificio-gobierno", ifc="10386-Gobierno.ifc",
         titulo="Edificio de gobierno", categoria="Edificio",
         resumen="Cubierta reticulada de dos tipos de cerchas sobre un edificio de hormigón premoldeado.",
         tipo="Edificio", peso="15 tn", ancho="15 m", largo="92,5 m", superficie="1.387,5 m²",
         alto=None, perfileria="Perfiles conformados", normativa="CIRSOC 301",
         desafio="La obra consiste en la cubierta de un edificio ejecutado con hormigón premoldeado. La cubierta está compuesta por cerchas reticuladas de 15 metros de luz, de dos tipos, para dar entrada de luz al edificio: cerchas a un agua con cordones y montantes de perfiles conformados de 600 kg, y cerchas a un agua de 800 kg.",
         pdf=None),
    dict(folder="10444-UP N13", slug="unidad-penitenciaria-up13", ifc="10444-UP13.ifc",
         titulo="Unidad Penitenciaria N.º 13", categoria="Cubierta",
         resumen="Cuatro cubiertas para edificios penitenciarios en perfiles laminados tipo W.",
         tipo="Cubierta (4 unidades)", peso="7 tn", ancho="12,2 m", largo="37 m", superficie="451,4 m²",
         alto=None, perfileria="Perfiles laminados y perfiles conformados", normativa="CIRSOC 301",
         desafio="Cuatro cubiertas para edificios penitenciarios, materializadas en perfiles laminados tipo W con correas en perfiles conformados. En los cerramientos se utilizaron paneles aislantes y chapas traslúcidas para mejorar la iluminación.",
         pdf=None),
    dict(folder="10517-BCR COCHERAS", slug="bcr-cocheras", ifc="10517-Cocheras.ifc",
         titulo="BCR Cocheras", categoria="Cocheras",
         resumen="Estructura de cocheras resuelta en perfiles armados y conformados.",
         tipo="Cocheras", peso="5 tn", ancho=None, largo=None, superficie=None,
         alto=None, perfileria="Perfiles armados y perfiles conformados", normativa="CIRSOC 301",
         desafio=None, pdf=None),
    dict(folder="10605-Torre Ciclones", slug="torre-ciclones", ifc=None,
         titulo="Torre Ciclones", categoria="Torre",
         resumen="Torre de soporte de maquinaria (ciclones), vinculada con modelos de referencia de obras linderas.",
         tipo="Torre", peso="19 tn", ancho="14 m", largo="10,5 m", superficie="147 m²",
         alto="10 m", perfileria="Perfiles laminados", normativa="CIRSOC 301",
         desafio="La torre de soporte de ciclones está conectada con otros edificios del predio, por lo que se trabajó con modelos de referencia para lograr la precisión necesaria en la implantación. Como el destino es el soporte de maquinaria, se incorporó al modelo la maqueta de los equipos para garantizar el calce.",
         pdf=None),
]

SCOPE_TAGS = ["Modelado 3D BIM", "Planos de taller", "Planos de montaje", "Archivos NC/DSTV", "Lista de materiales"]

VIEWER_SECTION_TEMPLATE = Template(r"""  <!-- ===== visor IFC — sólo se carga si el visitante lo abre ===== -->
  <section class="viewer-section">
    <div class="wrap">
      <div class="viewer-topbar">
        <div><span class="status-dot"></span> MODELO IFC INTERACTIVO</div>
        <span>Click para abrir · Arrastrar para orbitar · Rueda para zoom</span>
      </div>
      <div class="viewer-frame" data-ifc-viewer data-model="$ifc_file">
        <img class="viewer-cover" src="$hero_image" alt="Vista previa de $titulo">
        <div class="viewer-scrim">
          <button class="viewer-launch" type="button" data-viewer-launch>▶ Ver modelo 3D interactivo</button>
        </div>
        <div class="viewer-controls" data-viewer-controls hidden>
          <button type="button" data-viewer-reset title="Reencuadrar">⟳</button>
        </div>
        <div class="viewer-status" data-viewer-status hidden></div>
      </div>
      <p class="viewer-note">El modelo se procesa en tu navegador a partir del archivo <code>$ifc_file</code> — no requiere instalar software BIM.</p>
    </div>
  </section>
""")

VIEWER_SECTION_EMPTY = Template(r"""  <section class="viewer-section">
    <div class="wrap">
      <p class="viewer-note">El modelo IFC de esta obra todavía no está cargado. <!-- TINCHO: cuando tengas el .ifc, copialo a esta carpeta y agregá la sección del visor (ver _plantilla-proyecto/index.html). --></p>
    </div>
  </section>
""")

PROJECT_TEMPLATE = Template(r"""<!doctype html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>$titulo | Martín Centenaro — Ingeniería civil</title>
<meta name="description" content="$resumen" />
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="../../assets/css/style.css" />
<script type="importmap">
{
  "imports": {
    "three": "../../assets/vendor/three.module.min.js",
    "three/examples/jsm/utils/BufferGeometryUtils": "../../assets/vendor/BufferGeometryUtils.min.js",
    "web-ifc": "../../assets/vendor/web-ifc-api.min.js"
  }
}
</script>
</head>
<body class="project-page">

<header class="site-header overlay">
  <a class="brand" href="../../#top">MARTÍN CENTENARO<span>·ING.CIVIL</span></a>
  <nav class="site-nav" data-nav>
    <a href="../../index.html#proyectos">Obras</a>
    <a href="../../index.html#sobre-mi">Sobre mí</a>
    <a href="../../index.html#contacto">Contacto</a>
  </nav>
  <button class="nav-toggle" data-nav-toggle aria-label="Abrir menú"><span></span><span></span><span></span></button>
</header>

<main>
  <section class="project-hero" style="background-image:url('$hero_image')">
    <div class="wrap">
      <p class="eyebrow">$categoria</p>
      <h1>$titulo</h1>
      <p class="lead">$resumen</p>
      <div class="hero-specs">
$hero_specs      </div>
    </div>
  </section>

$viewer_section
  <section class="project-content wrap">
    <div class="project-description">
      <p class="eyebrow">El proyecto</p>
      <h2>Del modelo a la documentación de obra.</h2>
      <p>$resumen</p>
      <p>El modelo BIM se utilizó como base para desarrollar la documentación de fabricación y montaje de la estructura.</p>
$desafio_block    </div>
    <div>
      <div class="data-list">
$data_rows      </div>
      <div class="scope-tags">
$scope_tags_html      </div>
$pdf_block    </div>
  </section>

  <section class="wrap">
    <div class="gallery$gallery_class">
$gallery_html    </div>
    <div class="back-link"><a href="../../index.html#proyectos">← Volver a obras</a></div>
  </section>
</main>

<a class="wa-float" href="https://wa.me/5493471597118?text=Hola%20Mart%C3%ADn%2C%20vi%20el%20proyecto%20$titulo_url%20en%20tu%20portfolio." target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">
  <svg viewBox="0 0 24 24"><path d="M12 2a10 10 0 00-8.6 15L2 22l5.2-1.4A10 10 0 1012 2zm0 18.1a8 8 0 01-4.3-1.2l-.3-.2-3.1.8.8-3-.2-.3A8.1 8.1 0 1112 20.1zm4.5-6c-.2-.1-1.4-.7-1.7-.8-.2-.1-.4-.1-.6.1-.2.2-.6.8-.8 1-.1.1-.3.2-.5.1-.2-.1-1-.4-2-1.2-.7-.6-1.2-1.4-1.4-1.6-.1-.2 0-.4.1-.5l.4-.5c.1-.1.2-.3.2-.4.1-.2 0-.3 0-.4-.1-.1-.6-1.4-.8-1.9-.2-.5-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3-.2.2-.8.8-.8 1.9s.8 2.2.9 2.4c.1.2 1.6 2.4 3.8 3.4.5.2 1 .4 1.3.5.5.2 1 .1 1.4.1.4-.1 1.4-.6 1.6-1.1.2-.5.2-1 .1-1.1-.1-.1-.2-.2-.4-.3z"/></svg>
</a>

<footer class="site-footer">
  <span>© <span id="year"></span> Martín Centenaro — Ingeniería civil</span>
  <span>Sitio construido para GitHub Pages</span>
</footer>

<script src="../../assets/js/common.js"></script>
<script type="module" src="../../assets/js/ifc-viewer.js"></script>
<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
</body>
</html>
""")
