---
name: calculadora-ganache
description: Especificação completa para construir a calculadora "Faça a Sua Própria Ganache" (Volume 3 do ebook da Tatiana Duarte Moreira) como página web. Use sempre que for programar, testar, corrigir ou atualizar a calculadora de ganache, o cardápio de receitas prontas, o recálculo por substituição de ingredientes ou a tabela Ganache Perfeita.
---

# Calculadora de Ganache: especificação para o programador

Você é o **agente programador** deste projeto. A parte técnica (chocolate, ganache, proporções) já foi pesquisada e aprovada. Seu trabalho é **transformar isso numa página web que funcione**, sem inventar regra técnica nova.

## ⚠️ Decisões de 23–24/09/2026 (mandam sobre o resto deste arquivo)
Depois do teste da Tatiana com cobertura fracionada, que deu recheio e blindagem **moles**:
1. **Recheio, trufa e bombom: só chocolate de verdade.**
2. **Fracionado só na blindagem e na cobertura de bolo**, e só de marcas que indicam o produto para ganache. Esse preparo se chama **Falsa Ganache**.
3. **Com fracionado: nunca manteiga**, e o mínimo de gordura do leite.
4. **Fracionado branco: fora da calculadora** até a Tatiana testar.
5. **Toda receita gerada é conferida contra as proporções das receitas oficiais** antes de aparecer.
6. O cálculo é por **chocolate : líquido total** (seção 7). O modelo antigo de "igualar % de água e gordura" e a regra "+20% de fracionado" **foram descartados**.

Leia também: `capitulo ganaches/Conclusão para a calculadora de ganache.pdf` e `capitulo ganaches/Teste-23-09-e-receitas-oficiais.md`.

## ▶️ ESTADO ATUAL (25/09/2026): a v1 da calculadora JÁ EXISTE, com tema escuro. Continue a partir dela, não comece do zero.

**Arquivos**
- **Fonte da calculadora (edite este):** `capitulo ganaches/fontes/calculadora-src.html`
- **Fonte da tabela Ganache Perfeita:** `capitulo ganaches/fontes/ganache-perfeita-src.html` (conteúdo do capítulo 3; **não mude os números sem a Tatiana pedir**)
- **Gerar as versões finais:** `python "capitulo ganaches/fontes/montar.py"` gera `capitulo ganaches/calculadora-ganache.html` e `capitulo ganaches/ganache-perfeita.html` (arquivo único, pronto para a Hotmart). **Nunca edite os arquivos gerados à mão.** Precisa de Pillow (`pip install pillow`); sem ele, gera sem fotos e avisa.
- **O que o `montar.py` faz:** põe o cabeçalho com charset; troca acentos e símbolos por códigos (`&#NNN;` no HTML, `\uXXXX` no `<script>`, com par substituto para emojis, e `\XXXX ` no `<style>`), porque a Hotmart entrega o arquivo sem charset; diminui as fotos (lado maior 800 px, JPEG 75%) e embute como data URI; avisa se o arquivo passar de 5 MB.
- **Fotos:** `capitulo ganaches/fotos-receitas/` (nomes em `LEIA-ME.txt`: `capa.jpg`, `1.jpg`…`15.jpg`, `cremosa.jpg`, `estrutura.jpg`, `cobertura.jpg`). **A pasta ainda está sem fotos**; sem foto, aparece uma ilustração SVG.
- **Prévia para a Tatiana:** artifact privado https://claude.ai/artifact/HFEk7pv8KywwcEAN8e8124 (atualize republicando `capitulo ganaches/calculadora-ganache.html` com esse `url`).
- **Git:** branch `main-p86j61`, PR #1 (rascunho) para `main`.

**O que a v1 já faz**
- **Abas embaixo:** Início · Monte · Receitas · Guia. Barra do topo com o nome da calculadora.
- **Início** "Faça a Sua Própria Ganache", com dois botões grandes: **Monte a sua ganache** e **Receitas prontas**.
- **Monte a sua ganache:** passos numerados com botões em grade. Textura (Cremosa, Estrutura, Cobertura, em 3 cards com foto ou ilustração) · chocolate (7 tipos) · origem (nacional, importado, cobertura fracionada) · creme (35, 30, 25, 20, 17%) · sabor (clássica, fruta, chá/erva/especiaria, licor, pasta, coco, caramelo) · peso. Devolve receita em gramas + pizza + modo de preparo + avisos. A cobertura fracionada só libera **Estrutura/blindagem** (5 : 1, sem manteiga); nas outras texturas, bloqueia com o texto da Tatiana.
- **Receitas prontas:** as 19 de `Receitas-autorais-100g.md`. Em 25/09 a Tatiana mandou fotos das receitas (apostilas eduK e Callebaut): a 10 (cajá) foi corrigida; 16 (framboesa e vinho do Porto), 17 (cumaru e mel), 18 (matcha) e 19 (ganache ao leite) são novas; as fotos confirmaram a 9 (pistache) e a 15 (caramelo salgado). Creme UHT das fotos convertido para creme 30% com a mesma água (UHT = 73% de água). Na 18, a foto cortou o preparo: onde entra o matcha está a confirmar., em cards de 2 colunas com filtro por chocolate. A receita abre com foto grande e título por cima, linha de informações (ponto, rendimento, chocolate), pizza, ingredientes com bolinha de marcar, preparo e avisos. Dentro dela dá para: trocar o chocolate (tipo e origem), trocar qualquer ingrediente por outro do mesmo grupo (ex.: limão → abacaxi), tirar um sabor, escolher o peso final, voltar à original e imprimir/salvar em PDF.
- **Guia:** (1) tabela "Quanto chocolate para cada 1 g de creme" (creme 35%, nacional/importado, mesma fórmula da tabela Ganache Perfeita) + nota da Falsa Ganache; (2) "Deu errado? Veja como consertar", 6 casos em sanfona (talhou; não voltou nem com mixer; talhou com fruta ou licor; mole demais; empelotou ao bater; grossa e sem brilho), com base na Fase 2.
- **Regra de troca:** líquido por líquido mantém a **mesma quantidade de água**. Troca de chocolate reescala os líquidos pela régua da tabela Ganache Perfeita (`W = PROPORCAO × FIRME.importado ÷ FIRME[origem] ÷ 0,58`).
- **Receitas prontas mostram o preparo, as medidas ("raspas de ½ laranja", "6 folhas"), as dicas, as variações e a validade da própria Tatiana**, iguais a `Receitas-autorais-100g.md` (campos `prep`, `notas` e 3º elemento dos `itens`). Se ela trocar um ingrediente ou o tipo de chocolate, o preparo passa a ser o gerado pela calculadora, com aviso. Quando o arquivo de receitas mudar, atualize o `RECEITAS`: o `testar.py` confere gramas e frases do preparo contra o arquivo.
- No "Monte a sua ganache", o modo de preparo é gerado a partir dos ingredientes, com texto próprio (sem copiar fontes). Avisos de fruta ácida, abacaxi/kiwi (ferver), chocolate branco de supermercado (+10%), fracionada e "teste primeiro".
- Os dados ficam no topo do script (`DADOS: edite aqui`): TIPOS, TEXTURAS, FIRME, PROPORCAO, EXTRAS, FALSA, ING (ingredientes com % de água), GRUPOS, FAMILIAS, RECEITAS.

**Visual aprovado pela Tatiana (25/09): tema ESCURO com as cores do ebook.** Inspirado no app da Google Play "Chocolate Cake Recipes: Baking" (Beast code Studios): abas embaixo, cards com foto, receita com foto grande e título por cima, ingredientes com bolinha de marcar. Cores (tokens no `:root` do fonte): fundo azul-marinho escuro `#0E1626`, cartões `#16243E`/`#1D2E4D`, vinho `#8C3A3B` (botão principal, opção escolhida), ouro `#D4A24E`/`#B0863A` (sobretítulos, números, aba ativa, detalhes), texto creme `#F3ECE2`, títulos `#F3E3C9`, rosa `#D98B95` (ícones, líquido na pizza). Fontes: **Playfair Display** (títulos) e **Montserrat** (texto). Largura máxima 520 px. Na impressão, volta para fundo branco. **Não trocar esse visual sem a Tatiana pedir.**

**Conferido no celular (25/09), 360 e 400 px, Chromium:** barra de abas sempre no rodapé (a vez em que "apareceu no meio" era só a captura de tela da página inteira), sem rolagem para o lado, sem erro de script. Corrigidos: setinha do "Deu errado?" que aparecia como `&#` (o `montar.py` não escapava o CSS) e proporção "2,8 : 1" quebrando em duas linhas na tabela do Guia.
- Para testar de novo: `pip install playwright` (não rode `playwright install`; use `executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome'`), viewport 360×740, `is_mobile=True`, e tire capturas da **tela visível** (não `full_page`, que desenha a barra fixa no meio).

**MOTOR v3 (26/09): AS RECEITAS DA TATIANA SÃO A BASE** (o v2, que partia da tabela e da literatura, foi reprovado por ela: "a ganache ao leite saiu diferente da receita que eu dei")
- **Nível:** as receitas clássicas de bico dela, com chocolate importado e creme fresco 35%, por 100 g de chocolate: **meio amargo 54,5% = 60 g de creme · ao leite 33,6% = 40 g · branco 28% = 28 g** (`BASE_AGUA`). **A diferença entre TIPOS de chocolate vem daí** (meio amargo → ao leite: creme × 0,67; ao leite → branco: × 0,7). Blend = meio a meio; caramelo e ruby = pela tabela, a partir do branco e do ao leite.
- **Mesmo tipo, outro chocolate** (outro % de cacau, nacional, gordura do rótulo) e **outra textura**: a diferença vem da manteiga de cacau e da tabela Ganache Perfeita (`Wt`, relativo). A pessoa informa o **% de cacau do rótulo** (não o nome amargo/meio amargo) e, se quiser, a gordura em 100 g.
- **Monte a sua ganache:** parte da receita da autora de cada sabor (`MODELO`): clássica = bico (1, 2, 3), fruta = cajá (10, sem a cachaça), chá = Earl Grey (7), licor = conhaque (8), pasta = pistache (9), coco = 4, caramelo = 15. Depois balanceia para o chocolate, a textura e o creme escolhidos e troca o sabor mantendo a água.
- Receita com `tambem` (ex.: pistache = "branco ou ao leite") não muda as quantidades entre esses tipos, porque a própria receita dela diz isso.
- O `testar.py` confere que clássica + cremosa + importado + creme 35% devolve exatamente 60/40/28 g, que as diferenças entre texturas e origens seguem a tabela, e que mais cacau dá mais creme.
- A regra da polpa no caramelo saiu do Monte: a base de fruta é a receita de cajá dela (polpa fervida com glucose e manteiga). Confirmar com ela.

**Receitas prontas: decisão da Tatiana (26/09)** 
- **Todas as receitas da Tatiana são a BASE, feitas com chocolate IMPORTADO e CREME DE LEITE FRESCO 35%.** As quantidades são as das receitas originais dela (`Receitas_integrais_calculadora.md` e as fotos das apostilas eduK/Callebaut que ela mandou em 25/09), divididas para 100 g de chocolate. O creme das receitas originais é lido como creme fresco (é assim que ela quer), sem converter.
- A pessoa só escolhe **quanto quer fazer**. Se trocar para **chocolate nacional**, a calculadora refaz a proporção (`trocarChocolate`: líquidos × FIRME.nacional ÷ FIRME.importado), porque o nacional tem menos manteiga de cacau e fica mais mole, e mostra o aviso "Chocolate nacional".
- As 19 receitas: 1–3 bico (meio amargo, ao leite, branca/colorida); 4 coco (variações na mesma receita: doce de leite com nozes, doce de leite com coco, compota de abóbora); 5 cheesecake de frutas vermelhas; 6 limão siciliano e lavanda (**troca o chá/erva/tempero, nunca a fruta**: `trava`); 7 Earl Grey; 8 ao leite com conhaque; 9 pistache; 10 cajá com cachaça; 11 limão com manjericão; 12 hojichá; 13 trufa meio amargo (811); 14 trufa ao leite (823); 15 caramelo salgado; 16 framboesa e vinho do Porto; 17 cumaru e mel; 18 matcha; 19 ganache ao leite. Uma sessão anterior tinha trocado sabores e quantidades; **nunca mais troque sabor de receita dela.**
- 13 e 14 vieram sem modo de preparo (usa o da calculadora, com aviso). Na 18 a foto cortou o preparo: onde entra o matcha está a confirmar.
- **`Receitas-autorais-100g.md` é gerado** por `python "capitulo ganaches/fontes/receitas-md.py"` (precisa de node) a partir do `RECEITAS`. Não edite o .md à mão.
- **Regra da polpa (Tatiana, 25/09): polpa de fruta nunca vai crua; entra no caramelo, como na receita 15.** Feito no "Monte a sua ganache" (família Fruta): açúcar = (creme + polpa) × 32/94. As receitas 10 e 16 estão como nas fotos dela (polpa fervida com glucose e manteiga); perguntar se passam para o caramelo.

**Teste das contas:** depois do `receitas-md.py` e do `montar.py`, rode `python "capitulo ganaches/fontes/testar.py"`. Ele passa por todas as combinações do "Monte a sua ganache" (9.975) e todas as trocas das 15 receitas (630 telas) e reprova NaN, número negativo, peso errado e troca de líquido que muda a água. Em 25/09 achou creme **negativo** em coco + Estrutura + branco; agora esse caso (e qualquer sabor que tome todo o líquido) é bloqueado com sugestão de Cremosa ou Clássica. Rode sempre antes de enviar.
- Várias receitas prontas têm mais água que a régua da tabela (até 2,5×). É de propósito: bombom moldado, trufa oca e recheio de casca são mais moles. As receitas 2, 13 e 19 batem com a régua (100%). Não "corrija" esses números.

**O que falta fazer (nesta ordem, parando para a Tatiana aprovar cada item)**
1. **Tatiana ver a prévia no celular e aprovar** (link do artifact acima). Ajustar o que ela pedir.
2. **Revisão dos textos com a Tatiana** (voz de confeiteira, "você"), incluindo os 6 consertos do "Deu errado?", os avisos e o modo de preparo.
3. **Fotos:** quando ela mandar, colocar em `fotos-receitas/` com os nomes do LEIA-ME, rodar o `montar.py` e conferir o tamanho final (até ~5 MB).
4. Números "a confirmar" (% do creme nas receitas 4, 7 e 11; manteiga da 15) e marcar como `testada: true` as que a Tatiana testar.
5. "Adicionar à tela de início": ícone (SVG embutido) e `<meta name="apple-mobile-web-app-title">`.
6. Teste no link da Hotmart.

**Como falar com a Tatiana:** português simples, frases curtas, sem termos técnicos. Ela usa o celular e é iniciante em tecnologia. Mande imagens das telas e o link da prévia, e termine com o que ela precisa responder.

## 0. Antes de escrever qualquer código, leia

Os arquivos do capítulo estão em `INFO PRODUTO ATUAL/capitulo ganaches/` (a lista de receitas está em `INFO PRODUTO ATUAL/`):

| Arquivo | O que tem |
|---|---|
| `CONTEXTO_MESTRE_Calculadora_Ganache.docx` | briefing: público, voz, dados das fracionadas, regras |
| `CONTEXTO_RESUMIDO_4_Volumes.docx` | o produto inteiro (4 volumes) |
| `Fase-1-O-que-e-chocolate.md` | composição dos chocolates, lei, Falsa Ganache |
| `Fase-2-O-que-e-ganache.md` | emulsão, papel de cada ingrediente, por que talha |
| `ganache-perfeita.html` | a tabela de introdução, **já atualizada em 23/09** com as faixas oficiais (seção 7.3). Reaproveite visual e números. |
| `capitulo ganaches/Teste-23-09-e-receitas-oficiais.md` e o PDF de conclusão | **as regras e faixas atuais** |
| `Lista-receitas-prontas.md` | as 25 receitas prontas (numeradas de 1 a 25) que a Tatiana vai mandar |
| `capitulo ganaches/Receitas-autorais-100g.md` | **as receitas que vão para o cardápio** (Opção 2): versões autorais por 100 g de chocolate, creme 30%, com preparo próprio. **Não mostrar fontes no produto.** |
| `Receitas_integrais_calculadora.md` (na raiz) | o acervo original (uso interno, para conferir proporções). **Não publicar o texto dele.** |
| `capitulo ganaches/Analise-das-15-receitas.md` | a análise do acervo: proporções, o que falta e o que precisa confirmar. O preparo das receitas tem que ser **reescrito** no formato padronizado (não copiar o texto das apostilas). |
| `receitas-prontas.json` *(quando existir)* | as receitas dela convertidas (seção 5) |

Os `.docx` se leem com `unzip -p arquivo.docx word/document.xml`, removendo as tags.

## 1. Regras que mandam em tudo

1. **A receita testada da Tatiana ganha do modelo.** Se o cálculo reprovar uma receita dela que funciona, quem está errado é o cálculo: ajuste o modelo e avise.
2. **Não inventar número.** Composição sem fonte fica marcada como `estimado: true` e a interface mostra isso de forma discreta. Sem dado, escreva "não encontrado" e pergunte.
3. **Perguntar antes de assumir.** Decisões de produto são da Tatiana. Trabalhe em etapas e **pare para aprovação** no fim de cada uma (seção 9).
4. **Voz de confeiteira, nunca de químico.** O aviso é "vai ficar mole demais para cortar", não "atividade de água acima do limite". Português do Brasil, frases curtas.
5. **Cobertura fracionada não é chocolate.** A ganache feita com ela se chama **Falsa Ganache** e só existe na **blindagem e na cobertura de bolo**, sem manteiga.
6. **A IA não tem paladar.** Todo resultado termina lembrando que o teste na bancada é da confeiteira.
7. Não copie textos de fabricantes nem de livros. Números de composição podem ser usados, com crédito.

## 2. O produto

- **Nome:** Faça a Sua Própria Ganache · Volume 3 do ebook (capítulo 3). Nome do ebook ainda em aberto.
- **Rodapé fixo:** `Ferramenta do Volume 3 · Faça a Sua Própria Ganache · Tatiana Duarte Moreira`
- **Público:** confeiteira iniciante ou com pouca técnica, que usa muito cobertura fracionada, compra o que acha na região e não pode desperdiçar insumo. Usa **celular**.
- **Hospedagem:** arquivo enviado para o **Hotmart Drive**, que entrega o HTML sem charset. Por isso:
  - entregue **um único arquivo `index.html`** (HTML + CSS + JS juntos), sem depender de outros arquivos locais;
  - inclua `<meta charset="utf-8">` **e** escape os acentos (entidades numéricas `&#NNN;` no HTML e escapes unicode do tipo barra-invertida + `u00e9` no JS) no arquivo final, como já foi feito em `ganache-perfeita.html`;
  - só use bibliotecas de CDN público (cdnjs ou jsdelivr) e fontes do Google Fonts;
  - os dados ficam num bloco separado no **topo do script**, marcado `/* ===== DADOS: edite aqui ===== */`, para a Tatiana atualizar todo mês sem mexer no resto. Mantenha também os dados-fonte em arquivos `.json` na pasta `dados/` e um script simples `montar.py` que gera o `index.html` final (injeta os JSON e escapa os acentos).

## 2.1 As 3 texturas (decisão da Tatiana, revisada em 23/09)

| id | Textura | Serve para | Como fica |
|---|---|---|---|
| `firme` | Firme | trufa, bombom cortado, blindagem, tira de sustentação | enrola, corta e segura o bolo |
| `cremosa` | Cremosa | recheio de bolo, bombom recheado, de colher | macia, espalha e recheia |
| `cobertura` | Cobertura | drip cake, calda, decoração de bolo | bem mole, quase líquida |

Alinhado com as receitas oficiais: **Firme** = "firme (corte, trufa)" do PDF de conclusão. **Cremosa** = "cremoso (recheio de bolo, colher)". A blindagem com chocolate de verdade usa a faixa Firme até a Tatiana mandar receita própria (inferência, marcar assim). A **Falsa Ganache só existe na blindagem**, dentro da textura Firme. A grade tem 3 colunas: **Nacional · Importado · Falsa Ganache**.

Em toda a calculadora, "textura" é uma dessas três. O **uso** (trufa, drip etc.) é só um rótulo dentro da textura.

## 3. O fluxo da página (decisão da Tatiana, 23/09/2026)

```
[Início] EQUILÍBRIO PERFEITO
   a tabela Ganache Perfeita: 4 ingredientes, 3 texturas, proporções
    │
    ├─ OPÇÃO 1 (principal): "MONTE A SUA GANACHE"
    │     Passo 1 · Qual textura?   Firme · Cremosa · Cobertura
    │     Passo 2 · Qual chocolate? tipo (meio amargo, ao leite, branco…)
    │                               + nacional ou importado (ou a marca)
    │     Passo 3 · Qual sabor?     Clássica · Fruta · Pasta saborizante ·
    │                               Castanhas e frutas secas · Licor
    │     Passo 4 · Quanto quer fazer? (g)
    │     → RECEITA em gramas + pizza + modo de preparo + avisos
    │           └─ "Quero trocar um ingrediente" → recalcula
    │
    └─ OPÇÃO 2: "DICAS DE RECEITAS"
          as receitas testadas da Tatiana (10 a 15 na v1), em cardápio com foto
          → RECEITA
                ├─ "Mudar o peso" → escala
                └─ "Quero trocar um ingrediente" → recalcula + avisos
```

A antiga opção "tenho a minha receita" (digitar ou fotografar a receita da pessoa) **saiu da v1**. Se a Tatiana quiser, ela entra numa v2.

### 3.1 Início: Equilíbrio Perfeito
Reaproveite `capitulo ganaches/ganache-perfeita.html` (visual e números): os 4 ingredientes, as 3 texturas e a grade Ganache de Verdade × Falsa Ganache. A Falsa Ganache só aparece na blindagem. Essa página também é a introdução do capítulo no ebook. Termina com dois botões grandes: **"Monte a sua ganache"** e **"Dicas de receitas"**.

### 3.2 Opção 1: Monte a sua ganache (o coração da calculadora)
Uma pergunta por tela, com botões grandes (celular). Sempre mostra o caminho: "Firme › Meio amargo nacional › Fruta".

**Passo 1, textura:** Firme (trufa, bombom cortado, blindagem) · Cremosa (recheio de bolo, bombom recheado) · Cobertura (drip, calda).

**Passo 2, chocolate:**
- tipo: meio amargo, ao leite, branco, amargo, blend, caramelo, ruby;
- origem: nacional ou importado. Opcionalmente, a marca, da lista do banco (seção 4);
- **se escolher cobertura fracionada:** só libera a textura **Firme como blindagem**, só com marca permitida, e só com sabor Clássica (seção 7.1). Nos outros casos, mostra o aviso do adendo da Tatiana e sugere chocolate de verdade;
- **tipo sem faixa** (ex.: meio amargo cremoso, drip, amargo, blend, caramelo, ruby, enquanto não chegam as receitas): "Ainda não temos receita testada para essa combinação", com sugestão da combinação mais próxima que existe.

**Passo 3, sabor (família):**

| Família | O que a pessoa escolhe | Como entra na conta |
|---|---|---|
| **Clássica** | só chocolate e creme | todo o líquido é creme |
| **Fruta** | polpa, suco ou purê (maracujá, morango, limão, laranja…) | entra **no lugar** do creme, grama por grama. Limite de quanto do líquido pode ser fruta: **vem das receitas da Tatiana**. Referência que já funcionou: branco nacional 1 kg + creme 17% 150 g + limão 200 ml (fruta = 57% do líquido, 2,9 : 1, cremosa). |
| **Pasta saborizante** | pistache, avelã, maracujá industrializado… | **não é líquido**. Quantidade e ajuste vêm das receitas da Tatiana. Sem receita dela → "ainda sem receita testada". |
| **Castanhas e frutas secas** | pasta de pistache, amendoim, castanha 100% | têm gordura própria e amolecem a ganache. Ajuste vem das receitas da Tatiana. |
| **Licor** | rum, licor de laranja… | conta como líquido, no lugar do creme. Referência: Sicao trufas ao rum (360 g de meio amargo + 120 g de creme 35% + 40 g de rum). |

**Passo 4, quanto fazer:** peso final em gramas (padrão: 500 g).

**Resultado:** a proporção chocolate : líquido total é o **meio da faixa** da textura e do tipo (seção 7.3). O líquido é dividido entre creme e sabor pelas regras da família. Aparecem ingredientes em gramas, pizza, preparo padronizado (seção 6), a origem dos números ("receita oficial Harald", "receita testada da Tatiana"…) e os avisos. **Nunca** mostre uma receita fora da faixa.

**Nacional × importado (obrigatório, decisão da Tatiana 23/09):** a calculadora **sempre** pergunta se o chocolate é nacional ou importado, porque a lei muda a composição. No Brasil, chocolate precisa de no mínimo 25% de sólidos de cacau hoje (RDC 723/2022) e 35% a partir de maio de 2027 (Lei 15.404/2026), e pode ter até 5% de gordura vegetal. Na Europa (Diretiva 2000/36/CE), o mínimo é 35%, e a couverture tem pelo menos 31% de manteiga de cacau. O importado tem mais manteiga de cacau, e por isso pede **menos chocolate** para o mesmo ponto.
- **Nacional:** faixas das receitas oficiais brasileiras (seção 7.3).
- **Importado:** `faixa nacional × (MC+GV do nacional) ÷ (MC+GV do importado)`, com MC+GV: nacional meio 26 · ao leite 27 · branco 28; importado meio 37 · ao leite 30 · branco 29,5 (seção 4.1). Marcar como "calculado". Conferência: a trufa Callebaut 811 do acervo (receita 13: 2 : 1 com creme 35% ≈ 2,5 : 1 em creme UHT) bate com o cálculo (~2,6 : 1). Receitas testadas de importado substituem o cálculo.
- Mesmos números da tabela `ganache-perfeita.html`: firme meio amargo 3,75 (nac) / 2,64 (imp) · ao leite 4,4 / 3,96 · branco 5,5 / 5,22; cremosa ao leite 2,4 / 2,16 · branco 2,75 / 2,61.

### 3.3 Opção 2: Dicas de receitas
- **Cardápio** com as receitas testadas da Tatiana (10 a 15 na v1): foto, nome, textura, chocolate, sabor e o selo "Verdade" ou "Falsa (blindagem)". Filtros por textura, chocolate e sabor. Sem foto, use um card de cor sólida.
- **Página da receita:** ingredientes em gramas, rendimento, pizza, preparo padronizado, validade e onde guardar.
- **Mudar o peso:** escala tudo proporcionalmente (arredonda para 1 g, ou 5 g acima de 500 g).
- **"Quero trocar um ingrediente":** a pessoa escolhe qual e pelo quê → recalcula pela seção 7.4 e confere pela 7.5. Exemplos: meio amargo nacional → importado; creme 35% → caixinha; maracujá → morango; chocolate → fracionado (só se for blindagem).

**As receitas da Tatiana servem para duas coisas:** são o cardápio da Opção 2 **e** calibram as faixas e os limites de sabor da Opção 1. Por isso, cada família de sabor precisa de pelo menos uma receita testada dela.

### 3.4 Sempre visível
- Um **"por quê?"** clicável em cada aviso, com 1 a 3 frases tiradas das Fases 1 e 2.
- O **aviso da Falsa Ganache** sempre que a receita tiver cobertura fracionada.
- **Imprimir ou salvar em PDF:** botão com `window.print()` e CSS `@media print` que mostra só a receita.
- **Rodapé** da seção 2.

## 4. Banco de ingredientes (composição por 100 g)

Componentes, em **% do peso**:
`MC` manteiga de cacau · `SIG` sólidos de cacau isentos de gordura · `ACU` açúcares (sacarose + outros açúcares adicionados) · `LAC` lactose · `GL` gordura do leite · `SL` sólidos de leite sem gordura e sem lactose · `GV` gordura vegetal · `GO` outra gordura (castanhas, pasta) · `AGUA` · `ALC` álcool · `OUT` outros sólidos.

### 4.1 Chocolates e coberturas
Valores usados na tabela aprovada. ✅ = ficha oficial · ⚠️ = estimado.

| id | nome | MC | SIG | ACU | LAC | GL | SL | GV | fonte |
|---|---|---|---|---|---|---|---|---|---|
| imp-amargo | Valrhona Guanaja 70% | 42 | 28 | 29 | 0 | 0 | 0 | 0 | ✅ + cálculo |
| imp-meio | Callebaut 811 (54,5%) | 37 | 18,5 | 44 | 0 | 0 | 0 | 0 | ✅ |
| imp-leite | Callebaut 823 (33,6%) | 30 | 5 | 42 | 8,9 | 6 | 7,6 | 0 | ✅ + cálculo |
| imp-branco | Callebaut W2 | 29,5 | 0 | 46,5 | 9,3 | 6,3 | 7,9 | 0 | ✅ + cálculo |
| imp-blend | blend importado (média 811 e 823) | 33,5 | 11,75 | 43 | 4,5 | 3 | 3,8 | 0 | ⚠️ |
| imp-caramelo | Valrhona Dulcey 35% | 35,4 | 0 | 28,6 | 14,5 | 6,9 | 12,3 | 0 | ✅ receita + ⚠️ divisão do leite |
| imp-ruby | Callebaut Ruby RB1 | 29,7 | 17,6 | 26,4 | 10,8 | 6,3 | 9,2 | 0 | ⚠️ (a ficha oficial diverge entre embalagens) |
| nac-amargo | Harald Unique 70% | 38 | 32 | 29 | 0 | 0 | 0 | 0 | ⚠️ rótulo |
| nac-meio | Sicao Nobre meio amargo (40%) | 21 | 19 | 49 | 0 | 5 | 0 | 5 | ⚠️ rótulo |
| nac-leite | ao leite nacional típico | 22 | 6 | 48 | 7,6 | 5 | 6,4 | 5 | ⚠️ |
| nac-branco | branco nacional típico | 22 | 0 | 51 | 8,6 | 5 | 7,4 | 6 | ⚠️ |
| nac-blend | blend nacional típico | 21,5 | 12,5 | 48,5 | 3,8 | 5 | 3,2 | 5 | ⚠️ |
| frac-escuro | fracionada meio amargo/amargo (média das com liquor e só cacau em pó) | 1,5 | 7 | 55 | 2,2 | 0,5 | 1,8 | 31 | ⚠️ rótulo Harald Confeiteiro |
| frac-leite | fracionada ao leite | 0,5 | 3 | 53 | 5,7 | 1 | 4,8 | 32 | ⚠️ |
| frac-branco | fracionada branca | 0 | 0 | 55 | 5,9 | 1 | 5,1 | 33 | ⚠️ rótulo Harald TOP branco |
| frac-blend | fracionada blend | 1 | 5 | 54 | 3,8 | 0,75 | 3,2 | 31,5 | ⚠️ |

**Não use a composição das fracionadas para balancear receita** (erro do teste de 23/09). Ela serve só para explicar. Dados de rótulo das fracionadas no CONTEXTO_MESTRE: Harald Confeiteiro meio amargo (açúcar 59, gordura 31, saturada 30, proteína 2,8 por 100 g) e Harald TOP branco (gordura 35, saturada 33).
**Classificação automática:** se o ingrediente listado tiver "gordura vegetal" no lugar da manteiga de cacau, é fracionada, e a receita vira Falsa Ganache.
**Chocolate digitado à mão:** permita cadastrar um chocolate pela ficha técnica (MC, SIG, açúcar, sólidos de leite, gordura do leite, GV).

### 4.2 Laticínios e outros (⚠️ estimados: confira na TACO/USDA e marque a fonte)

| id | ingrediente | AGUA | GL | LAC | SL | ACU | GO | ALC | observação |
|---|---|---|---|---|---|---|---|---|---|
| creme-35 | creme de leite fresco 35% | 58 | 35 | 3 | 4 | 0 | 0 | 0 | |
| creme-20 | creme de leite caixinha 20% | 73 | 20 | 3,5 | 3,5 | 0 | 0 | 0 | caixinha pode ter espessante |
| creme-17 | creme de leite caixinha 17% | 76 | 17 | 3,5 | 3,5 | 0 | 0 | 0 | |
| leite | leite integral | 88 | 3 | 4,7 | 4,3 | 0 | 0 | 0 | |
| manteiga | manteiga sem sal | 16 | 82 | 0,5 | 1,5 | 0 | 0 | 0 | legislação BR: mín. 80% gordura, máx. 16% água |
| glucose | glucose de milho (xarope) | 20 | 0 | 0 | 0 | 80 | 0 | 0 | |
| invertido | açúcar invertido | 22 | 0 | 0 | 0 | 78 | 0 | 0 | |
| mel | mel | 18 | 0 | 0 | 0 | 82 | 0 | 0 | |
| acucar | açúcar refinado | 0 | 0 | 0 | 0 | 100 | 0 | 0 | |
| polpa-fruta | polpa ou purê de fruta (genérico) | 87 | 0 | 0 | 3 | 10 | 0 | 0 | cada fruta tem seu valor: usar a TACO |
| pasta-pistache | pasta de pistache 100% | 2 | 0 | 0 | 0 | 8 | 50 | 0 | ⚠️ |
| pasta-saborizante | pasta saborizante (genérica) | ? | ? | ? | ? | ? | ? | 0 | **não padronizada: pedir o rótulo** |
| licor | licor (genérico) | 50 | 0 | 0 | 0 | 25 | 0 | 25 | varia muito |

## 5. Receitas prontas: formato do dado

A Tatiana vai mandar as receitas pelo modelo de `Lista-receitas-prontas.md`. Converta cada uma para `dados/receitas-prontas.json`:

```json
{
  "codigo": 1,
  "nome": "Trufa de Maracujá",
  "tipo": "verdade",
  "chocolate_tipo": "meio",
  "textura": "firme",
  "uso_principal": "trufa",
  "familia": "F",
  "foto": "https://… (URL no Hotmart Drive) ou null",
  "ingredientes": [
    {"id": "nac-meio", "nome_rotulo": "Harald Melken meio amargo", "g": 300},
    {"id": "creme-35", "g": 100},
    {"id": "polpa-maracuja", "g": 50},
    {"id": "manteiga", "g": 20},
    {"id": "glucose", "g": 20}
  ],
  "rendimento_g": 490,
  "preparo_familia": "F",
  "validade": "7 dias na geladeira",
  "testada": true,
  "observacoes_autora": "texto dela"
}
```

As 25 receitas numeradas estão em `Lista-receitas-prontas.md` (use o número como `codigo`). Enquanto elas não chegam, use **no máximo 3 receitas de exemplo**, marcadas `"exemplo": true` e com o aviso "receita de exemplo" na interface.

## 6. Modo de preparo padronizado

Texto base por **família** (creme, fruta, pasta, fruta seca) + ajuste por **textura**. Temperaturas das Fases 1 e 2:
- **Emulsionar entre 35 e 40 °C** (Valrhona). Juntar o líquido quente ao chocolate **em 3 ou 4 partes**, mexendo do centro para fora até formar o "núcleo" liso e brilhante. Finalizar com mixer.
- **Manteiga** entra no fim, com a ganache a ~35 °C. **Glucose** vai aquecida junto com o líquido.
- **Fruta:** aquecer a polpa com a glucose e juntar em partes. Se for ácida, juntar a ganache a ~35 °C, nunca fervendo com o creme.
- **Pasta saborizante e fruta seca:** misturar a pasta ao chocolate derretido antes do líquido.
- **Firme:** trufa → geladeira até firmar e enrolar. Bombom cortado → despejar no aro e cristalizar a 16–18 °C por 12–24 h ⚠️. Blindagem → ponto de pomada, aplicar sobre o bolo gelado e alisar.
- **Cremosa:** bombom recheado → rechear a ~28–30 °C (escuros) ou ~26–28 °C (ao leite e branco) e deixar firmar a 16–18 °C antes de fechar (Wybauw; Morató; faixa ⚠️). Se for **batida**, descansar na geladeira de 4 a 12 h e bater devagar só até o ponto. Recheio de bolo → usar em ponto de pomada.
- **Cobertura:** usar a ~30–32 °C sobre bolo gelado (drip). Para calda, usar morna ⚠️.
- **Falsa Ganache:** derreter a cobertura a 40–45 °C, sem temperar, **sem manteiga**. Guardar na geladeira, validade curta.

A Tatiana revisa esses textos antes de publicar.

## 7. O cálculo (revisado depois do teste de 23/09/2026)

> **O motor antigo, que igualava % de água e gordura entre chocolate e fracionado, FALHOU no teste.** O modelo agora é por **proporção chocolate : líquido total**, conferida contra **faixas das receitas oficiais**. A composição em % (água, gordura) só serve para explicar e para avisar. Ela **nunca** decide uma receita sozinha.

### 7.1 Classificar antes de calcular
1. **Chocolate de verdade** (o rótulo diz "chocolate" e tem manteiga de cacau ou massa de cacau): ganache liberada em todas as texturas.
2. **Fracionado permitido** (a marca indica para ganache): **só blindagem e cobertura de bolo**. Lista atual:
   - Selecta Supreme meio amargo e blend: sim
   - Garoto Confeitaria (Nestlé Professional): sim
   - Harald Top: sim, só na blindagem
3. **Fracionado não permitido:** Sicao Mais, Sicao Fácil, Genuine fracionada (Cargill), Mavalério Premium. A ganache fica **bloqueada**, com a explicação.
4. **Fracionado branco (qualquer marca):** **bloqueado**. Não tem referência oficial, e foi o que falhou no teste.

### 7.2 Contar o líquido
- **Líquido total** = creme + leite + suco + polpa + licor + água + chantilly (todos em gramas; ml de líquido aquoso ≈ g).
- **Líquidos de sabor substituem o creme grama por grama.** Nunca somam por cima.
- Calcule **chocolate : líquido total** e compare com a faixa da seção 7.3.
- Glucose e manteiga não entram no líquido. Registre à parte: a manteiga é **proibida** com fracionado.

### 7.3 Faixas oficiais de partida (creme UHT 17–20%)
Fonte: `capitulo ganaches/Teste-23-09-e-receitas-oficiais.md` e o PDF "Conclusão para a calculadora de ganache".

| Ponto | Branco | Ao leite | Meio amargo | Origem |
|---|---|---|---|---|
| **Firme** (corte, trufa) | 5,5 : 1 | 4,4 : 1 | 3,5–4 : 1 | Harald Melken: trufas de corte e trufa bicolor |
| **Cremoso** (recheio de bolo, colher) | 2,5–3 : 1 | 2,3–2,5 : 1 | **sem referência oficial** | Harald ovo de colher · Sicao Nobre (35% + glucose) · Nestlé |
| **Blindagem com fracionado** (Falsa Ganache) | **bloqueado** | — | creme + chantilly 3 : 1 (Harald Top) · creme 5 : 1 (Selecta Supreme) · água 9 : 1 (fonte a confirmar) · chantilly vegetal 3,3–4 : 1 (média ~3,8) | marcas e prática |

- **Creme 35%:** use as receitas da Sicao como referência (branco 3 : 1, ao leite 2,3 : 1, com glucose).
- **Sem faixa = sem receita.** Amargo, blend, caramelo, ruby, meio amargo cremoso, blindagem com chocolate de verdade e cobertura/drip ficam **"sem referência ainda"** até a Tatiana mandar as receitas. O motor não inventa número para eles.
- **As receitas testadas da Tatiana substituem a faixa correspondente.** Guarde cada faixa com a origem: `oficial`, `pratica` ou `teste-tatiana`.

### 7.4 Troca de ingrediente (chocolate de verdade)
- **Troca de chocolate** (mesmo tipo, outra marca): manter o chocolate : líquido dentro da faixa do ponto. Se a receita estava no meio da faixa, mantenha a mesma posição relativa.
- **Troca de tipo** (ex.: meio amargo → branco): leve a proporção para a faixa do novo tipo no mesmo ponto (ex.: firme meio amargo 3,5–4 → firme branco 5,5).
- **Troca de creme (17/20 ↔ 35%):** use a faixa do creme certo. Se não houver faixa para aquele creme, avise.
- **Troca por fruta ou suco:** entra grama por grama no lugar do creme. Se ficar abaixo da faixa, **aumente o chocolate**, sem tirar o líquido de sabor, e avise.
- **Troca de chocolate de verdade por fracionado:** só é permitida se o destino for **blindagem ou cobertura de bolo** com marca permitida. Nesse caso, use as receitas de blindagem com fracionado (7.3), **tire a manteiga** e deixe a gordura do leite no mínimo. O chantilly vegetal completa o líquido melhor que mais creme. Em qualquer outro caso, **bloqueie**.
- **Não existe mais a regra "+20% de chocolate para fracionado"** (hipótese que falhou). Também saíram: o multiplicador 0,85 de líquido para fracionado, a pizza "Fracionado 5 : 1" e a regra de somar 5% de glucose com fracionado.

### 7.5 Validação obrigatória antes de mostrar qualquer receita
1. Classificação (7.1) feita.
2. Chocolate : líquido total dentro da faixa do tipo e do ponto. Fora da faixa → **aviso vermelho com a faixa esperada**, nunca uma receita "balanceada".
3. Fracionado + manteiga, manteiga de cacau ou chocolate de verdade misturado → **bloquear** e explicar que amolece.
4. Fracionado em recheio, trufa ou bombom → **bloquear** e sugerir chocolate de verdade. Se a pessoa insistir no recheio de bombom, mostre a proporção com o aviso: "Vai ficar puxento e com gosto de gordura. Não recomendamos: nem as fábricas indicam fracionado para recheio." (decisão da Tatiana)
5. Fracionado branco → **bloquear**.
6. Mostrar a **origem de cada número**: receita oficial, receita de prática ou teste da Tatiana.
7. Nunca igualar composição (% de água, gordura) entre chocolate e fracionado como se as gorduras fossem iguais.

### 7.6 Avisos (linguagem de confeiteira)

| Condição | Aviso |
|---|---|
| proporção abaixo da faixa (líquido demais) | "Vai ficar mole. Para [ponto] com [chocolate], use de X a Y g de chocolate para cada 100 g de líquido." |
| proporção acima da faixa | "Pouco líquido: pode ficar dura demais ou talhar." |
| fracionado em recheio, trufa ou bombom | "Cobertura fracionada não é ganache: no recheio fica mole, puxenta e com gosto de gordura. Use chocolate de verdade." |
| fracionado + manteiga | "Cobertura fracionada com manteiga amolece e não firma. Tire a manteiga." |
| fracionado branco | "Ainda não temos receita segura com cobertura branca fracionada." |
| marca não permitida | "Essa marca indica o produto só para banho e casca, não para ganache." |
| fruta ácida + creme | "Junte a fruta com a ganache a ~35 °C para o creme não talhar." |
| sem referência | "Ainda não temos receita testada para essa combinação." |

### 7.7 Preparo da Falsa Ganache (blindagem)
Derreter a 40–45 °C (Selecta: até 50 °C). **Nunca temperar.** Sem manteiga, sem manteiga de cacau e sem chocolate de verdade misturado. O chantilly vegetal completa o líquido melhor que mais creme. Aplicar logo. Se endurecer, micro-ondas em pulsos de 5 s. Na prática, o bolo coberto fica melhor fora da geladeira, com recheio que aguente temperatura ambiente.

## 8. Visual
- **O visual que vale é o tema escuro de "ESTADO ATUAL" (25/09).** A tabela `ganache-perfeita.html` continua com a identidade dela (Gloock + Figtree).
- **Celular primeiro:** funcionar bem com 360–400 px, botões grandes, sem rolagem lateral.
- A barra do semáforo mostra a faixa ideal como uma área sombreada e o valor como um marcador.

## 9. Etapas (pare no fim de cada uma e mostre para a Tatiana)

1. **Estrutura e navegação:** início (Equilíbrio Perfeito) → "Monte a sua ganache" (4 passos) e "Dicas de receitas" (cardápio), com telas de exemplo. Mostrar no celular.
2. **Motor de cálculo + testes:** implementar as seções 4 e 7 em JS puro, com funções testáveis. Testes obrigatórios:
   - **o teste de 23/09 tem que ser reprovado:** 600 g de fracionado branco + 95 g de creme 17% + 38 g de manteiga + 130 ml de limão, como recheio → bloqueado; 200 g de fracionado branco + 45 g de creme 17%, como blindagem → bloqueado;
   - a base que funciona tem que passar: 1 kg de branco nacional + 150 g de creme 17% + 200 ml de limão = 2,9 : 1, recheio cremoso branco → verde;
   - cada receita oficial da tabela 7.3 tem que dar verde no próprio ponto;
   - fracionado meio amargo Selecta 500 g + creme 100 g, como blindagem → verde; o mesmo como recheio → bloqueado com sugestão;
   - **caso real 1:** ganache de maracujá com pasta saborizante;
   - **caso real 2:** a ganache de laranja e morango que cobre o tiramisù de pão de mel (família fruta, a que mais desanda);
   - cada receita pronta da Tatiana tem que dar 🟢 no diagnóstico dela mesma. Se não der, ajustar a faixa e avisar.
3. **Opção 1 completa (Monte a sua ganache):** os 4 passos, a receita gerada, trocar ingrediente.
4. **Opção 2 completa (Dicas de receitas):** cardápio com as receitas da Tatiana, escalar, trocar ingrediente.
5. **Acabamento:** "por quê?", impressão, rodapé, versão final para a Hotmart (arquivo único com acentos escapados), teste abrindo o arquivo pelo link da Hotmart.

Em cada etapa, entregue a **lista do que foi testado** e o que ainda está como estimado.

## 10. Em aberto (perguntar para a Tatiana)
- Opção "tenho a minha receita" (digitar ou foto): fora da v1. Perguntar se entra numa v2.
- Fotos das receitas prontas: onde estão hospedadas.
- Faixas para blend, caramelo e ruby, que só vão existir depois das receitas dela.
- Validade e atividade de água: fica fora da v1, que só mostra a validade informada pela autora.
- Fichas técnicas oficiais da Sicao e da Mavalério (SAC).
- Sabor coco no "Monte a sua ganache": usa 22 g de leite de coco fixo (da receita 4). Na Estrutura com ao leite ou meio amargo nacional, sobram só 4 a 6 g de creme em 500 g. Perguntar se o coco deve ficar só na Cremosa ou se o leite de coco deve diminuir.
