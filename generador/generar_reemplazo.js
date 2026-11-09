// Genera los PDF de las guías de reemplazo a partir de reemplazo/guia.html
// Uso: node generador/generar_reemplazo.js
const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');
const root = path.resolve(__dirname, '..');
const src = fs.readFileSync(path.join(root, 'reemplazo/guias.js'), 'utf8');
const ids = [...src.matchAll(/\{ id:"([^"]+)"/g)].map(m => m[1]);
(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const id of ids) {
    for (const modo of ['guia', 'pauta']) {
      const url = 'file://' + path.join(root, 'reemplazo/guia.html') + `?g=${id}` + (modo === 'pauta' ? '&pauta=1' : '');
      const warns = [];
      page.removeAllListeners('console');
      page.on('console', m => { if (m.type() === 'warning' || m.type() === 'error') warns.push(m.text()); });
      await page.goto(url, { waitUntil: 'load' });
      await page.evaluate(() => document.fonts.ready);
      const out = path.join(root, 'reemplazo', `${id}-${modo}.pdf`);
      await page.pdf({ path: out, format: 'Letter', printBackground: true, margin: { top: '9mm', bottom: '9mm', left: '10mm', right: '10mm' } });
      console.log(out.replace(root + '/', ''), warns.join(' | '));
    }
  }
  await browser.close();
})();
