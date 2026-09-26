# Calculadora "Faça a Sua Própria Ganache": contexto do trabalho (26/09/2026)

Use a skill `calculadora-ganache` (`.claude/skills/calculadora-ganache/SKILL.md`). A seção **ESTADO ATUAL** e as **Correções da Tatiana** mandam sobre o resto.

## Onde está
- **Branch:** `main-p86j61` · **PR #1** (rascunho) para `main`.
- **Prévia (artifact privado, abre no celular):** https://claude.ai/artifact/HFEk7pv8KywwcEAN8e8124. Depois de mudar, republique `capitulo ganaches/calculadora-ganache.html` nesse link.
- **Fonte (edite só este):** `capitulo ganaches/fontes/calculadora-src.html`
- **Rodar sempre, nesta ordem:**

      pip install pillow playwright
      python "capitulo ganaches/fontes/receitas-md.py"   # gera Receitas-autorais-100g.md a partir das receitas
      python "capitulo ganaches/fontes/montar.py"        # gera calculadora-ganache.html (arquivo único para a Hotmart)
      python "capitulo ganaches/fontes/testar.py"        # confere as contas; tem que dar 0 erros

## O que foi feito nesta sessão
1. **Celular:** conferido em 360 e 400 px. Corrigidos: a setinha do "Deu errado?" (o `montar.py` agora escapa o CSS), a proporção quebrando linha e a tabela do Guia larga demais.
2. **Receitas prontas:** agora são **17 no cardápio**, todas da Tatiana. Vêm do acervo `Receitas_integrais_calculadora.md` e das fotos das apostilas que ela mandou.
   - Uma sessão anterior tinha trocado sabores e quantidades. Isso foi desfeito.
   - **Títulos padronizados**, ditados por ela, para não usar os nomes das apostilas. Ex.: "Ganache de Chocolate Amargo 54% – Ponto de Bico", "Ganache de Coco (doce de leite, creme de abóbora e nozes)", "Ganache de Chocolate Branco com Caipirinha de Cupuaçu" (cupuaçu no lugar do cajá), "Ganache de Chocolate Ruby com Amora e Vinho" (amora no lugar da framboesa), "Ganache de Mel com Especiarias".
   - Saiu a de matcha. A 19 (ganache ao leite) fica **oculta**, só como base do Monte.
   - Tudo por **100 g de chocolate**, com o preparo, as medidas, as dicas e a validade. Sem "rende X bombons" nem "para cada X g" das apostilas.
   - A de limão com lavanda **não deixa trocar o limão**: só o chá, a erva ou o tempero.
3. **Motor (v3), decidido com a Tatiana:**
   - **Base = receitas dela, com chocolate importado.** O creme é o que a receita original diz: **creme UHT das apostilas = 25%**, fresco = 35%.
   - **A diferença entre tipos de chocolate vem das receitas de bico dela:** meio amargo 60 g, ao leite 40 g e branco 28 g de creme 25% para 100 g de chocolate.
   - **"Monte a sua ganache" clássica = receita 19:** 400 g de ao leite importado + 164 g de creme 25% + 32 g de glucose + 10 g de manteiga. O `testar.py` confere isso.
   - Os outros sabores partem da receita dela: fruta = cajá (polpa fervida com glucose e manteiga), chá = Earl Grey, licor = conhaque, pasta = pistache, coco e caramelo salgado.
   - **O chocolate é escolhido pelo % de cacau do rótulo**, não pelo nome amargo/meio amargo. A gordura do rótulo é opcional. Dentro do mesmo tipo, e entre nacional e importado, a conta segue a **manteiga de cacau** (literatura da Fase 1 e da Fase 2). Mais cacau pede mais creme.
   - **Troca de creme** (ex.: 25% → caixinha 17%): mantém a água, e **a gordura que falta entra como manteiga**.
   - **Glucose a mais: não entra.** O açúcar já passa do teto de 30–35% com chocolate nacional.
   - **A pessoa informa os gramas de CHOCOLATE**, e a calculadora dá o creme, a glucose, a manteiga e o **rendimento total em gramas**.
4. **Teste automático** (`testar.py`): percorre todas as combinações do Monte e todas as trocas das receitas. Confere também os números-base e as gramas e frases do preparo contra `Receitas-autorais-100g.md`.

## O que falta
- **Fotos:** colocar em `capitulo ganaches/fotos-receitas/`, com os nomes do `LEIA-ME.txt`, e rodar o `montar.py`.
- A Tatiana ainda não confirmou a quantidade de manteiga com creme de caixinha. Com 400 g de ao leite nacional e caixinha 17%, dá ~28 g. Ela achou 45 g "muito" (isso era com a base errada, de creme 35%).
- A 13 e a 14 (trufas) vieram sem modo de preparo, então usam o preparo da calculadora.
- A tabela do capítulo (`ganache-perfeita-src.html`) ainda usa os nomes "Amargo/Meio amargo". Mudar só se ela pedir.
- Testar pelo link da Hotmart.

## Como falar com a Tatiana
Português simples, frases curtas, sem termos técnicos. Ela usa o celular e é iniciante em tecnologia. Mande imagens das telas e o link da prévia. **Nunca mude sabor, nome ou número de receita dela sem ela pedir.**
