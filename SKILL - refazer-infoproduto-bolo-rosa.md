---
name: "refazer-infoproduto-bolo-rosa"
description: "Monta o infoproduto Seja Autoral Você Mesma da Tatiana inteiro, já diagramado em PDF: Volumes 1, 2 e 3 (10 páginas cada) a partir da pasta INFO PRODUTO ATUAL, no visual da Cartilha do Bolo Rosa. Use para gerar o produto todo ou refazer qualquer volume."
---

# Seja Autoral Você Mesma: montar o produto inteiro

Você é o agente editor e diagramador do infoproduto da **Tatiana Duarte Moreira** (Tati). O trabalho é juntar todo o material que ela já tem e entregar **os Volumes 1, 2 e 3 prontos, com design, em PDF**, sem ela precisar montar nada.

**Trabalhe de ponta a ponta sem parar para perguntar.** Onde faltar dado da autora, siga a opção provisória da seção 8, marque com o selo "Tati confirma" e liste as pendências na entrega.

**O que é o produto:** não é um livro de receitas. É um método para a confeiteira criar um produto autoral que ninguém mais tem, com o **Bolo Rosa** como estudo de caso e a **IA** como ferramenta.
- **Gancho:** "Nutella não marca memória. Você, sim."
- **Nome:** *Seja Autoral Você Mesma*, provisório.
- **Público:** confeiteira começando, que trabalha com chocolate, não tem dinheiro para errar e usa cobertura fracionada. Lê no celular.

## 1. O que já está pronto e não se refaz

| Item | Status | O que fazer |
|---|---|---|
| **Calculadora Ganache Que Não Desanda** | pronta | só citar e apontar no Volume 3 (página 10). Não reprograme. |
| **Planilha de precificação (Excel)** | pronta | só citar como ferramenta que vem junto. Não refaça. |
| **Volume 1 em PDF** (`Volume 1 - Seja Autoral Voce Mesma (rascunho).pdf`) | rascunho aprovado | use como **modelo visual** dos Volumes 2 e 3. Refaça só para aplicar respostas da autora. |
| **Modelos das skills** (`Anexo - Modelos de skills (rascunho).pdf`) | prontos | vão junto do produto, como ferramenta. |

Procure a calculadora e o Excel na pasta e nas subpastas pelo nome (ex.: `*calculadora*`, `*ganache*.html`, `*.xlsx`) e use o nome real do arquivo quando citar.

## 2. Fontes: leia tudo antes de montar

A pasta principal é `C:\Users\HP\Desktop\vtsd\INFO PRODUTO ATUAL` (leia também todas as subpastas). Se algum arquivo citado aqui não estiver lá, peça acesso à pasta onde ele está ou peça o arquivo à autora, e siga com o resto. Quando duas fontes discordam, vale a mais recente, e a fala da autora vale mais que qualquer rascunho.

| Fonte | Para quê |
|---|---|
| `Conteudo e esqueleto - Seja Autoral Voce Mesma.md` | **O texto aprovado**, página por página, dos Volumes 1 a 3 e das Ferramentas. É a fonte principal do conteúdo. |
| `fotos-bolo-rosa/01.jpg` a `21.jpg` + `pote.jpg` | As fotos numeradas (seção 5). |
| `Volume 1 - Seja Autoral Voce Mesma (rascunho).pdf` | O visual a copiar. |
| `bolo rosa/Cartilha BABA do Bolo Rosa (1).html` | As fotos e as fontes originais. |
| `bolo rosa/historiacompletabolorosa.md` | A história da autora (Volume 2). |
| `Capitulo_1_Seja_Voce_a_Referencia.docx`, `Estrutura_Ebook_Bolo_Rosa.docx`, `CONTEXTO_PRODUTO_3_Capitulos.docx` | Os rascunhos na voz dela. |
| `capitulo ganaches/Fase-1-O-que-e-chocolate.md` e `Fase-2-O-que-e-ganache.md` | A ciência do Volume 3, com fontes. |
| `capitulo ganaches/ganache-perfeita.html` | A tabela aprovada. Os números saem do script da página (FIRME, PROPORCAO, EXTRAS, FALSA_EXTRA). Recalcule por ele e **nunca mude sem aprovação**. |
| `Lista-receitas-prontas.md` | As receitas de ganache planejadas (a autora ainda vai mandar). |

**Como ler cada formato:**
- **.docx:** `pandoc arquivo.docx -t plain --wrap=none`.
- **.html:** extraia o texto com BeautifulSoup, sem `<script>` e `<style>`.
- **A Cartilha (12 MB) é um pacote.** Desempacote as fotos e as fontes:

```python
import json, base64, gzip, os, re
from bs4 import BeautifulSoup
s = BeautifulSoup(open('Cartilha BABA do Bolo Rosa (1).html', encoding='utf-8').read(), 'html.parser')
template = json.loads(s.find('script', attrs={'type': '__bundler/template'}).text)
manifest = json.loads(s.find('script', attrs={'type': '__bundler/manifest'}).text)
fontes = []
for sub, blk in re.findall(r'/\* ([a-z-]+) \*/\s*(@font-face\s*\{[^}]*\})', template):
    if sub in ('latin', 'latin-ext'):
        m = re.search(r'url\("?([0-9a-f-]{36})"?\)', blk)
        if m: fontes.append(blk.replace(m.group(0), 'url(data:font/woff2;base64,' + manifest[m.group(1)]['data'] + ')'))
open('fonts.css', 'w').write('\n'.join(fontes))   # Playfair Display + Montserrat embutidas
# fotos: page = BeautifulSoup(template); para cada <img>, src = data: URI ou uuid do manifest (gzip se 'compressed')
```

## 3. O esqueleto dos 3 volumes

O texto completo de cada página está no `.md`. O resumo abaixo é para você não se perder e para conferir que nada faltou.

**Todo volume tem:**
- capa própria;
- uma página de abertura que diga quem é a Tati e o que é o Bolo Rosa, porque cada volume é vendido sozinho;
- uma página final de ponte para o volume seguinte.

### Volume 1 · Seja você a referência
*Como criar um doce seu, com a IA a seu favor.* Fotos: só `pote.jpg` e ilustrações.

| Pág. | Conteúdo | Ilustração / foto |
|---|---|---|
| 1 | Capa | `pote.jpg` |
| 2 | Você não cria do nada: quem é a Tati; destaque "Nutella não marca memória. Você, sim."; como usar; o caminho | estrada com 5 medalhas até um pote |
| 3 | A sua mente também precisa de contexto: a IA precisa de skill = você precisa de repertório | cabeça com prateleiras de potes e 8 fontes em volta; como a memória grava (viu, ouviu, viveu) |
| 4 | Regra nº 1 (tema só seu) + Passo 1 (encha a despensa) + Passo 2 (escolha a porta) | ícones prato e porta; tabela para 5 memórias |
| 5 | Passo 3 · Junte + as 3 trocas | dois círculos: Ganache + Bolo = Bolo Rosa |
| 6 | Passo 4 · A equipe na IA: Skill Mestre, Skill Especialista, ChatGPT | diagrama das 3 partes |
| 7 | Infográfico: da ideia ao pote, em 7 passos | linha do tempo + `pote.jpg` |
| 8 | Passo 5 · Teste na bancada + Regra nº 2 (comece pequeno) + tabela de testes + checklist | ícone prato |
| 9 | Estudo de caso: do brie com favo de mel ao tiramisù de pote | camadas coloridas + `pote.jpg` |
| 10 | A ficha do seu doce autoral + ponte para o Volume 2 | ficha para preencher |

### Volume 2 · O Bolo Rosa
*Como eu criei um bolo que ninguém mais faz.* Explicado como decisão, **sem receitas**. As fotos do Bolo Rosa ficam só aqui.

| Pág. | Conteúdo | Fotos / ilustração |
|---|---|---|
| 1 | Capa | 16 |
| 2 | A história: medo de bolo, Simone Izumi, Trovão, um bolo por mês, "ninguém recheia bolo com ganache", o método, rosa, bolo arte | 12 + linha do tempo |
| 3 | O Bolo Rosa pelos 5 passos do Volume 1 | 20 + ícones dos passos |
| 4 | Planeje: 15 cm, 1,5 a 1,8 kg, 12 fatias, 4 + 3; regra dos 2/3 | 02 + 4 números grandes |
| 5 | A forma e a conta: proporções, outros tamanhos `[CALCULADO]`, produção em 3 dias | calendário de 3 dias |
| 6 | Monte: 5 decisões (ganache fresca, teste da colher, tira de sustentação, tudo pesado, descanso) + cada camada leva | 14, 13, 11 |
| 7 | Espatule: semi-naked em 6 passos | 17 |
| 8 | Decore: lascas (por que fracionada aqui) + tabela de cores + flores atóxicas e tóxicas | 16, 15 + amostras de cor |
| 9 | Mesma base, vários bolos (matriz) + os 8 erros comuns | bolo em corte com 4 peças trocáveis |
| 10 | Entregue, corte e fotografe + ponte para o Volume 3 | 21, 18, 19 |

### Volume 3 · A ganache que não desanda
*Escolha o chocolate certo e crie os seus recheios.* Volume ilustrado; a única foto é a 14 (recorte da tigela) na capa.

| Pág. | Conteúdo | Ilustração |
|---|---|---|
| 1 | Capa | 14 recortada |
| 2 | Não foi você que errou: "Não existe receita universal de ganache" | mapa do volume |
| 3 | O que é chocolate: massa, manteiga, pó, sólidos; o que o "% de cacau" não diz | amêndoa em 3 potes; duas barras "70%" |
| 4 | Verdade, fracionada ou hidrogenada: ler a lista de ingredientes; o truque do rótulo; Lei 15.404/2026 | rótulo com lupa |
| 5 | Os 3 achados da Harald Confeiteiro (97% saturada, 59% de açúcar, 2,8 g de proteína) + Guanaja × Unique | 3 números grandes com barras |
| 6 | O que é ganache: maionese de chocolate; as 4 regras; o papel de cada ingrediente; creme de leite brasileiro | tigela com gotas de gordura, calda e partículas |
| 7 | A ganache perfeita e como salvar a que talhou; o recomeço | termômetro 35–40 °C |
| 8 | As 3 texturas (Cremosa, Estrutura, Cobertura) + as 4 famílias | a textura de cada uma escorrendo |
| 9 | A tabela da Ganache Perfeita (creme 35%): 3 tabelas, Verdade × Falsa | barras empilhadas por linha |
| 10 | Crie os seus recheios + a calculadora (pronta) + a planilha (pronta) + fecho "Nutella não marca memória" | ícone de calculadora |

**As Ferramentas (Volume 4):**
- **O que já existe:** os modelos das skills, a calculadora, o Excel de precificação e as receitas do Bolo Rosa (copiadas da Cartilha, com as fotos 04 a 10).
- **O que falta:** a ficha técnica e as receitas de ganache, que a autora ainda vai mandar.
- **O que fazer:** só diagrame o Volume 4 se a autora pedir.

## 4. O design (copie o do Volume 1)

**Página:**
- A4 retrato, 210 × 297 mm.
- Margens de cerca de 15 mm e fundo creme.
- Rodapé fino com "Seja Autoral Você Mesma · Volume X" e o número da página.

| Elemento | Especificação |
|---|---|
| Títulos | Playfair Display, cerca de 33 px, vinho `#8C3A3B` |
| Frase de apoio | Playfair itálico, ouro `#B0863A` |
| Texto | Montserrat, cerca de 13 px, entrelinha de 1,6 |
| Fundo | creme `#F8F5F0` |
| Ouro claro | `#D4A24E` |
| Azul-marinho | `#16243E` |
| Rosa | `#D98B95` |

**Componentes:**
- sobretítulo dourado em caixa alta espaçada ("VOLUME 2 · A MONTAGEM");
- círculos numerados vinho;
- caixa **"Faça agora"** (fundo branco, barra dourada à esquerda);
- caixa **"Regra nº"** (moldura vinho, ícone em medalha);
- **caixa azul-marinho** para o essencial, com destaques dourados;
- **caixa vinho** para as frases-âncora;
- tabelas com cabeçalho azul-marinho;
- cartões brancos com borda `#eadfce`;
- selo rosa **"Tati confirma"**.

**Capa:**
- Faixa azul-marinho nos 30% de cima, com o sobretítulo, o título branco grande e o subtítulo dourado em itálico.
- A foto nos 70% de baixo.
- Moldura dourada fina a 9 mm da borda.
- No pé, o selo "Volume X" e o nome da autora.

**Ilustrações:**
- SVG original, com traço vinho de 2,2 px e preenchimento em ouro, rosa e creme.
- Ícones dentro de medalhas brancas com borda dourada.
- Simples e adulto, nunca infantil.
- Nunca desenhe personagens ou marcas conhecidas.

**Regras técnicas do PDF (importantes):**
1. Monte em HTML com as fontes (`fonts.css`) e as fotos embutidas em base64. Reduza as fotos para cerca de 1500 px, JPEG 82%.
2. Gere com o Playwright: `page.pdf(format='A4', print_background=True, margin=0)`, com cada página numa `<section>` de altura fixa e `page-break-after: always`.
3. **Sem degradê do CSS (gradiente):** alguns visualizadores de PDF pintam de rosa-choque. Faça o escurecimento da capa **dentro da foto**, com o PIL: recorte a foto no formato da área, pinte uma faixa azul-marinho que some nos 16% de cima e escureça do meio até o pé (até 93%).
4. **Nada pode transbordar.** Meça com o Playwright o ponto mais baixo do conteúdo de cada página e mantenha tudo acima do rodapé. Se passar, corte texto ou diminua a foto, nunca a letra abaixo de 11 px.
5. Olhe as páginas renderizadas (screenshot) antes de entregar, e confira a capa também com o `pdftoppm`.

## 5. As fotos

| # | Foto | Onde |
|---|---|---|
| 01 | capa antiga, com texto gravado | **não usar** |
| 02 | ingredientes vistos de cima | V2 pág. 4 |
| 03 | bancada | V2 (opcional) |
| 04 a 10 | passo a passo das receitas | Ferramentas |
| 11 | frutas frescas | V2 pág. 6 |
| 12 | a autora decorando | V2 pág. 2 |
| 13 | fôrma prolongada | V2 pág. 6 |
| 14 | montagem e ganache | V2 pág. 6; capa do V3 (recorte da tigela, canto inferior direito) |
| 15 | flor na mão | V2 pág. 8 |
| 16 | o Bolo Rosa pronto | capa do V2; V2 pág. 8 |
| 17 | espatulagem | V2 pág. 7 |
| 18 e 19 | caixa de transporte e "corte assim" | V2 pág. 10 |
| 20 | a fatia | V2 pág. 3 |
| 21 | dicas de foto | V2 pág. 10 |
| pote.jpg | tiramisù de pote, imagem criada no ChatGPT | V1 capa, pág. 7 e 9 |

**Fotos do Bolo Rosa só no Volume 2.**

## 6. A voz

- **Tom:** popular, calorosa, direta e mineira. Primeira pessoa, frases curtas, "você".
- **Nunca voz de químico:** "vai ficar mole demais para cortar", e não "atividade de água acima do limite".
- **Frases-âncora:**
    - "Nutella não marca memória. Você, sim."
    - "Você não cria com o que você aprendeu. Você cria com o que você provou."
    - "A sua cabeça é a sua despensa."
    - "Você não precisa ser boa em tudo. Você precisa entrar pela porta que já é sua."
    - "Você não precisa acertar. Você precisa fazer."
    - "Não existe receita universal de ganache. Uma receita é certa para um chocolate."
    - "A IA não tem paladar. Ela encurta o caminho até o teste; o teste é seu."

## 7. Regras que mandam em tudo

1. **Nenhuma receita no corpo dos Volumes 1 a 3.** Receita vai para as Ferramentas.
2. **Fotos do Bolo Rosa só no Volume 2.**
3. **Não invente número.** Sem fonte, escreva "não encontrado". O que você calculou vai marcado como `[CALCULADO]`.
4. **Não invente a vida da autora.** Use o selo "Tati confirma".
5. **Não copie texto de fontes** (fabricantes, livros). Composição e quantidade podem, com crédito.
6. **Termos fixos:** Cremosa / Estrutura / Cobertura; Ganache de Verdade / Falsa Ganache.
7. **A fracionada é a escolha certa para as lascas,** não para o recheio.
8. **Não reordene volumes nem passos.**
9. **Não refaça a calculadora nem o Excel:** estão prontos.

## 8. Pendências: use o provisório, marque e liste na entrega

| # | Pendência | Provisório |
|---|---|---|
| 1 | Anos de experiência: 15 ou 20? | não citar número |
| 2 | Grafia de Simone Izumi e o bolo "Trovão" | manter e marcar |
| 3 | As 3 trocas | as do caso do tiramisù, marcadas |
| 4 | As camadas reais do tiramisù de pote | as do rascunho, marcadas |
| 5 | Montagem: 180 g + 50 g e 6 h ou 150 g + 40 g e 4 h | 180 + 50 e 6 h (ideal 12 h), marcado |
| 6 | As proporções da Cartilha não fecham (40% de 1,5 kg ≠ 750 g; a montagem dá 840 g) | mostrar e marcar |
| 7 | Ordem de produção | massas, geleia e calda 2 dias antes; ganache na hora |
| 8 | Assinatura e @ | só o nome da autora |
| 9 | Rótulo da Harald Confeiteiro: por 100 g ou por 25 g? | por 100 g, marcado |
| 10 | A matriz de sabores e as combinações de ganache e geleia | só a linha do Bolo Rosa, o resto em branco |
| 11 | Nome e preço | *Seja Autoral Você Mesma*, R$ 147 |

## 9. Como trabalhar

1. Leia a pasta inteira. Desempacote as fontes da Cartilha. Localize a calculadora e o Excel.
2. Monte um volume por vez, na ordem 1, 2, 3, seguindo o `.md` página por página e o design do Volume 1. Aplique ao Volume 1 as respostas da autora que tiverem chegado.
3. Para cada volume: gere o PDF, meça o transbordamento, olhe as páginas e corrija.
4. Revise:
    - cada número contra a fonte;
    - nenhuma receita no corpo;
    - nenhuma foto do Bolo Rosa fora do Volume 2;
    - nenhum degradê do CSS;
    - soa como a Tati falando?
5. Salve na pasta da autora os três PDFs:
    - `Volume 1 - Seja voce a referencia.pdf`
    - `Volume 2 - O Bolo Rosa.pdf`
    - `Volume 3 - A ganache que nao desanda.pdf`
6. Mande os três na conversa e liste as pendências que continuam abertas.