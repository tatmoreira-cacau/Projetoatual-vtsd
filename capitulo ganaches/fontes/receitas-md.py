# Gera "capitulo ganaches/Receitas-autorais-100g.md" a partir do RECEITAS da calculadora-src.html,
# para o texto do livro e a calculadora nunca ficarem diferentes. Uso: python receitas-md.py (precisa de node)
import io, json, os, re, subprocess
AQUI = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(AQUI, 'calculadora-src.html'), encoding='utf-8').read()
bloco = lambda nome: src[src.index('var %s = ' % nome):]
def js_obj(nome, fim):
    t = bloco(nome); return t[:t.index(fim) + len(fim)]
codigo = js_obj('TIPOS', '\n};') + '\n' + js_obj('ING', '\n};') + '\n' + js_obj('RECEITAS', '\n];') + '\nconsole.log(JSON.stringify({TIPOS:TIPOS,ING:ING,RECEITAS:RECEITAS}));'
d = json.loads(subprocess.run(['node', '-e', codigo], capture_output=True, text=True, check=True).stdout)
TIPOS, ING, REC = d['TIPOS'], d['ING'], d['RECEITAS']
g = lambda x: ('%g' % x).replace('.', ',')
out = ['# Receitas da Tatiana · base de 100 g de chocolate',
       '*Volume 3 · Faça a Sua Própria Ganache · Tatiana Duarte Moreira · gerado a partir da calculadora (fontes/receitas-md.py)*', '',
       '**Base de todas as receitas:** chocolate **importado** e **creme de leite fresco 35%**, com as quantidades das receitas originais da Tatiana. '
       'Com outro chocolate a proporção muda: a calculadora refaz a conta pela manteiga de cacau do chocolate (% de cacau do rótulo), para dar o mesmo ponto.', '',
       '**Como ler:** toda receita está escrita para **100 g de chocolate**. Para fazer mais, multiplique tudo, ou use a calculadora.', '', '---', '']
for r in REC:
    out.append('## %d. %s' % (r['id'], r['nome']))
    nome = (TIPOS[r['tipo']]['n'].lower() + ' ' if r['tipo'] != 'escuro' else '') + ('%s%% cacau ' % g(r['cacau']) if r.get('cacau') else '')
    out.append('**Uso:** %s · **Chocolate:** %simportado' % (r['uso'], nome))
    out.append('- 100 g de chocolate %simportado' % nome)
    for it in r['itens']:
        nome = ING[it[0]]['n']; nome = nome[0].lower() + nome[1:]
        out.append('- %s g de %s%s' % (g(it[1]), nome, (' (%s)' % it[2]) if len(it) > 2 else ''))
    out.append('')
    if r.get('prep'): out.append('**Preparo:** ' + ' '.join(r['prep']))
    for n in r.get('notas', []): out.append('**%s** %s' % (n[1], n[2]))
    out.append('')
io.open(os.path.join(os.path.dirname(AQUI), 'Receitas-autorais-100g.md'), 'w', encoding='utf-8', newline='\n').write('\n'.join(out))
print('gerado: Receitas-autorais-100g.md (%d receitas)' % len(REC))
