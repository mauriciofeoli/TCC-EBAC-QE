"""Lê o texto do PDF renderizado (pdftotext, páginas separadas por \\f) e grava paginas.json para o sumário.

Uso: python docs/gerador/calcular_paginas.py <arquivo.txt>
"""
import json
import os
import re
import sys

from gerar_tcc import SUMARIO

texto = open(sys.argv[1], encoding='utf-8').read()
paginas_pdf = texto.split('\f')
resultado = {}
pagina_sumario = next(i for i, p in enumerate(paginas_pdf, start=1) if re.search(r'^\s*2\.\s*SUMÁRIO\s*$', p, re.M))
for num, nome in SUMARIO:
    padrao = re.compile(r'^\s*' + re.escape(num) + r'\s*' + re.escape(nome.strip()) + r'\s*$', re.M | re.I)
    for i, pagina in enumerate(paginas_pdf, start=1):
        if i == pagina_sumario and num != '2.':
            continue  # as entradas do próprio sumário não contam
        if padrao.search(pagina):
            resultado[num] = i
            break
saida = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'paginas.json')
json.dump(resultado, open(saida, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(resultado)
