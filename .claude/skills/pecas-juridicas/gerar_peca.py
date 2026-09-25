#!/usr/bin/env python3
"""Gera uma peça .docx no papel timbrado e na formatação do escritório Cibelly Lopes.

Uso:
    python3 gerar_peca.py entrada.txt saida.docx

Marcação do arquivo de entrada (um parágrafo por bloco, separados por linha em branco):

    @ TEXTO        endereçamento / cabeçalho do processo (negrito, justificado, sem recuo)
    = TEXTO        nome da peça ou da ação (negrito, centralizado)
    ## TEXTO       seção de 1º nível, ex.: "## I. DOS FATOS" (negrito)
    ### TEXTO      subseção, ex.: "### III.1. Da ..." (negrito e itálico)
    - TEXTO        item de pedido/lista, ex.: "- a) a concessão ..." (justificado, sem recuo)
    > TEXTO        citação longa (recuo de 4 cm, fonte 10, espaçamento simples)
    :: TEXTO       linha centralizada (local e data)
    !! TEXTO       linha centralizada em negrito (nome e OAB na assinatura)
    ---            linha em branco
    (sem prefixo)  parágrafo comum (justificado, recuo de 1ª linha 1,25 cm)

Dentro de qualquer parágrafo, **texto** fica em negrito e _texto_ em itálico.
"""
import re
import sys
import zipfile
from pathlib import Path
from xml.sax.saxutils import escape

MODELO = Path(__file__).parent / "modelo" / "timbrado.docx"

SP = '<w:spacing w:after="160" w:line="360" w:lineRule="auto"/>'


def runs(texto, negrito=False, italico=False, tam=None):
    """Converte **negrito** e _itálico_ em runs do Word."""
    out = []
    for parte in re.split(r"(\*\*.+?\*\*|(?<!\w)_.+?_(?!\w))", texto):
        if not parte:
            continue
        b, i = negrito, italico
        if parte.startswith("**") and parte.endswith("**"):
            parte, b = parte[2:-2], True
        elif parte.startswith("_") and parte.endswith("_") and len(parte) > 1:
            parte, i = parte[1:-1], True
        rpr = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial"/>'
        if b:
            rpr += "<w:b/><w:bCs/>"
        if i:
            rpr += "<w:i/><w:iCs/>"
        if tam:
            rpr += f'<w:sz w:val="{tam}"/><w:szCs w:val="{tam}"/>'
        rpr = f"<w:rPr>{rpr}</w:rPr>"
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{escape(parte)}</w:t></w:r>')
    return "".join(out)


def par(ppr, conteudo):
    return f"<w:p><w:pPr>{ppr}</w:pPr>{conteudo}</w:p>"


def bloco(txt):
    if txt == "---":
        return par('<w:spacing w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>', "")
    if txt.startswith("@ "):
        return par(SP + '<w:jc w:val="both"/>', runs(txt[2:], negrito=True))
    if txt.startswith("= "):
        return par(SP + '<w:jc w:val="center"/>', runs(txt[2:], negrito=True))
    if txt.startswith("### "):
        return par('<w:keepNext/><w:spacing w:before="140" w:after="120" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>',
                   runs(txt[4:], negrito=True, italico=True))
    if txt.startswith("## "):
        return par('<w:keepNext/><w:spacing w:before="200" w:after="140" w:line="360" w:lineRule="auto"/><w:jc w:val="both"/>',
                   runs(txt[3:], negrito=True))
    if txt.startswith("- "):
        return par(SP + '<w:jc w:val="both"/>', runs(txt[2:]))
    if txt.startswith("> "):
        return par('<w:spacing w:after="160" w:line="240" w:lineRule="auto"/><w:ind w:left="2268"/><w:jc w:val="both"/>',
                   runs(txt[2:], tam=20))
    if txt.startswith(":: "):
        return par(SP + '<w:jc w:val="center"/>', runs(txt[3:]))
    if txt.startswith("!! "):
        return par(SP + '<w:jc w:val="center"/>', runs(txt[3:], negrito=True))
    return par(SP + '<w:ind w:firstLine="708"/><w:jc w:val="both"/>', runs(txt))


def gerar(entrada, saida):
    texto = Path(entrada).read_text(encoding="utf-8")
    blocos = [" ".join(l.strip() for l in b.splitlines()) for b in re.split(r"\n\s*\n", texto) if b.strip()]
    corpo = "".join(bloco(b) for b in blocos)
    with zipfile.ZipFile(MODELO) as zin, zipfile.ZipFile(saida, "w", zipfile.ZIP_DEFLATED) as zout:
        for item in zin.infolist():
            dados = zin.read(item.filename)
            if item.filename == "word/document.xml":
                dados = dados.decode("utf-8").replace("{{CORPO}}", corpo).encode("utf-8")
            zout.writestr(item, dados)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    gerar(sys.argv[1], sys.argv[2])
    print(f"Gerado: {sys.argv[2]}")
