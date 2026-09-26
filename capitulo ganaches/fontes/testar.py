# Confere as contas da calculadora: todas as combinações do "Monte a sua ganache"
# e todas as trocas das receitas prontas (sem NaN, sem número negativo, peso certo,
# troca de líquido mantendo a mesma água). Rode depois do montar.py:
#   pip install playwright      (não rode "playwright install" na nuvem)
#   python "capitulo ganaches/fontes/testar.py"
import os, sys, tempfile
from playwright.sync_api import sync_playwright
AQUI = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(os.path.dirname(AQUI), 'calculadora-ganache.html')
CHROME = '/opt/pw-browsers/chromium-1194/chrome-linux/chrome'
JS=r"""()=>{
function ruim(h){return /NaN|undefined|Infinity|>-\d|null g|null%/.test(h);}
var out={monte:0,monteErr:[],rec:[],swapErr:[],recN:0};
// clássica + cremosa + ao leite importado + creme 25% + 400 g de chocolate = a receita base da Tatiana (164 g de creme, 32 g de glucose, 10 g de manteiga)
(function(){
  B={tex:'cremosa',tipo:'leite',origem:'importado',cacau:null,gord:null,creme:'creme25',fam:'classica',esc:null,peso:400};
  var d=document.createElement('div'); d.innerHTML=buildRecipe(); var g=[].map.call(d.querySelectorAll('.ingr .g'),function(x){return x.textContent}).join(' ');
  if(g!=='400 g 164 g 32 g 10 g') out.monteErr.push('base ao leite: '+g);
})();
// a diferença entre tipos segue as receitas de bico dela (60 / 40 / 28 g de creme 25%)
if(Math.abs(W('escuro','importado','cremosa')/W('leite','importado','cremosa')-40/60)>1e-9||Math.abs(W('branco','importado','cremosa')/W('leite','importado','cremosa')-40/28)>1e-9) out.monteErr.push('escada de tipos');
// as diferenças entre texturas e entre nacional/importado seguem a tabela Ganache Perfeita (Wt)
['escuro','leite','branco'].forEach(function(t){ ['cremosa','estrutura','cobertura'].forEach(function(tx){ ['importado','nacional'].forEach(function(o){
  var a=W(t,o,tx)/W(t,'importado','cremosa'), b=Wt(t,o,tx)/Wt(t,'importado','cremosa');
  if(Math.abs(a-b)>1e-9) out.monteErr.push('relativo '+t+' '+o+' '+tx);
});});});
// mais cacau → menos chocolate por creme (mais perto de 1 : 1)
['cremosa','estrutura','cobertura'].forEach(function(tx){ ['importado','nacional'].forEach(function(o){ for(var c=36;c<=89;c++){ if(W('escuro',o,tx,c+1)>W('escuro',o,tx,c)+1e-9) out.monteErr.push('escuro '+o+' '+c+'% '+tx+' não diminui'); } }); });
// todos os % de cacau no Monte
['escuro','leite','branco'].forEach(function(t){ var fx=TIPOS[t].faixa; ['importado','nacional'].forEach(function(o){ for(var c=fx[0];c<=fx[1];c+=2.5){ Object.keys(TEXTURAS).forEach(function(tex){
  B={tex:tex,tipo:t,origem:o,cacau:c,gord:null,creme:'creme35',fam:'classica',esc:null,peso:500}; var h=buildRecipe(); out.monte++;
  if(ruim(h)) out.monteErr.push('cacau '+[t,o,c,tex].join('/'));
});}});});

var creme=['creme35','creme30','creme25','creme20','creme17'];
Object.keys(TEXTURAS).forEach(function(tex){Object.keys(TIPOS).forEach(function(tipo){Object.keys(ORIGENS).forEach(function(o){
 if(!existe(tipo,o)&&o!=='fracionada') return;
 creme.forEach(function(c){Object.keys(FAMILIAS).forEach(function(f){(FAMILIAS[f].lista||[null]).forEach(function(e){
  B={tex:tex,tipo:tipo,origem:o,creme:c,fam:f,esc:e,peso:500}; var h=buildRecipe(); out.monte++;
  if(ruim(h)) out.monteErr.push([tex,tipo,o,c,f,e].join('/'));
  var m=h.match(/<span class="g">([0-9,]+) g/); if(m&&m[1]!=='500') out.monteErr.push('chocolate '+m[1]+' '+[tex,tipo,o,c,f,e].join('/'));
 });});});
});});});
RECEITAS.forEach(function(r){
  var a=agua(r.itens), alvo=100/W(r.tipo,r.origem,r.tex);
  out.rec.push([r.id,r.nome,r.tipo,r.origem,Math.round(a*10)/10,Math.round(alvo*10)/10,Math.round(a/alvo*100)]);
  Object.keys(TIPOS).forEach(function(t){['nacional','importado'].forEach(function(o){
    abrir(r); trocarChocolate(t,o); drawRec(); out.recN++;
    abrir(r); if(TIPOS[t].cacau){ trocarChocolate(t,o,TIPOS[t].faixa[1]); drawRec(); out.recN++; if(ruim(document.getElementById('rec-out').innerHTML)) out.swapErr.push(r.id+' cacau max '+t+'/'+o); }
    if(ruim(document.getElementById('rec-out').innerHTML)) out.swapErr.push(r.id+' choc '+t+'/'+o);
  });});
  r.itens.forEach(function(it,i){
    var g=grupoDe(ING[it[0]].cat);
    Object.keys(ING).filter(function(id){return GRUPOS[g].indexOf(ING[id].cat)>=0}).concat(['__tirar']).forEach(function(n){
      abrir(r); trocarItem(i,n); M.rec.peso=1000; drawRec(); out.recN++;
      var h=document.getElementById('rec-out').innerHTML;
      if(ruim(h)) out.swapErr.push(r.id+' '+it[0]+'->'+n);
      var m=h.match(/<span class="g">([0-9,]+) g/); if(!m||m[1]!=='1000') out.swapErr.push('chocolate '+r.id+' '+n);
      if(n!=='__tirar'&&ING[it[0]].w&&ING[n].w&&Math.abs(agua(M.rec.itens)-agua(r.itens))>0.01) out.swapErr.push('agua '+r.id+' '+n);
    });
  });
});
return out;}"""
h = open(HTML, encoding='utf-8').read()
# abre uma porta para o teste enxergar as funções de dentro do script
h = h.replace('<script>\n(function(){', '<script>\n(function(){window.__T=function(src){return eval(src)();};', 1)
tmp = os.path.join(tempfile.gettempdir(), 'calculadora-teste.html')
open(tmp, 'w', encoding='utf-8').write(h)
with sync_playwright() as p:
    b = p.chromium.launch(**({'executable_path': CHROME} if os.path.exists(CHROME) else {}))
    pg = b.new_page(); errs = []
    pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + tmp)
    o = pg.evaluate('src=>window.__T(src)', '(' + JS + ')')
    telas = pg.evaluate('src=>window.__T(src)', "(function(){return RECEITAS.map(function(r){abrir(r);return document.getElementById('rec-out').innerText.replace(/\\s+/g,' ')})})")
    b.close()
# cada receita pronta tem que mostrar as gramas e o preparo do arquivo da Tatiana
import re
md = open(os.path.join(os.path.dirname(AQUI), 'Receitas-autorais-100g.md'), encoding='utf-8').read()
difs = []
for n, bloco in enumerate(re.split(r'\n## \d+\. ', md)[1:]):
    tela = telas[n]
    for g, nome in re.findall(r'^- (\d+) g de ([^\n(*]+)', bloco, re.M):
        if not re.search(r'(^|\D)' + g + r' g', tela): difs.append('receita %d: %s g de %s' % (n + 1, g, nome.strip()))
    prep = re.search(r'\*\*Preparo:\*\* (.*)', bloco)
    if prep and 'igual à receita' not in prep.group(1):
        for frase in re.split(r'(?<=\.) ', prep.group(1)):
            if frase.strip() and frase.strip() not in tela: difs.append('receita %d, preparo: %s' % (n + 1, frase.strip()))
o['swapErr'] += difs
print('Monte a sua ganache: %d combinações, %d com erro' % (o['monte'], len(o['monteErr'])))
for e in o['monteErr'][:20]: print('   ', e)
print('Receitas prontas: %d telas, %d com erro' % (o['recN'], len(o['swapErr'])))
for e in o['swapErr'][:20]: print('   ', e)
print('Água de cada receita pronta x a das receitas de bico da autora (bombom e trufa oca são mais moles de propósito):')
for r in o['rec']: print('   %2d %-48s %5.1f g  x %5.1f g  (%d%%)' % (r[0], r[1], r[4], r[5], r[6]))
print('Erros de script:', errs or 'nenhum')
sys.exit(1 if o['monteErr'] or o['swapErr'] or errs else 0)
