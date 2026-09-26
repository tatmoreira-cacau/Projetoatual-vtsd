# Continuar a calculadora de ganache

Use a skill `calculadora-ganache` (`.claude/skills/calculadora-ganache/SKILL.md`).
A seção **ESTADO ATUAL (25/09/2026)** diz o que já está pronto e o que falta, na ordem.

Edite só `capitulo ganaches/fontes/calculadora-src.html` e gere as versões finais com:

    pip install pillow playwright
    python "capitulo ganaches/fontes/receitas-md.py"
    python "capitulo ganaches/fontes/montar.py"
    python "capitulo ganaches/fontes/testar.py"

- Branch: `main-p86j61` · PR #1 (rascunho).
- Prévia para a Tatiana (artifact privado): https://claude.ai/artifact/HFEk7pv8KywwcEAN8e8124
  Depois de mudar a calculadora, republique `capitulo ganaches/calculadora-ganache.html` nesse mesmo link.

## Próximo passo
Esperar a Tatiana aprovar a calculadora no celular. Depois, revisar os textos com ela (inclusive os 6 consertos do "Deu errado?").

Regras: não mudar números sem ela pedir; voz de confeiteira; responder em português simples, com imagens das telas. Ela usa celular e é iniciante em tecnologia.
