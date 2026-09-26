# Gera as versões finais (para a Hotmart) a partir dos arquivos-fonte desta pasta.
# Uso: python montar.py            (usa as fotos de ../fotos-receitas)
#      python montar.py OUTRA_PASTA (usa as fotos de outra pasta, para teste)
# - acrescenta o cabeçalho HTML com charset utf-8
# - troca os acentos por códigos (&#NNN; no HTML, escapes unicode no JS e no CSS), porque a Hotmart entrega o arquivo sem charset
# - diminui as fotos (lado maior 800 px, JPEG 75%) e embute dentro do HTML, porque a Hotmart hospeda um arquivo só
import base64, io, json, os, re, sys
AQUI = os.path.dirname(os.path.abspath(__file__))
SAIDA = os.path.dirname(AQUI)  # pasta "capitulo ganaches"
FOTOS_DIR = sys.argv[1] if len(sys.argv) > 1 else os.path.join(SAIDA, 'fotos-receitas')
PARES = [('calculadora-src.html', 'calculadora-ganache.html'), ('ganache-perfeita-src.html', 'ganache-perfeita.html')]
BS = chr(92)
LADO, QUALIDADE, LIMITE_MB = 800, 75, 5.0
EXTS = ('.jpg', '.jpeg', '.png', '.webp')

def esc_html(t): return ''.join(c if ord(c) < 128 else '&#%d;' % ord(c) for c in t)
def esc_css(t):
    # dentro do <style>, &#NNN; não funciona: usa o escape do CSS (\203a )
    return ''.join(c if ord(c) < 128 else BS + '%x ' % ord(c) for c in t)
def esc_js(t):
    # emojis (acima de FFFF) viram par substituto: 💧
    return ''.join(c if ord(c) < 128 else ''.join(BS + 'u%04x' % u for u in u16(c)) for c in t)
def u16(c):
    b = c.encode('utf-16-le')
    return [b[i] | (b[i + 1] << 8) for i in range(0, len(b), 2)]

def ler_fotos():
    fotos = {}
    if not os.path.isdir(FOTOS_DIR): return fotos
    try:
        from PIL import Image, ImageOps
    except ImportError:
        print('AVISO: Pillow não instalado (pip install pillow). Fotos não embutidas.')
        return fotos
    for nome in sorted(os.listdir(FOTOS_DIR)):
        base, ext = os.path.splitext(nome)
        if ext.lower() not in EXTS: continue
        im = ImageOps.exif_transpose(Image.open(os.path.join(FOTOS_DIR, nome)))
        if im.mode in ('RGBA', 'LA', 'P'):
            im = im.convert('RGBA')
            fundo = Image.new('RGB', im.size, (248, 245, 240))  # creme do ebook
            fundo.paste(im, mask=im.split()[-1])
            im = fundo
        im = im.convert('RGB')
        im.thumbnail((LADO, LADO), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'JPEG', quality=QUALIDADE, optimize=True, progressive=True)
        fotos[base.lower()] = 'data:image/jpeg;base64,' + base64.b64encode(buf.getvalue()).decode('ascii')
        print('  foto %-14s %4dx%-4d %4d KB' % (nome, im.size[0], im.size[1], len(buf.getvalue()) // 1024))
    return fotos

CAB = ('<!DOCTYPE html>\n<html lang="pt-BR">\n<head>\n<meta charset="utf-8">\n'
       '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
       '<meta name="theme-color" content="#5A3526">\n'
       '<style>body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n')

fotos = ler_fotos()
print('fotos embutidas:', len(fotos), '(' + (', '.join(sorted(fotos)) or 'nenhuma') + ')')

for src, dst in PARES:
    s = io.open(os.path.join(AQUI, src), encoding='utf-8').read()
    if 'var FOTOS = {};' in s:
        s = s.replace('var FOTOS = {};', 'var FOTOS = ' + json.dumps(fotos, separators=(',', ':')) + ';')
    partes = re.split(r'(<script>.*?</script>|<style>.*?</style>)', s, flags=re.S)
    corpo = ''.join(esc_js(p) if p.startswith('<script>') else esc_css(p) if p.startswith('<style>') else esc_html(p) for p in partes)
    i = corpo.index('<div class="wrap">')
    out = CAB + corpo[:i] + '</head>\n<body>\n' + corpo[i:] + '\n</body>\n</html>\n'
    io.open(os.path.join(SAIDA, dst), 'w', encoding='utf-8', newline='\n').write(out)
    mb = len(out.encode('utf-8')) / 1048576
    print('gerado: %s (%.2f MB)' % (dst, mb) + ('  <-- ACIMA DE %.0f MB: use fotos menores' % LIMITE_MB if mb > LIMITE_MB else ''))
