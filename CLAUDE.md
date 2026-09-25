# Cibelly Lopes Advocacia

Este repositório contém o site do escritório (cibellylopes.adv.br, publicado no Azure Static Web Apps) e o padrão de trabalho da Dra. Cibelly Maria Lopes da Silva (OAB/SP 471.453) para redigir documentos jurídicos.

## Documentos jurídicos
Para qualquer peça, petição, manifestação, recurso, procuração, declaração ou contrato, **siga a skill `.claude/skills/pecas-juridicas/SKILL.md`**. Ela define a estrutura, o estilo de redação, os dados fixos e a formatação no papel timbrado. O `.docx` final é gerado com `gerar_peca.py`.

Os documentos dos clientes ficam no Google Drive (uma pasta por cliente). Nunca coloque dados de clientes neste repositório: ele é publicado como site.

## Site
HTML estático (`index.html`, `admin/`, `assets/`). Identidade visual: azul #1f364e, dourado #b49265, títulos em Arsenal e texto em Mona Sans.
