# -*- coding: utf-8 -*-
"""Genera data/proyectos.json y las 13 paginas de proyecto, copiando y
renombrando los assets reales (imagenes, ifc, pdf) desde OBRAS/.
Se corre UNA sola vez para armar el sitio. Despues de esto, Tincho edita
los archivos generados a mano (no hace falta volver a correr este script,
salvo que se regenere todo desde cero)."""
import glob
import html
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_common import PROJECTS, SCOPE_TAGS, PROJECT_TEMPLATE, VIEWER_SECTION_TEMPLATE, VIEWER_SECTION_EMPTY

SRC = os.path.expanduser("~/mnt/Tincho_portfolio/OBRAS")
SITE = os.path.expanduser("~/mnt/Tincho_portfolio/PORTFOLIO-WEB")


def spec_row(label, value):
    if not value:
        return ""
    return f'          <div><span>{html.escape(label)}</span><b>{html.escape(str(value))}</b></div>\n'


def copy_gallery(src_folder, dest_folder):
    """Copia CAPTURAS/*.png (+ Resumen.png suelto si existe) como galeria/01.jpg, 02.jpg..."""
    os.makedirs(dest_folder, exist_ok=True)
    files = sorted(glob.glob(os.path.join(src_folder, "CAPTURAS", "*")))
    extra = os.path.join(src_folder, "Resumen.png")
    if os.path.isfile(extra):
        files.append(extra)
    out_names = []
    for i, f in enumerate(files, start=1):
        ext = os.path.splitext(f)[1].lower() or ".png"
        name = f"{i:02d}{ext}"
        shutil.copyfile(f, os.path.join(dest_folder, name))
        out_names.append(name)
    return out_names


def copy_ifc(src_folder, dest_folder, ifc_name):
    if not ifc_name:
        return None
    src = os.path.join(src_folder, "3D", ifc_name)
    if not os.path.isfile(src):
        print(f"  [!] no encontre el ifc: {src}")
        return None
    dest = os.path.join(dest_folder, "modelo.ifc")
    shutil.copyfile(src, dest)
    return "modelo.ifc"


def copy_pdf(src_folder, dest_folder, pdf_name):
    if not pdf_name:
        return None
    src = os.path.join(src_folder, "3D", pdf_name)
    if not os.path.isfile(src):
        return None
    dest = os.path.join(dest_folder, "ficha-planos.pdf")
    shutil.copyfile(src, dest)
    return "ficha-planos.pdf"


def build_project_html(p, gallery_files, ifc_out, pdf_out):
    hero_specs = ""
    for label, key in [("Peso", "peso"), ("Superficie", "superficie"), ("Alto", "alto")]:
        v = p.get(key)
        if v:
            hero_specs += f'          <span>{html.escape(label)}<b>{html.escape(v)}</b></span>\n'
    if not hero_specs:
        hero_specs = f'          <span>Tipo<b>{html.escape(p["tipo"])}</b></span>\n'

    data_rows = ""
    data_rows += spec_row("Tipo de estructura", p.get("tipo"))
    data_rows += spec_row("Peso", p.get("peso"))
    data_rows += spec_row("Dimensiones", (f'{p["ancho"]} × {p["largo"]}' if p.get("ancho") and p.get("largo") else None))
    data_rows += spec_row("Superficie", p.get("superficie"))
    data_rows += spec_row("Alto de cercha", p.get("alto"))
    data_rows += spec_row("Perfilería", p.get("perfileria"))
    data_rows += spec_row("Normativa", p.get("normativa"))

    scope_tags_html = "".join(f'          <span>{html.escape(t)}</span>\n' for t in SCOPE_TAGS)

    desafio_block = ""
    if p.get("desafio"):
        desafio_block = (
            '        <div class="desafio">\n'
            '          <h3>El desafío</h3>\n'
            f'          <p>{html.escape(p["desafio"])}</p>\n'
            '        </div>\n'
        )

    pdf_block = ""
    if pdf_out:
        pdf_block = f'        <p class="download-link"><a class="button ghost" href="{html.escape(pdf_out)}" target="_blank" rel="noopener">Descargar planos (PDF) ↓</a></p>\n'

    gallery_html = "".join(
        f'      <div><img src="galeria/{fn}" alt="{html.escape(p["titulo"])} — vista {i+1}" loading="lazy"></div>\n'
        for i, fn in enumerate(gallery_files)
    )
    gallery_class = " cols-1" if len(gallery_files) <= 1 else ""
    hero_image = f'galeria/{gallery_files[0]}' if gallery_files else ''

    if ifc_out:
        viewer_section = VIEWER_SECTION_TEMPLATE.substitute(
            ifc_file=ifc_out, hero_image=hero_image, titulo=p["titulo"]
        )
    else:
        viewer_section = VIEWER_SECTION_EMPTY.substitute()

    return PROJECT_TEMPLATE.substitute(
        titulo=p["titulo"], titulo_url=p["titulo"].replace(" ", "%20"),
        resumen=p["resumen"], categoria=p["categoria"],
        hero_image=hero_image, hero_specs=hero_specs,
        viewer_section=viewer_section,
        data_rows=data_rows,
        scope_tags_html=scope_tags_html, desafio_block=desafio_block,
        pdf_block=pdf_block, gallery_html=gallery_html, gallery_class=gallery_class,
    )


PLACEHOLDER_PROJECT = dict(
    titulo="Nombre de la obra", categoria="Categoría (ej: Nave Industrial)",
    resumen="Una frase corta que resuma la obra.",
    tipo="Tipo de estructura", peso="00 tn", ancho="00 m", largo="00 m",
    superficie="000 m²", alto="00 m", perfileria="Perfiles armados y perfiles conformados",
    normativa="CIRSOC 301",
    desafio="Contá acá algún desafío particular de la obra (opcional — si no aplica, borrá este bloque entero).",
)


def build_template_folder():
    dest = os.path.join(SITE, "proyectos", "_plantilla-proyecto")
    os.makedirs(os.path.join(dest, "galeria"), exist_ok=True)
    html_out = build_project_html(PLACEHOLDER_PROJECT, ["01.jpg", "02.jpg"], "modelo.ifc", None)
    # marcar con comentarios TINCHO: los puntos a editar
    html_out = html_out.replace(
        "<title>Nombre de la obra |",
        "<!-- TINCHO: cambiá el título acá y en el <h1> de más abajo --><title>Nombre de la obra |",
    )
    html_out = html_out.replace(
        "<h1>Nombre de la obra</h1>",
        "<h1>Nombre de la obra</h1> <!-- TINCHO: título de la obra -->",
    )
    html_out = html_out.replace(
        '<p class="lead">Una frase corta que resuma la obra.</p>',
        '<p class="lead">Una frase corta que resuma la obra.</p> <!-- TINCHO: bajada corta -->',
    )
    html_out = html_out.replace(
        '<div class="desafio">',
        '<!-- TINCHO: borrá este bloque completo si no aplica --><div class="desafio">',
    )
    with open(os.path.join(dest, "index.html"), "w", encoding="utf-8") as f:
        f.write(html_out)
    with open(os.path.join(dest, "galeria", "PONE_ACA_TUS_FOTOS.txt"), "w", encoding="utf-8") as f:
        f.write("Poné acá las fotos de la obra, nombradas 01.jpg, 02.jpg, 03.jpg...\n"
                "(o .png, manteniendo la numeración). Ver ../../../GUIA.md\n")
    with open(os.path.join(dest, "PONE_ACA_TU_MODELO.txt"), "w", encoding="utf-8") as f:
        f.write("Poné acá el archivo IFC de la obra, renombrado a: modelo.ifc\n"
                "Ver ../../GUIA.md\n")


def main():
    manifest = []
    os.makedirs(os.path.join(SITE, "proyectos"), exist_ok=True)
    os.makedirs(os.path.join(SITE, "data"), exist_ok=True)

    for p in PROJECTS:
        slug = p["slug"]
        src_folder = os.path.join(SRC, p["folder"])
        dest_folder = os.path.join(SITE, "proyectos", slug)
        gallery_folder = os.path.join(dest_folder, "galeria")
        print("→", slug)

        gallery_files = copy_gallery(src_folder, gallery_folder)
        ifc_out = copy_ifc(src_folder, dest_folder, p.get("ifc"))
        pdf_out = copy_pdf(src_folder, dest_folder, p.get("pdf"))

        html_out = build_project_html(p, gallery_files, ifc_out, pdf_out)
        with open(os.path.join(dest_folder, "index.html"), "w", encoding="utf-8") as f:
            f.write(html_out)

        meta = [v for v in [p.get("peso"), p.get("superficie")] if v]
        manifest.append({
            "slug": slug,
            "titulo": p["titulo"],
            "categoria": p["categoria"],
            "resumen": p["resumen"],
            "imagen": f"proyectos/{slug}/galeria/{gallery_files[0]}" if gallery_files else "",
            "meta": meta,
        })

    with open(os.path.join(SITE, "data", "proyectos.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)

    build_template_folder()

    print("\nListo:", len(manifest), "proyectos generados en", SITE)


if __name__ == "__main__":
    main()
