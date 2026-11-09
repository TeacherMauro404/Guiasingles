"""
Motor de generación de guías de inglés (PDF) — Instituto Marítimo de Valparaíso.

Cada tema se describe como un diccionario (ver carpeta temas/). Por cada tema se generan:
  <slug>-guia.pdf      guía del estudiante (sin respuestas)
  <slug>-pauta.pdf     pauta de corrección (uso docente)
  <slug>-completa.pdf  guía con las respuestas incrustadas (autocorrección)

Mini-lenguaje para los ítems:
  [respuesta]        espacio en blanco; en la pauta aparece la respuesta.
  {a|b*|c}           selección múltiple; la opción con * es la correcta.
  "texto => resp"    (tipo rewrite / questions) enunciado y respuesta modelo.
"""
import re
import random
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer, Table,
                                TableStyle, KeepTogether, CondPageBreak)

NAVY = colors.HexColor("#0E2A47")
BLUE = colors.HexColor("#1F5C8B")
BAR = colors.HexColor("#1E5A8A")
GOLD = colors.HexColor("#C8912B")
GOLD_SOFT = colors.HexColor("#FBF4E4")
BLUE_SOFT = colors.HexColor("#EEF4FA")
GREEN = colors.HexColor("#1B7A3D")
INK = colors.HexColor("#152230")
MUTED = colors.HexColor("#5A6B7A")
LINE = colors.HexColor("#B8C7D6")
ANS = "#C0392B"   # color de respuestas en la versión completa

W, H = LETTER
MARGIN = 16 * mm
CW = W - 2 * MARGIN

ST = {
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=20, leading=24, textColor=NAVY, spaceAfter=2),
    "obj": ParagraphStyle("obj", fontName="Helvetica-Bold", fontSize=9, leading=11.5, textColor=GREEN),
    "goal": ParagraphStyle("goal", fontName="Helvetica-Oblique", fontSize=9, leading=11.5, textColor=BLUE),
    "rem_h": ParagraphStyle("remh", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=NAVY),
    "rem": ParagraphStyle("rem", fontName="Helvetica", fontSize=8.6, leading=12.4, textColor=INK),
    "bar": ParagraphStyle("bar", fontName="Helvetica-Bold", fontSize=9.3, leading=12, textColor=colors.white),
    "instr": ParagraphStyle("instr", fontName="Helvetica-Oblique", fontSize=8.4, leading=11, textColor=MUTED),
    "item": ParagraphStyle("item", fontName="Helvetica", fontSize=9.4, leading=13, textColor=INK),
    "num": ParagraphStyle("num", fontName="Helvetica-Bold", fontSize=9.4, leading=13, textColor=NAVY, alignment=2),
    "text": ParagraphStyle("text", fontName="Helvetica", fontSize=9.4, leading=15.5, textColor=INK),
    "bank": ParagraphStyle("bank", fontName="Helvetica-Bold", fontSize=9.2, leading=13, textColor=NAVY, alignment=TA_CENTER),
    "small": ParagraphStyle("small", fontName="Helvetica", fontSize=8.6, leading=11.5, textColor=INK),
    "ph": ParagraphStyle("ph", fontName="Helvetica-Bold", fontSize=9.4, leading=12.5, textColor=NAVY),
    "pans": ParagraphStyle("pans", fontName="Helvetica", fontSize=9, leading=12.6, textColor=INK),
    "score": ParagraphStyle("score", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=NAVY, alignment=TA_CENTER),
}

ARROW = '<font name="Symbol">→</font>'
BLANK = "________"


def esc(s):
    return s.replace("&", "&amp;").replace("<b>", "\x01").replace("</b>", "\x02") \
            .replace("<i>", "\x03").replace("</i>", "\x04").replace("<", "&lt;").replace(">", "&gt;") \
            .replace("\x01", "<b>").replace("\x02", "</b>").replace("\x03", "<i>").replace("\x04", "</i>")


def arrows(s):
    return s.replace("→", ARROW)


RX_BLANK = re.compile(r"\[([^\]]*)\]")
RX_CHOICE = re.compile(r"\{([^}]*)\}")


def answers_of(s):
    """Respuestas de un ítem en orden de aparición."""
    out = []
    for m in re.finditer(r"\[([^\]]*)\]|\{([^}]*)\}", s):
        if m.group(1) is not None:
            out.append(m.group(1))
        else:
            opts = m.group(2).split("|")
            out.append(next(o[:-1] for o in opts if o.endswith("*")))
    return out


def render(s, mode, numbered=None, long_blank=False):
    """Convierte el mini-lenguaje a markup ReportLab.
    mode: 'guia' (blancos) | 'completa' (respuestas en rojo)."""
    s = esc(s)
    counter = [0]

    def rb(m):
        counter[0] += 1
        pre = f"<b>({numbered[0] + counter[0]})</b>" if numbered else ""
        if mode == "completa":
            return f'{pre}<font color="{ANS}"><b><u>{m.group(1)}</u></b></font>'
        return pre + (BLANK + "____" if long_blank else BLANK)

    def rc(m):
        opts = m.group(1).split("|")
        if mode == "completa":
            parts = [f'<font color="{ANS}"><b><u>{o[:-1]}</u></b></font>' if o.endswith("*") else o for o in opts]
        else:
            parts = [o.rstrip("*") for o in opts]
        return "(" + " / ".join(parts) + ")"

    s = RX_BLANK.sub(rb, s)
    s = RX_CHOICE.sub(rc, s)
    if numbered:
        numbered[0] += counter[0]
    return arrows(s)


def ans_markup(t):
    return f'<font color="{ANS}"><b>{esc(t)}</b></font>'


# ---------------------------------------------------------------- bloques visuales

def header_footer(topic, kind):
    label = {"guia": "GUÍA DE PRÁCTICA", "pauta": "PAUTA DE CORRECCIÓN", "completa": "GUÍA + PAUTA"}[kind]

    def draw(c, doc):
        c.saveState()
        c.setFillColor(NAVY)
        c.rect(MARGIN, H - 14 * mm - 12 * mm, CW, 12 * mm, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("Helvetica-Bold", 10.5)
        c.drawString(MARGIN + 4 * mm, H - 19.5 * mm, "INSTITUTO MARÍTIMO DE VALPARAÍSO")
        c.setFont("Helvetica", 7.4)
        c.drawString(MARGIN + 4 * mm, H - 23.6 * mm, "Departamento de Inglés  ·  English Department")
        c.setFillColor(colors.HexColor("#E9C579"))
        c.setFont("Helvetica-Bold", 9)
        c.drawRightString(W - MARGIN - 4 * mm, H - 19.5 * mm, label)
        c.setFillColor(colors.white)
        c.setFont("Helvetica", 7.4)
        c.drawRightString(W - MARGIN - 4 * mm, H - 23.6 * mm, f"{topic['nivel']} Medio  ·  Nivel {topic['cefr']}")
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 7)
        c.drawString(MARGIN, 10 * mm, f"Instituto Marítimo de Valparaíso · Departamento de Inglés · {topic['titulo']}")
        c.drawRightString(W - MARGIN, 10 * mm, f"Página {doc.page}")
        c.restoreState()
    return draw


def make_doc(path, topic, kind):
    doc = BaseDocTemplate(path, pagesize=LETTER, leftMargin=MARGIN, rightMargin=MARGIN,
                          topMargin=30 * mm, bottomMargin=16 * mm,
                          title=f"{topic['titulo']} — {kind}", author="Instituto Marítimo de Valparaíso")
    fr = Frame(MARGIN, 16 * mm, CW, H - 46 * mm, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
    doc.addPageTemplates([PageTemplate(id="p", frames=[fr], onPage=header_footer(topic, kind))])
    return doc


def name_box(total):
    t = Table([[Paragraph("<b>NOMBRE:</b> ______________________________________________", ST["small"]),
                Paragraph("<b>CURSO:</b> __________  <b>FECHA:</b> ___________", ST["small"])],
               [Paragraph(f"<b>PUNTAJE:</b> ______ / {total}      <b>NOTA:</b> ______", ST["small"]),
                Paragraph("<b>Tiempo sugerido:</b> 2 clases de 45 min", ST["small"])]],
              colWidths=[CW * 0.58, CW * 0.42], rowHeights=[8 * mm, 7 * mm])
    t.setStyle(TableStyle([("BOX", (0, 0), (-1, -1), 0.8, NAVY), ("LINEBEFORE", (1, 0), (1, -1), 0.5, LINE),
                           ("LINEABOVE", (0, 1), (-1, 1), 0.5, LINE), ("BACKGROUND", (0, 1), (-1, 1), BLUE_SOFT),
                           ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("LEFTPADDING", (0, 0), (-1, -1), 6)]))
    return t


def boxed(flowables, bg, border, pad=7):
    t = Table([[flowables]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), bg), ("BOX", (0, 0), (-1, -1), 0.7, border),
                           ("LEFTPADDING", (0, 0), (-1, -1), pad + 2), ("RIGHTPADDING", (0, 0), (-1, -1), pad + 2),
                           ("TOPPADDING", (0, 0), (-1, -1), pad), ("BOTTOMPADDING", (0, 0), (-1, -1), pad)]))
    return t


def bar(n, title, pts):
    ptxt = f'  <font name="Helvetica" color="#BFD4E8">({pts} pts)</font>' if pts else \
           '  <font name="Helvetica" color="#BFD4E8">(producción)</font>'
    t = Table([[Paragraph(f"EJERCICIO {n} · {esc(title)}{ptxt}", ST["bar"])]], colWidths=[CW])
    t.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), BAR), ("LEFTPADDING", (0, 0), (-1, -1), 6),
                           ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5)]))
    return t


def numbered_table(cells, cols, row_h=None):
    """cells: lista de markup; se distribuye en columnas (orden por columna)."""
    n = len(cells)
    rows = (n + cols - 1) // cols
    data = []
    for r in range(rows):
        row = []
        for c in range(cols):
            i = c * rows + r
            if i < n:
                row += [Paragraph(f"{i + 1}.", ST["num"]), Paragraph(cells[i], ST["item"])]
            else:
                row += ["", ""]
        data.append(row)
    nw = 7 * mm
    cw = (CW - cols * nw) / cols
    t = Table(data, colWidths=[nw, cw] * cols, rowHeights=row_h)
    t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 2),
                           ("RIGHTPADDING", (0, 0), (-1, -1), 4), ("TOPPADDING", (0, 0), (-1, -1), 2.6),
                           ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6)]))
    return t


def write_line(width="full"):
    return "_" * (92 if width == "full" else 40)


# ---------------------------------------------------------------- ejercicios

def shuffled(seq, seed):
    r = random.Random(seed)
    s = list(seq)
    for _ in range(20):
        r.shuffle(s)
        if s != list(seq) or len(s) < 2:
            break
    return s


def scramble_words(sentence, seed):
    """Desordena las palabras (se mantienen mayúsculas como pista)."""
    end = sentence[-1] if sentence[-1] in ".?!" else ""
    words = sentence.rstrip(".?!").split()
    return " / ".join(shuffled(words, seed)), end


def build_exercise(ex, n, mode, slug):
    """Devuelve (flowables, puntos, respuestas_para_pauta)."""
    tp = ex["tipo"]
    fl = []
    pts = 0
    key = []      # lista de strings
    instr = ex.get("instr", "")
    seed = f"{slug}-{n}"

    if tp in ("fill", "choice"):
        items = ex["items"]
        cells = [render(it, mode, long_blank=ex.get("largo", False)) for it in items]
        for it in items:
            a = answers_of(it)
            key.append(" / ".join(a))
            pts += len(a)
        if ex.get("banco"):
            fl.append(boxed(Paragraph("   ·   ".join(ex["banco"]), ST["bank"]), GOLD_SOFT, GOLD, 4))
            fl.append(Spacer(1, 4))
        fl.append(numbered_table(cells, ex.get("cols", 2)))
        pts = ex.get("pts", pts)

    elif tp == "text":
        cnt = [0]
        paras = []
        if ex.get("banco"):
            fl.append(boxed(Paragraph("   ·   ".join(ex["banco"]), ST["bank"]), GOLD_SOFT, GOLD, 4))
            fl.append(Spacer(1, 4))
        txt = ex["texto"]
        for p in txt.split("\n"):
            paras.append(Paragraph(render(p, mode, numbered=cnt), ST["text"]))
        key = answers_of(txt)
        pts = len(key)
        fl.append(boxed(paras, BLUE_SOFT, LINE, 6))

    elif tp == "rewrite":
        cols = ex.get("cols", 1)
        cells = []
        for it in ex["items"]:
            q, a = [x.strip() for x in it.split("=>")]
            key.append(a)
            if mode == "completa":
                cells.append(f"{arrows(esc(q))} {ARROW} {ans_markup(a)}")
            else:
                cells.append(f"{arrows(esc(q))}<br/>{ARROW} {'_' * (34 if cols == 2 else 78)}")
        pts = len(key)
        fl.append(numbered_table(cells, cols))

    elif tp == "order":
        cells = []
        for i, s in enumerate(ex["items"]):
            sc, end = scramble_words(s, f"{seed}-{i}")
            key.append(s)
            if mode == "completa":
                cells.append(f"<i>{esc(sc)}</i> {esc(end)}<br/>{ARROW} {ans_markup(s)}")
            else:
                cells.append(f"<i>{esc(sc)}</i> {esc(end)}<br/>{ARROW} {'_' * 70}")
        pts = len(key)
        fl.append(numbered_table(cells, 1))

    elif tp == "match":
        pairs = ex["pares"]
        rights = shuffled([p[1] for p in pairs], seed)
        letters = "abcdefghijklmnop"
        data = []
        for i, (l, r) in enumerate(pairs):
            correct = letters[rights.index(r)]
            key.append(correct)
            box = f'<font color="{ANS}"><b>{correct}</b></font>' if mode == "completa" else "____"
            data.append([Paragraph(f"{i + 1}.", ST["num"]), Paragraph(esc(l), ST["item"]),
                         Paragraph(box, ST["item"]), Paragraph(f"<b>{letters[i]})</b>", ST["num"]),
                         Paragraph(esc(rights[i]), ST["item"])])
        t = Table(data, colWidths=[7 * mm, CW * 0.36, 12 * mm, 8 * mm, CW - 27 * mm - CW * 0.36])
        t.setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("TOPPADDING", (0, 0), (-1, -1), 2.6),
                               ("BOTTOMPADDING", (0, 0), (-1, -1), 2.6), ("LEFTPADDING", (0, 0), (-1, -1), 2)]))
        fl.append(t)
        pts = len(key)
        key = [f"{i + 1}-{k}" for i, k in enumerate(key)]

    elif tp == "classify":
        cats = ex["categorias"]          # {cat: [palabras]}
        words = shuffled([w for ws in cats.values() for w in ws], seed)
        fl.append(boxed(Paragraph("   ·   ".join(words), ST["bank"]), GOLD_SOFT, GOLD, 4))
        fl.append(Spacer(1, 4))
        hdr = [Paragraph(f"<b>{esc(c)}</b>", ST["bank"]) for c in cats]
        maxn = max(len(v) for v in cats.values())
        rows = [hdr]
        for r in range(maxn):
            row = []
            for c, ws in cats.items():
                if mode == "completa" and r < len(ws):
                    row.append(Paragraph(ans_markup(ws[r]), ST["item"]))
                else:
                    row.append("")
            rows.append(row)
        t = Table(rows, colWidths=[CW / len(cats)] * len(cats), rowHeights=[16] + [17] * maxn)
        t.setStyle(TableStyle([("GRID", (0, 0), (-1, -1), 0.5, LINE), ("BACKGROUND", (0, 0), (-1, 0), BLUE_SOFT),
                               ("VALIGN", (0, 0), (-1, -1), "MIDDLE")]))
        fl.append(t)
        for c, ws in cats.items():
            key.append(f"<b>{esc(c)}:</b> " + ", ".join(esc(w) for w in ws))
        pts = sum(len(v) for v in cats.values())
        key = [("raw", k) for k in key]

    elif tp == "reading":
        paras = [Paragraph(arrows(esc(p)), ST["text"]) for p in ex["texto"].split("\n")]
        if ex.get("titulo_texto"):
            paras.insert(0, Paragraph(f"<b>{esc(ex['titulo_texto'])}</b>", ST["rem_h"]))
        fl.append(boxed(paras, BLUE_SOFT, LINE, 7))
        fl.append(Spacer(1, 5))
        tf = ex.get("vf", [])
        if tf:
            hA = Paragraph("<b>A.</b> Write <b>T</b> (true) or <b>F</b> (false).", ST["small"])
            cells = []
            for s, v in tf:
                mark = ans_markup("T" if v else "F") if mode == "completa" else "____"
                cells.append(f"{esc(s)}  {mark}")
                key.append("T" if v else "F")
            fl.append(KeepTogether([hA, numbered_table(cells, 1)]))
        qs = ex.get("preguntas", [])
        if qs:
            fl.append(Spacer(1, 3))
            hB = Paragraph("<b>B.</b> Answer the questions in English.", ST["small"])
            cells = []
            for q in qs:
                qq, a = [x.strip() for x in q.split("=>")]
                cells.append(f"{esc(qq)}<br/>{ARROW} " + (ans_markup(a) if mode == "completa" else "_" * 74))
            fl.append(KeepTogether([hB, numbered_table(cells, 1)]))
            qkey = [q.split("=>")[1].strip() for q in qs]
        else:
            qkey = []
        pts = len(tf) + len(qs)
        key = ([("sub", "A. " + " · ".join(f"{i + 1}. {k}" for i, k in enumerate(key)))] if tf else []) + \
              ([("sub", "B. " + " · ".join(f"{i + 1}. {esc(k)}" for i, k in enumerate(qkey)))] if qs else [])

    elif tp == "write":
        cells = []
        for p in ex["items"]:
            line = "_" * max(10, 86 - len(p))
            cells.append(f"{esc(p)} {line}<br/>{'_' * 92}")
        fl.append(numbered_table(cells, 1))
        if ex.get("modelo"):
            fl.insert(0, Paragraph(f"<i>Ejemplo: {esc(ex['modelo'])}</i>", ST["instr"]))
        pts = 0
        key = [("raw", "Respuesta personal. Revisar uso correcto de la estructura trabajada.")]

    else:
        raise ValueError(tp)

    head = [bar(n, ex["titulo"], pts)]
    if instr:
        head.append(Spacer(1, 2))
        head.append(Paragraph(esc(instr), ST["instr"]))
    head.append(Spacer(1, 3))
    return head, fl, pts, key


def remember_box(topic):
    inner = [Paragraph("PARA RECORDAR — Remember", ST["rem_h"]), Spacer(1, 3)]
    for line in topic["recordar"]:
        inner.append(Paragraph(arrows(line), ST["rem"]))
    return boxed(inner, GOLD_SOFT, GOLD)


def build_topic(topic, outdir):
    slug = topic["slug"]
    results = {}
    pre_total = 0
    for i, ex in enumerate(topic["ejercicios"], 1):
        pre_total += build_exercise(ex, i, "guia", slug)[2]
    for mode in ("guia", "completa"):
        story = [name_box(pre_total), Spacer(1, 7), Paragraph(esc(topic["titulo"]), ST["title"]),
                 Paragraph("Objetivo: " + esc(topic["objetivo"]), ST["obj"]),
                 Paragraph("Goal: " + esc(topic["goal"]), ST["goal"]), Spacer(1, 6), remember_box(topic),
                 Spacer(1, 8)]
        total = 0
        allkeys = []
        for i, ex in enumerate(topic["ejercicios"], 1):
            head, body, pts, key = build_exercise(ex, i, mode, slug)
            total += pts
            allkeys.append((i, ex["titulo"], key))
            story.append(CondPageBreak(30 * mm))
            if ex["tipo"] in ("write", "fill", "choice", "match", "classify", "rewrite", "order"):
                story.append(KeepTogether(head + body))
            else:
                story.append(KeepTogether(head + body[:1]))
                story += body[1:]
            story.append(Spacer(1, 7))
        story.pop()  # sin espacio final
        doc = make_doc(f"{outdir}/{slug}-{mode}.pdf", topic, mode)
        doc.build(story)
        results["total"] = total
        results["keys"] = allkeys
    build_pauta(topic, results, outdir)
    return results["total"]


def build_pauta(topic, res, outdir):
    story = [Paragraph(esc(topic["titulo"]), ST["title"]),
             Paragraph("PAUTA DE CORRECCIÓN — USO DEL DOCENTE", ST["obj"]),
             Paragraph("Hoja de respuestas separada; no se entrega junto con la guía del estudiante. "
                       "Los ejercicios de producción son de respuesta personal. "
                       f"Puntaje total: {res['total']} puntos (1 punto por respuesta correcta). "
                       "Escala sugerida: 60 % de exigencia para nota 4,0.", ST["instr"]),
             Spacer(1, 8)]
    for n, title, key in res["keys"]:
        block = [Paragraph(f"Ejercicio {n} — {esc(title)}", ST["ph"]), Spacer(1, 2)]
        if key and isinstance(key[0], tuple):
            for _, k in key:
                block.append(Paragraph(arrows(k), ST["pans"]))
        else:
            txt = " · ".join(f"<b>{i + 1}.</b> {arrows(esc(k))}" for i, k in enumerate(key))
            block.append(Paragraph(txt, ST["pans"]))
        story.append(KeepTogether([boxed(block, colors.white, LINE, 5)]))
        story.append(Spacer(1, 5))
    doc = make_doc(f"{outdir}/{topic['slug']}-pauta.pdf", topic, "pauta")
    doc.build(story)
