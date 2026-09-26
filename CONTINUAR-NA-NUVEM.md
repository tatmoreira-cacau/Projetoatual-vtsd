# Continuar a calculadora de ganache

Use a skill `calculadora-ganache` (`.claude/skills/calculadora-ganache/SKILL.md`).
Edite só `capitulo ganaches/fontes/calculadora-src.html` e gere as versões finais com:

    python "capitulo ganaches/fontes/montar.py"

## Já feito (25/09/2026)
1. **Fotos ligadas:** o `montar.py` diminui (800 px, JPEG 75%) e embute as fotos de `capitulo ganaches/fotos-receitas/` (nomes no LEIA-ME). Sem foto aparece uma ilustração SVG. A pasta ainda está sem fotos.
2. **Novo visual aprovado pela Tatiana:** tema **escuro com as cores do ebook** (fundo azul-marinho escuro, vinho nos botões, ouro nos detalhes, Playfair Display + Montserrat), inspirado no app da Google Play "Chocolate Cake Recipes: Baking" (Beast code Studios). Tem:
   - abas embaixo: Início · Monte · Receitas · Guia;
   - passos numerados com botões em grade (textura em 3 cards com foto ou ilustração);
   - receita com foto grande e título por cima, linha de informações e ingredientes com bolinha de marcar;
   - aba Guia: tabela de proporções (creme 35%, nacional/importado, mesma fórmula da tabela Ganache Perfeita) + "Deu errado? Veja como consertar" (6 casos, base na Fase 2).

## Feito em 26/09/2026
1. **Conferido no celular (360 e 400 px):** Início, Monte, Receitas (cardápio e receita) e Guia. Sem rolagem lateral e sem erro de script. A barra de abas fica no rodapé em todas as telas. O "meio da tela" era efeito da captura de página inteira, que desenha elementos fixos na altura da primeira tela. No celular de verdade isso não acontece.
2. **Guia:** as proporções da tabela ("2,8 : 1") quebravam em duas linhas em 360 px. Agora ficam numa linha só.
3. **`montar.py`:** a barra do topo ia parar dentro do `<head>` do arquivo final. Agora o `<body>` começa nela. O navegador já corrigia sozinho, mas o arquivo fica certo.
4. **SKILL.md:** a seção "Visual aprovado" foi atualizada para o tema escuro.

## Falta
1. Mostrar para a Tatiana aprovar (capturas de 360 px em anexo na conversa de 26/09).
2. Pôr as fotos em `capitulo ganaches/fotos-receitas/` e rodar o `montar.py` de novo (ele avisa se passar de 5 MB).
3. Depois: item 2 da skill, revisar os textos com ela (inclusive os do "Deu errado?").
