# Guías de Inglés · Instituto Marítimo de Valparaíso

Sitio estático (GitHub Pages) con guías de inglés en PDF para 1° y 2° Medio.

## Contenido
- **49 guías por tema** (`*-guia.pdf`, 3–4 páginas, 9–10 ejercicios): versión del estudiante, `*-pauta.pdf` (pauta docente) y `*-completa.pdf` (guía con respuestas en rojo).
- **21 guías de reemplazo** (`reemplazo/*-guia.pdf` y `reemplazo/*-pauta.pdf`): 2 hojas para 45 minutos con sopa de letras, unscramble, odd one out, crucigrama, sentence scramble, código secreto y bonus.

## Cómo editar y regenerar
- Guías por tema: el contenido está en `generador/temas_*.py`. Regenerar con:
  `python3 generador/generar.py` (o `python3 generador/generar.py present-simple` para un solo tema).
- Guías de reemplazo: el contenido está en `reemplazo/guias.js` y la plantilla en `reemplazo/guia.html`. Regenerar los PDF con:
  `node generador/generar_reemplazo.js` (requiere Playwright).
- Proyecto tríptico de predicciones (2° Medio, will): guía y plantilla en `proyectos/triptico.html`, presentación en `proyectos/triptico-slides.html`. Regenerar con `node generador/generar_triptico.js` (crea guía, pauta, plantilla y presentación en PDF).
