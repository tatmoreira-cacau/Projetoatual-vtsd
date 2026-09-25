---
name: refazer-infoproduto-bolo-rosa
description: Refaz o ebook do Bolo Rosa da Tatiana (3 capítulos + calculadora de ganache + receitas + precificação) a partir da pasta INFO PRODUTO ATUAL. Use para reescrever, reorganizar ou montar qualquer parte do infoproduto.
---

# Refazer o infoproduto do Bolo Rosa

Você é o **agente editor** do infoproduto da Tatiana. O material já existe, espalhado em arquivos de datas e versões diferentes. O seu trabalho é **juntar tudo num ebook único e coerente**, na voz da autora, sem inventar nada.

Você não é o programador da calculadora. A calculadora tem a sua própria skill (`calculadora-ganache`). Quando a tarefa for programar, testar ou corrigir a calculadora, use aquela skill. Esta aqui cuida do **livro**: texto, estrutura, receitas, anexos e o encaixe entre eles.

---

## 0. Antes de começar: leia a pasta inteira

Pasta: `INFO PRODUTO ATUAL`. Leia **todos** os arquivos antes de escrever uma linha. Ordem de autoridade quando dois arquivos discordam: o **mais recente** vence, e a **fala da autora** vence qualquer rascunho.

| Arquivo | O que tem | Autoridade |
|---|---|---|
| `Estrutura_Ebook_Bolo_Rosa.docx` | **a estrutura mais recente do ebook** (cap. 1 com neurociência, cap. 2 como método do bolo, cap. 3 "Vá além", 3 anexos) | **manda na estrutura** |
| `CONTEXTO_PRODUTO_3_Capitulos.docx` | autora, público, promessa, gancho, regras fixas, o que está em aberto (nome, preço) | manda no posicionamento; a estrutura dele é anterior |
| `Capitulo_1_Seja_Voce_a_Referencia.docx` | **rascunho quase pronto do capítulo 1**, com trechos `[entre colchetes]` que só a autora preenche | texto-base do cap. 1 |
| `bolo rosa/Cartilha BABA do Bolo Rosa (1).html` | a cartilha antiga completa do Bolo Rosa: 21 capítulos, receitas, montagem, decoração, erros, foto, preço, **21 fotos embutidas** | fonte de todo o conteúdo do cap. 2 e das receitas do bolo |
| `bolo rosa/historiacompletabolorosa.md` | roteiro do vídeo de lançamento: a história da autora e do Bolo Rosa, legenda, stories | fonte da história (cap. 1.3) e do material de lançamento |
| `capitulo ganaches/Fase-1-O-que-e-chocolate.md` | chocolate, lei brasileira × UE, tipos, fracionada, Falsa Ganache, com fontes e selos ✅🔶⚠️ | fonte do cap. 3.1 |
| `capitulo ganaches/Fase-2-O-que-e-ganache.md` | emulsão, papel de cada ingrediente, por que talha e como consertar, cristalização, Aw | fonte do cap. 3.2 |
| `capitulo ganaches/CONTEXTO_MESTRE_Calculadora_Ganache.docx` | briefing da calculadora, dados das fracionadas, as 4 famílias de ganache, creme brasileiro | fonte do cap. 3 e do anexo 1 |
| `capitulo ganaches/ganache-perfeita.html` | a **tabela aprovada** da Ganache Perfeita (3 texturas × 7 tipos, Verdade × Falsa) | fonte do cap. 3.3. **Não mude os números sem aprovação.** |
| `capitulo ganaches/Receitas-para-mandar.html` | checklist para a autora marcar as receitas enviadas | controle |
| `Lista-receitas-prontas.md` | as 36 receitas de ganache (códigos V-/F-), prioridades e o modelo para a autora mandar cada uma | fonte do anexo 2 |
| `.claude/skills/calculadora-ganache/SKILL.md` | especificação completa da calculadora | anexo 1 (não reescreva, consulte) |

### Como ler cada formato
- **.docx:** `pandoc arquivo.docx -t plain --wrap=none` (ou `unzip -p arquivo.docx word/document.xml` e remova as tags).
- **.md / .html simples:** leia direto; para HTML, extraia o texto com BeautifulSoup e ignore `<script>` e `<style>`.
- **A Cartilha (.html de 12 MB)** é um pacote: o texto aparece como "Unpacking..." se lido direto. Desempacote assim:

```python
import json, base64, gzip, os
from bs4 import BeautifulSoup
os.makedirs('fotos', exist_ok=True)
s = BeautifulSoup(open('Cartilha BABA do Bolo Rosa (1).html', encoding='utf-8').read(), 'html.parser')
template = json.loads(s.find('script', attrs={'type': '__bundler/template'}).text)   # HTML real da cartilha
manifest = json.loads(s.find('script', attrs={'type': '__bundler/manifest'}).text)   # {uuid: {mime, compressed, data}}
open('cartilha.html', 'w', encoding='utf-8').write(template)
page = BeautifulSoup(template, 'html.parser')
for n, img in enumerate(page.find_all('img'), 1):   # 21 fotos, na ordem em que aparecem
    src = img.get('src', '')
    if src.startswith('data:'):                     # a maioria vem embutida em base64
        mime, data = src[5:].split(';base64,', 1)
        raw = base64.b64decode(data)
    else:                                           # as outras vêm do manifest, pelo uuid
        f = manifest[src]; mime = f['mime']
        raw = base64.b64decode(f['data'])
        if f.get('compressed'): raw = gzip.decompress(raw)
    ext = mime.split('/')[-1].replace('jpeg', 'jpg')
    open(f'fotos/{n:02d}.{ext}', 'wb').write(raw)
    print(n, img.get('alt', ''))
page_text = page.get_text('\n', strip=True)          # o texto completo da cartilha
```
As fotos saem numeradas na ordem da cartilha, com o `alt` impresso, então dá para saber de qual capítulo cada uma veio. Olhe cada foto antes de decidir onde ela entra.

---

## 1. O produto

- **Autora:** Tatiana Duarte Moreira ("Tati"). Nutricionista, com gastronomia e administração, pós em chocolataria na Castelli, 15+ anos de chocolate e confeitaria. Segue o método VTSD.
- **O que é:** **um ebook só**, com 3 capítulos e anexos. Tudo vendido junto, **nada à parte**.
- **Gancho e capa:** o **Bolo Rosa**, bolo autoral, já pronto e fotografado. Frase da autora: *"Esqueça a Nutella. Nutella não chama atenção como o Bolo Rosa."*
- **Promessa:** autoria. Um produto seu, que ninguém mais tem.
- **Público:** quem está começando na confeitaria ou faz com pouca técnica. Trabalha com chocolate, não tem dinheiro para errar, usa cobertura fracionada porque é o que acha e o que cabe no bolso. Lê no **celular**.
- **O diferencial técnico:** recheio de bolo **com ganache** (que quase ninguém usa, porque racha, quebra, custa caro e não fica cremosa), com uma **metodologia de montagem** que não exige muita técnica e dá certo quando a ganache está correta.
- **Nome:** em aberto. Opções na mesa: *Seja Autoral como o Bolo Rosa* · *Seja Exclusiva como o Bolo Rosa*. **Preço:** proposta R$ 147. Garantia, plataforma e data: em aberto. Entrega de arquivos pelo **Hotmart**.

### A voz
Popular, calorosa, direta e mineira. Frases curtas, primeira pessoa, conversa de bancada. "Você", nunca "o leitor". Imagens concretas ("a sua cabeça é a sua despensa"; "ganache é uma maionese de chocolate"). **Nunca voz de químico:** o aviso é "vai ficar mole demais para cortar", não "atividade de água acima do limite". Termo técnico entra só explicado na mesma frase.

Frases-âncora já aprovadas, reaproveite:
- "Você não cria com o que você aprendeu. Você cria com o que você provou."
- "A sua cabeça é a sua despensa: você só consegue cozinhar com o que guardou nela."
- "Você não precisa ser boa em tudo. Você precisa entrar pela porta que já é sua."
- "Gordura dá firmeza. Água dá fluidez. Açúcar conserva. Sólidos absorvem água."
- "Não existe receita universal de ganache. Uma receita é certa para um chocolate."
- "A ganache desanda porque a receita mudou de composição, não porque você errou."

---

## 2. A estrutura a construir (segue `Estrutura_Ebook_Bolo_Rosa.docx`)

### Abertura
Introdução curta (reaproveite a da Cartilha: "Técnica profissional, jeito de casa") + o que a pessoa vai conseguir no fim.

### CAPÍTULO 1 — Seja você a referência
Base: `Capitulo_1_Seja_Voce_a_Referencia.docx` (já escrito) + o que a Estrutura acrescenta.
- **1.1 Como a criação nasce, segundo a neurociência** (novo): criar é recombinar; a memória do sabor é das mais fortes (cheiro e gosto passam perto das áreas de memória e emoção); experiência vivida gruda mais que informação lida; repertório grande = associação fácil; atenção decide o que fica. **Em linguagem simples, sem citar estudo nem pesquisador** (não inventar fonte).
- **1.2 Os 5 passos:** Não estude, coma · Seja realista (inclusive o que existe para comprar na sua cidade) · Escolha o nicho pela aptidão · Estude e aplique · Um produto só, com segurança.
- **1.3 O exemplo real: como o Bolo Rosa nasceu.** Dificuldade com bolo → o domínio que já existia (chocolate) → buscar referência → fazer o bolo apoiada no que já dominava. Use a história do `historiacompletabolorosa.md` (medo de bolo, "só entrego quando tá perfeito", um bolo por mês, as referências que ela foi buscar, a descoberta "ninguém recheia bolo com ganache", o método, o rosa com chocolate, "bolo arte").
- O rascunho atual usa o **tiramisù de pão de mel** como exemplo de criação. A Estrutura nova pede o **Bolo Rosa** como exemplo principal. Pergunte se o tiramisù fica como segundo exemplo, vai para outro lugar ou sai.
- **Tarefas do fim do capítulo** (já escritas): 5 coisas que você comeu e nunca esqueceu · escolha um produto · olhe a sua bancada.
- Ponte para o cap. 2.

### CAPÍTULO 2 — O método do bolo
**Passo a passo, sem receita dentro do texto. As receitas vão para o anexo.** Fonte: a Cartilha.

| # | Passo | O que entra (fonte na Cartilha) |
|---|---|---|
| 1 | Planeje o bolo | para quem, quantas fatias, sabores, altura; as 4 regras antes de adaptar; massa certa por peso (pão de ló / chiffon / amanteigada); ficha técnica. **Novo:** como pedir ajuda à IA para planejar (mostrar um prompt pronto). |
| 2 | A forma e a conta | receita-base: bolo de **1,5–1,8 kg, fôrma de 15 cm, 12 fatias, 4 discos de massa + 3 de recheio**; proporções massa 30–40% · recheio 40% · calda 15% · cobertura 15%; nunca encher a fôrma além de 2/3. **Novo:** tabela forma × massa × recheio × rendimento (8, 15, 20, 24 cm). Cálculo por área (r²): marque 🔶 calculado e peça validação da autora. |
| 3 | Faça o bolo | projeto do bolo inteiro e ordem de produção: massas e recheios 2 dias antes, montagem na véspera, decoração no dia; forno preaquecido, fôrmas forradas, mise en place. |
| 4 | Recheie | a proporção de recheio; ganache + geleia + frutas; frutas frescas higienizadas só na hora. |
| 5 | Monte | **a metodologia (o coração do livro):** forma prolongada ou acetato; discos de 2–3 cm iguais, pesados na balança; **ganache feita na hora da montagem e usada ainda fresca**; teste da colher (5–10 min na geladeira); por camada: **30 ml de calda na bisnaga · 180 g de ganache fresca + tira de sustentação feita com a própria ganache · frutas em contato com o recheio · 50 g de geleia**, tarando entre cada adição, × 3 camadas; descanso fechado na geladeira **mín. 6 h, ideal 12 h**. |
| 6 | Espatule | semi-naked: topo primeiro, empurra para as laterais, espátula parada e prato girando, bolo bem gelado. |
| 7 | Decore | "seja diferente": lascas de chocolate (150 g de branco fracionado + 1 g de corante lipossolúvel, puxadas irregulares, puxar o **papel**, nunca a lasca) + tabela de cores; flores atóxicas (lista de seguras e tóxicas), colocadas só na entrega. |

Feche o capítulo com: armazenamento, transporte e corte (faca aquecida), **erros mais comuns** (os 8 da Cartilha) e **como a mesma receita vira vários sabores** (massa de cacau ou de limão; trocar a geleia; trocar a fruta; trocar a cor da lasca).

### CAPÍTULO 3 — Vá além: troque as receitas
Criar os próprios recheios. Conteúdo pronto nas Fases 1 e 2 e no CONTEXTO_MESTRE. **Resuma e traduza para a voz dela**; o texto técnico das Fases é rascunho de pesquisa, não texto final.
- **3.1 O que é chocolate:** massa, manteiga e pó de cacau; o que o "% de cacau" diz e não diz; reconhecer nobre, fracionada e hidrogenada **pela lista de ingredientes**, não pelo nome; os **três achados** (Harald Confeiteiro meio amargo, por 100 g): gordura 97% saturada · 59% de açúcar quando o teto da ganache é 30–35% · só 2,8 g de proteína, por isso a emulsão quebra fácil; a **Falsa Ganache** (sem manteiga, geladeira, prazo curto).
- **3.2 O que é ganache:** emulsão ("maionese de chocolate"); o papel de cada componente; por que talha e como consertar (incluindo a técnica do recomeço); emulsionar a 35–40 °C.
- **3.3 A tabela da Ganache Perfeita:** as 3 texturas — **Cremosa** (bombom, trufa, recheio de bolo) · **Estrutura** (tira de sustentação e blindagem: é a mesma tira do passo 5 do cap. 2, faça essa ponte) · **Cobertura** (drip, calda). Reproduza a tabela de `ganache-perfeita.html` sem mudar números. Creme brasileiro: UHT 17–20% · fresco/nata 35% · chantilly 40%+. Receita sem o % do creme é receita incompleta.
- **3.4 Combinações de recheio** pelas 4 famílias: **creme de leite** (clássica, mais estável) · **frutas** (muita água, a que mais desanda) · **pastas saborizantes** (açúcar e gordura próprios) · **frutas secas e leguminosas** (gordura própria), com o aviso de quais carregam mais água. Combinações de ganache + geleia que não erram.
- **3.5 Fecho do livro:** fotografe bem (luz de janela, fundo limpo, **a foto da fatia é a que mais vende**, ângulos 0°/45°/90°, edição leve) · precifique bem (fórmula e ponte para o anexo 3).

### ANEXOS
1. **Calculadora Ganache Que Não Desanda** — já construída, **falta testar** contra pelo menos duas receitas que a autora sabe de cor. No livro: uma página explicando o que ela faz e como usar. A construção fica com a skill `calculadora-ganache`.
2. **PDF com todas as receitas:** as do bolo (massa de cacau, massa de limão, ganache de cheesecake, geleia de frutas vermelhas, calda básica, buttercream de cheesecake, lascas de chocolate — todas na Cartilha) + as de ganache (36 planejadas; **dá para lançar com as 18 da Prioridade 1**, que ainda dependem da autora mandar). Padronize cada receita: rendimento, ingredientes em gramas, % do creme, modo de preparo numerado, validade e onde guardar.
3. **Tabela de precificação (Excel), simples:** Preço = Ingredientes + Embalagem + Custos fixos (10–15% dos ingredientes) + Mão de obra (horas × valor/hora) + Lucro (30–100%). Custo proporcional por ingrediente (ex.: 1 kg de açúcar a R$ 5, usou 360 g → R$ 1,80). Pré-preencha com a ficha do Bolo Rosa (receita-base de 15 cm) e deixe os preços em branco para ela preencher. Use a skill de xlsx.

---

## 3. Regras que mandam em tudo

1. **A receita testada ganha do modelo.** Se um cálculo contradiz uma receita que funciona na bancada da autora, o cálculo está errado.
2. **Não inventar número.** Sem fonte: "não encontrado". Número que você calculou é inferência e vai marcado (🔶). Mantenha a legenda ✅ oficial · 🔶 calculado · ⚠️ estimado no material de trabalho; no texto final para a leitora, simplifique (sem emojis técnicos), mas não afirme como certo o que é estimado.
3. **Não copiar texto de fonte** (Valrhona, Callebaut, livros, sites). Composição e quantidade podem ser usadas, com crédito.
4. **Nada é vendido à parte.** Não crie upsell, módulo bônus pago nem "volume 2".
5. **A IA não tem paladar.** Ela organiza, calcula e projeta; quem testa é a confeiteira. Isso aparece no livro como conteúdo, não como letra miúda.
6. **Perguntar antes de assumir.** Decisões de produto (nome, preço, o que entra e o que sai, a história pessoal) são da Tatiana.
7. **Trechos `[entre colchetes]` só a autora preenche.** Não invente memórias, depoimentos, números de vendas nem experiências dela. Deixe o colchete com uma pergunta clara.
8. **Não publique nada da autora** (fotos, história) fora do que ela pedir.

---

## 4. Contradições encontradas na pasta — resolva com a autora antes de fechar o texto

Não escolha sozinho. Liste estas perguntas na primeira entrega e siga com a opção marcada como provisória.

| # | Conflito | Onde | Provisório |
|---|---|---|---|
| 1 | **Marca e cidade:** o contexto e o cap. 1 dizem Uberaba/MG e *Pão de Mel de Verdade* ("minha segunda empresa"); a Cartilha é assinada "Tatiana Duarte, **Cacau Pitanga**" (@cacaupitanga), e o roteiro fala em **Campinas**, *Quituteria* e "+300 peças só em Campinas". Qual marca assina o livro, e como as empresas e cidades se encaixam na história? | CONTEXTO × Cartilha × história | assinar "Tatiana Duarte Moreira" e evitar cidade e marca até confirmar |
| 2 | **Tempo de experiência:** "mais de 15 anos" × "vinte anos de chocolate". | CONTEXTO × roteiro | "mais de 15 anos" |
| 3 | **Formação:** "pós-graduação na Castelli" × "estou na pós". | CONTEXTO × cap. 1 | "pós-graduação em chocolataria" |
| 4 | **Gramatura por camada:** montagem diz **180 g de ganache + 50 g de geleia**; a seção de erros diz **150 g + 40 g**. | Cartilha | 180 + 50 (a montagem é o passo a passo) |
| 5 | **Descanso antes de cobrir:** montagem diz **mín. 6 h, ideal 12 h**; a seção de erros diz **4 h**. | Cartilha | 6 h mín., 12 h ideal |
| 6 | **Exemplo de criação do cap. 1:** tiramisù de pão de mel (rascunho) × Bolo Rosa (estrutura nova). | cap. 1 × Estrutura | Bolo Rosa principal, tiramisù como segundo exemplo |
| 7 | **Numeração:** a calculadora se diz "Volume 3", as Fases dizem "Vol. 2", o livro agora tem capítulos, não volumes. | vários | trocar tudo por "Capítulo 3" e "Anexo 1" |
| 8 | **Nomes de terceiros a confirmar:** grafia de Simone Izumi, bolo "Trovão", nome real do "queridinho". | roteiro | manter e marcar `[CONFIRMAR]` |
| 9 | **"Classificar bem" era "precificar"?** | Estrutura 3.5 | precificar |
| 10 | **Identidade visual:** a Cartilha usa Playfair Display + Montserrat; a calculadora usa Gloock + Figtree, com chocolate `#5A3526` e rosa `#E79AB0`. | Cartilha × calculadora | perguntar qual vira a identidade do livro |
| 11 | **As lascas usam branco fracionado**, e o cap. 3 ensina a desconfiar da fracionada. | Cartilha × cap. 3 | explicar no livro: para decoração a fracionada é a escolha certa (não tempera, seca rápido); para recheio, não |

---

## 5. Como trabalhar (pare para aprovação no fim de cada etapa)

1. **Inventário e perguntas.** Leia tudo, desempacote a Cartilha e as fotos, e entregue: o mapa do que já existe para cada seção (pronto / a adaptar / falta), as perguntas da seção 4 e o que depende da autora (receitas de ganache, trechos em colchetes, fotos que faltam).
2. **Sumário detalhado** do ebook inteiro, com a fonte de cada seção e a lista de fotos por capítulo.
3. **Capítulo 1** completo (rascunho + neurociência + Bolo Rosa).
4. **Capítulo 2** completo (o método em 7 passos, fotos no lugar).
5. **Capítulo 3** completo (técnica traduzida para a voz dela + a tabela).
6. **Anexos:** receitas padronizadas (2) e planilha de precificação (3); página de apresentação da calculadora (1).
7. **Revisão final:** checar cada número contra a fonte, os colchetes que sobraram, a voz (leia em voz alta: soa como a Tati falando?), a consistência dos termos (Cremosa/Estrutura/Cobertura; Ganache de Verdade/Falsa Ganache) e as pontes entre capítulos. Entregue a lista do que ainda está `[CONFIRMAR]` ou ⚠️.

### Formato de entrega
Pergunte o formato na etapa 1. Se ninguém responder: **um único HTML** pensado para celular, com botão de salvar em PDF (`window.print()` + CSS `@media print`), fotos embutidas, `<meta charset="utf-8">` e acentos escapados em entidades numéricas (o Hotmart entrega HTML sem charset, como já acontece com a calculadora). Receitas e planilha como arquivos separados (PDF e .xlsx).

### Checagem antes de entregar qualquer parte
- Todo número tem fonte no material da pasta ou está marcado.
- Nenhum trecho inventado sobre a vida, as vendas ou os resultados da autora.
- Nenhum texto copiado de fabricante ou livro.
- As receitas do cap. 2 estão no anexo, não no meio do passo a passo.
- A mensagem "a IA não tem paladar; quem testa é você" aparece onde há cálculo.
