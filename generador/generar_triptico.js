// Genera los PDF del proyecto "Tríptico de predicciones" desde proyectos/triptico.html
// Uso: node generador/generar_triptico.js
const { chromium } = require('playwright');
const path = require('path');
const root = path.resolve(__dirname, '..');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  for (const [modo, landscape] of [['guia', false], ['pauta', false], ['plantilla', true]]) {
    await p.goto('file://' + path.join(root, 'proyectos/triptico.html') + '?modo=' + modo, { waitUntil: 'load' });
    await p.evaluate(() => document.fonts.ready);
    const out = path.join(root, `triptico-predicciones-${modo}.pdf`);
    await p.pdf({ path: out, format: 'Letter', landscape, printBackground: true,
      margin: landscape ? { top: '8mm', bottom: '8mm', left: '8mm', right: '8mm' } : { top: '9mm', bottom: '9mm', left: '11mm', right: '11mm' } });
    console.log(path.basename(out));
  }
  await p.goto('file://' + path.join(root, 'proyectos/triptico-slides.html'), { waitUntil: 'load' });
  await p.evaluate(() => document.fonts.ready);
  await p.pdf({ path: path.join(root, 'triptico-predicciones-presentacion.pdf'), width: '10in', height: '5.625in', printBackground: true, margin: { top: 0, bottom: 0, left: 0, right: 0 } });
  console.log('triptico-predicciones-presentacion.pdf');
  await b.close();
})();
