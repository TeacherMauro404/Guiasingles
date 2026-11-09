"""Genera todas las guías PDF. Uso: python3 generar.py [slug ...]"""
import sys, os, importlib, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from motor import build_topic
OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
temas = []
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), "temas_*.py"))):
    temas += importlib.import_module(os.path.basename(f)[:-3]).TEMAS
sel = sys.argv[1:]
for t in temas:
    if sel and t["slug"] not in sel:
        continue
    total = build_topic(t, OUT)
    print(f"{t['slug']:32s} {len(t['ejercicios'])} ejercicios · {total} pts")

# Verificación: caracteres que Helvetica (WinAnsi) no puede mostrar
def _walk(o):
    if isinstance(o, str):
        yield o
    elif isinstance(o, dict):
        for v in o.values(): yield from _walk(v)
        for k in o.keys(): yield from _walk(k)
    elif isinstance(o, (list, tuple)):
        for v in o: yield from _walk(v)
bad = set()
for t in temas:
    for s in _walk(t):
        for ch in s:
            if ch != "→":
                try: ch.encode("cp1252")
                except UnicodeEncodeError: bad.add((t["slug"], ch))
if bad:
    print("ADVERTENCIA caracteres no soportados:", sorted(bad))
