---
name: pecas-juridicas
description: Padrão de redação e formatação das peças e documentos do escritório Cibelly Lopes Advocacia (Iguape/SP). Use SEMPRE que for redigir, revisar ou formatar petição inicial, contestação, réplica, manifestação, recurso, defesa administrativa, renúncia, reclamação trabalhista, ação de família, procuração, declaração de hipossuficiência, contrato de honorários ou qualquer documento jurídico para a Dra. Cibelly.
---

# Peças jurídicas no padrão Cibelly Lopes

Este guia foi extraído das peças reais da Dra. Cibelly (inicial consumerista contra banco, reclamação trabalhista, ação de alimentos com guarda, réplica contra a Fazenda, manifestação sobre laudo pericial, defesa de autuação de trânsito, renúncia de mandato, procuração, declaração de hipossuficiência e contrato de honorários). Siga-o à risca: o objetivo é que a peça saia pronta para assinar, sem que ela precise reescrever nada.

## 1. Fluxo de trabalho

1. **Leia os documentos do caso primeiro.** Ela organiza tudo no Google Drive, uma pasta por cliente (documentos pessoais, comprovante de endereço, extratos, contratos, laudos, prints de WhatsApp, decisões). Os fatos saem desses documentos, com datas, valores, números de contrato, fls. e Id. exatos. Nunca invente fato, número ou data.
2. **Dado faltante** entra como `[PREENCHER: descrição]`, e você avisa no fim quais campos ficaram em aberto.
3. **Jurisprudência:** cite só o que tem certeza (súmula, tema repetitivo, número do REsp/RE, tese). Se não tiver certeza, marque `[VERIFICAR]`. Nunca invente ementa nem número de processo.
4. **Escreva o texto** no formato de marcação do gerador (seção 6) e gere o `.docx` no timbrado:
   `python3 .claude/skills/pecas-juridicas/gerar_peca.py peca.txt "nome da peca.docx"`
5. **PDF:** gere uma prévia com `soffice --headless --convert-to pdf "nome da peca.docx"` (se o Writer não estiver instalado: `apt-get install -y libreoffice-writer`) e confira o layout. Sem a fonte Arial no ambiente, a prévia sai com outra fonte; o PDF de protocolo deve ser exportado pelo Word, onde a Arial aparece corretamente.
6. **Nome do arquivo:** minúsculas, sem acento, descritivo e curto, como ela faz: `inicial.docx`, `replica.docx`, `manifestacao laudo.docx`, `pedido renuncia.docx`, `recurso.docx`, `procuracao.docx`, `declaracao de hipossuficiencia.docx`, `contrato honorarios.docx`.
7. Se ela pedir, suba os arquivos na pasta do cliente no Drive.

## 2. Formatação (idêntica ao modelo dela)

O gerador já aplica tudo isto; a lista serve para conferência:

- Papel A4 com o **timbrado** (logo CIBELLY LOPES no topo, monograma CL em marca d'água, rodapé com telefone, Instagram, e-mail e endereço). Arquivo: `modelo/timbrado.docx`.
- Margens: superior 6 cm, inferior 3 cm, esquerda 2 cm, direita 1,3 cm. Número de página no rodapé.
- **Arial 12**, espaçamento **1,5**, 8 pt depois de cada parágrafo, texto **justificado**.
- Parágrafo comum com **recuo de 1ª linha de 1,25 cm**.
- Endereçamento e dados do processo: **negrito**, justificado, sem recuo.
- Nome da peça ou da ação: **NEGRITO, CAIXA ALTA, CENTRALIZADO**, em parágrafo próprio.
- Seções: `I. DOS FATOS`, em **negrito e caixa alta**, com algarismo romano e ponto.
- Subseções: `III.1. Da urgência médica comprovada`, em ***negrito e itálico***, só a inicial maiúscula.
- Itens dos pedidos: `a)`, `b)`, `c)`, sem recuo.
- Local e data centralizados; nome da advogada em negrito e caixa alta, centralizado; OAB na linha de baixo.

## 3. Estrutura das peças

### 3.1 Endereçamento
- Juízo desconhecido ou gênero não confirmado: `EXCELENTÍSSIMO(A) SENHOR(A) DOUTOR(A) JUIZ(A) DE DIREITO DA VARA CÍVEL DA COMARCA DE IGUAPE/SP`.
- Gênero conhecido: `EXCELENTÍSSIMA SENHORA DOUTORA JUÍZA DE DIREITO DA 2ª VARA CÍVEL DA COMARCA DE ...`.
- Juizado: `... JUIZ(A) DE DIREITO DO JUIZADO ESPECIAL CÍVEL DA COMARCA DE ...`.
- Trabalho: `... JUIZ(A) DO TRABALHO DA VARA DO TRABALHO DE REGISTRO/SP`.
- Esfera administrativa: `ILUSTRÍSSIMO(A) SENHOR(A) AUTORIDADE DE TRÂNSITO DO MUNICÍPIO DE ...`, seguido de um bloco de identificação (órgão, auto de infração, placa, código, datas).

Destaques abaixo do endereçamento, quando cabem, em negrito: `PRIORIDADE DE TRAMITAÇÃO: PESSOA IDOSA` e, na linha seguinte, `(art. 1.048, I, do CPC e art. 71 da Lei nº 10.741/2003)`.

### 3.2 Peça intermediária (manifestação, réplica, renúncia, pedidos em geral)
```
Processo nº 0000000-00.0000.0.00.0000
Classe do processo
Exequente/Autor: ...            (quando ajuda a identificar)
Executado/Réu: ...

FULANO DE TAL, já qualificado nos autos da [ação] em epígrafe, que move em face de [PARTE], vem, respeitosamente, à presença de Vossa Excelência, por sua advogada que esta subscreve, apresentar

NOME DA PEÇA EM CAIXA ALTA

pelas razões de fato e de direito a seguir expostas.
```
A primeira seção costuma ser uma síntese: `I. BREVE SÍNTESE DO ANDAMENTO PROCESSUAL` ou `I. DA SÍNTESE DO LAUDO PERICIAL`, com fls./Id. de cada ato.

### 3.3 Petição inicial
Qualificação completa: **NOME EM CAIXA ALTA**, nacionalidade, estado civil, profissão, RG, CPF, endereço completo com CEP. Depois:

> vem, respeitosamente, à presença de Vossa Excelência, por intermédio de sua advogada (procuração anexa), com fundamento nos arts. ... do ... , propor a presente
>
> **AÇÃO ... C/C ... , COM PEDIDO DE TUTELA DE URGÊNCIA**
>
> em face de **RÉU**, pessoa jurídica de direito privado, inscrita no CNPJ sob o nº ..., com sede na ..., pelos fatos e fundamentos a seguir expostos.

Ordem das seções (use as que couberem):
1. `DA GRATUIDADE DA JUSTIÇA` (arts. 98 e 99, § 3º, do CPC; na trabalhista, art. 790, §§ 3º e 4º, da CLT). Ela sempre concretiza: renda, benefício, NB, triagem Defensoria/OAB e "declaração de hipossuficiência anexa".
2. `DA PRIORIDADE DE TRAMITAÇÃO` (idoso: data de nascimento e idade).
3. `DA OPÇÃO PELO JUIZADO ESPECIAL CÍVEL` / competência, quando for o caso.
4. `DOS FATOS` (na trabalhista, antes vem `DA SÍNTESE CONTRATUAL`: admissão, função, jornada, salário e forma de rescisão).
5. `DO DIREITO`, em subseções `V.1.`, `V.2.` ..., cada uma com uma tese.
6. `DA TUTELA DE URGÊNCIA`: probabilidade do direito em lista `(i) ... (ii) ...`, perigo de dano, reversibilidade (art. 300, § 3º, do CPC) e pedidos liminares `a)`, `b)`, `c)`, com multa e prazo (ex.: 48 horas, R$ 500,00 por desconto) e pedido subsidiário.
7. `DOS PEDIDOS`.
8. Provas, valor da causa e fecho.

### 3.4 Pedidos
- Abertura: `Diante do exposto, requer:` / `Ante o exposto, requer o recorrente:` / `Diante de todo o exposto, requer a reclamante, com a indicação de valor a cada pedido nos termos do art. 840, §1º, da CLT:`.
- Itens `a)`, `b)`, `c)`..., começando em minúscula e terminando em `;` (o último em `.`).
- Ordem usual: gratuidade → prioridade → tutela → citação/audiência → inversão do ônus da prova → **TOTAL PROCEDÊNCIA** (em caixa alta), com cada condenação discriminada → pedidos **subsidiários** ("subsidiariamente, caso ...", "mais subsidiariamente ainda") → exibição de documentos (art. 396 e seguintes / art. 400 do CPC) → intimações em nome da(s) advogada(s).
- Na condenação em dinheiro, ela indica correção e juros com súmulas: Súmulas 43 e 54 do STJ (danos materiais), Súmula 362 do STJ (correção do dano moral desde o arbitramento).
- **Trabalhista:** cada pedido tem valor líquido estimado por extenso, "sem prejuízo de apuração exata em liquidação"; pedido sem valor leva "(pedido de natureza processual, sem conteúdo econômico direto)" ou "(pedido declaratório, sem conteúdo econômico direto)"; honorários de sucumbência de 15% (art. 791-A da CLT); o valor da causa é a soma dos pedidos.
- Pedido de intimações:
  `que todas as intimações sejam feitas em nome da advogada CIBELLY MARIA LOPES DA SILVA, OAB/SP nº 471.453, com endereço profissional na Rua Latif Corrêa, nº 29, Centro, Iguape/SP, CEP 11920-000.`

### 3.5 Fecho
```
Protesta provar o alegado por todos os meios de prova em direito admitidos, especialmente [prova documental / pericial / depoimento pessoal ...].

Dá-se à causa o valor de R$ 17.303,90 (dezessete mil, trezentos e três reais e noventa centavos).

Termos em que,
pede deferimento.

Iguape/SP, 23 de setembro de 2026.

CIBELLY MARIA LOPES DA SILVA
OAB/SP nº 471.453
```
- Variações que ela usa: "Nestes termos, / Pede deferimento." e "Termos em que, pede deferimento." A cidade é a do escritório que assina (Iguape/SP, ou Itupeva/SP quando atua com a Dra. Larissa).
- Na defesa administrativa, feche com `ROL DE DOCUMENTOS ANEXOS` numerado em romanos (I. Instrumento de procuração; II. ...).

## 4. Estilo de redação

- **Tom:** técnico, firme e respeitoso. Nada de adjetivação exagerada nem latinismo gratuito. Expressões recorrentes dela: "vem, respeitosamente, à presença de Vossa Excelência", "com a devida vênia", "o que se admite apenas por argumentação" / "por amor ao debate", "A impugnação não merece prosperar.", "Diante desse quadro", "Não é, nem de longe, o caso".
- **Fatos:** ordem cronológica, datas em `dd/mm/aaaa` (ou por extenso em peça administrativa), valores `R$ 2.380,42`. Os valores principais vêm também por extenso: `R$ 10.000,00 (dez mil reais)`. Cada fato aponta sua prova: "conforme extrato anexo", "fls. 39/40", "Id. 57f59a6".
- **Irregularidades e argumentos em lista** com rótulo: `a) Refinanciamento não solicitado: o instrumento ...;`. Para encadear teses, ela usa "Em primeiro lugar, ... Em segundo lugar, ... Em terceiro lugar, ... Por fim, ...".
- **Frase curta de impacto** depois do raciocínio longo. Exemplos dela: "Se o próprio Estado, por meio de seu agente, orientou o condutor a não realizar o teste, não pode o Estado, em seguida, puni-lo precisamente por não tê-lo realizado." / "Não se trata aqui de especular sobre o que o agente pensou, mas de ler, objetivamente, o que o agente fez."
- **Fundamentação:** artigo exato e diploma por extenso na 1ª menção, sigla depois: "art. 6º, VIII, do Código de Defesa do Consumidor" → "art. 6º, VIII, do CDC". Formatos: `art. 300, § 3º, do CPC`, `arts. 98 e 99`, `Lei nº 9.099/95`, `Lei nº 10.741/2003 (Estatuto da Pessoa Idosa)`.
- **Precedentes** citados no corpo do parágrafo, com a tese entre aspas e a identificação completa: Súmula 297 do STJ, Tema Repetitivo 1.061 (REsp 1.846.649/MA), EAREsp 676.608/RS, Súmula 331, IV e V, do TST, RE 760.931 (Tema 246). Ela **não** usa blocos longos de ementa; transcreve só a tese, entre aspas.
- **Denominação das partes**, com inicial maiúscula e a mesma forma do começo ao fim: Autor/Réu (cível), Requerente/Requerido (família), Reclamante/Reclamada ou 1ª Reclamada (trabalhista), recorrente (administrativo), Exequente/Executado. Ela se refere a si mesma como "a subscritora".
- **Sempre há pedido subsidiário** quando a tese principal pode cair: limitar descontos, revisar juros, afastar só a suspensão, etc.
- **Boa-fé processual** como estratégia: ela antecipa compensação ("o Autor desde já concorda com a compensação ...") e reconhece o que é incontroverso, o que dá credibilidade à peça.
- Na peça trabalhista, ela mostra o cálculo das estimativas no texto (divisor 220, dias úteis, adicional de 50%, reflexo em DSR).

## 5. Dados fixos

**Advogada:** CIBELLY MARIA LOPES DA SILVA, brasileira, em união estável, advogada, OAB/SP nº 471.453.
Endereço profissional: Rua Latif Corrêa, nº 29, Centro, Iguape/SP, CEP 11920-000.
E-mail processual: cibellylopes@adv.oabsp.org.br · Telefone/WhatsApp: (11) 96842-1883.

**Atuação conjunta** (inclua só quando ela indicar):
- Dr. LUCAS RIYODI HIOKI CARNEIRO, OAB/SP nº 399.818. Rua Capitão Dias, 600, Piso Superior, Vila Garcez, Iguape/SP, CEP 11920-000. Nesse caso use "por intermédio de seus advogados".
- Dra. LARISSA LOURENÇON DA SILVA, OAB/SP nº 537.355. Avenida Itália, nº 566, Jardim São Vicente, Itupeva/SP, CEP 13295-114. Nesse caso use "por intermédio de suas advogadas".
Com dois advogados, as duas assinaturas vêm uma embaixo da outra.

## 6. Marcação do gerador (`gerar_peca.py`)

Escreva um bloco por parágrafo, com uma linha em branco entre os blocos:

| Prefixo | Uso |
|---|---|
| `@ ` | endereçamento, nº do processo, classe e partes (negrito) |
| `= ` | nome da peça ou da ação (negrito, centralizado) |
| `## ` | seção `I. DOS FATOS` |
| `### ` | subseção `III.1. Da ...` |
| `- ` | item de pedido `a) ...` |
| `> ` | citação longa, raramente usada |
| `:: ` | linha centralizada (local e data) |
| `!! ` | linha centralizada em negrito (nome e OAB) |
| `---` | linha em branco |
| (nada) | parágrafo comum com recuo |

`**texto**` sai em negrito e `_texto_` em itálico. Use negrito no corpo para o nome das partes na qualificação (ex.: `**CICERO ...**, brasileiro, ...`).

Exemplo mínimo em `exemplos/exemplo_manifestacao.txt`.

## 7. Documentos do kit de atendimento

Todos no timbrado. Veja os modelos em `exemplos/kit_atendimento.md`:
- **Procuração** `PROCURAÇÃO AD JUDICIA ET EXTRA`, com OUTORGANTE (qualificação), OUTORGADA (dados fixos) e PODERES (cláusula ad judicia et extra e poderes especiais: receber citação, confessar, reconhecer a procedência do pedido, desistir, renunciar, transigir, firmar acordos, receber e dar quitação, substabelecer com ou sem reservas). Na procuração com poderes limitados, o objeto vem restrito ("exclusivamente para ...") e há cláusula de extinção automática com o cumprimento do objeto.
- **Declaração de hipossuficiência**: qualificação + "declara para os devidos fins que neste momento está impossibilitada de arcar com as custas processuais sem prejuízo do seu próprio sustento e de sua família." + local, data e linha de assinatura.
- **Contrato de honorários**: `INSTRUMENTO PARTICULAR DE PRESTAÇÃO DE SERVIÇOS E HONORÁRIOS ADVOCATÍCIOS`, com cláusulas numeradas (objeto; honorários, com 30% do proveito na trabalhista, inclusive FGTS, seguro-desemprego e multas; sucumbência da advogada, arts. 22 e 23 da Lei 8.906/94; destaque do art. 22, § 4º; INPC, multa de 20% e juros de 1% ao mês; despesas à parte; vencimento antecipado; multa de 1 salário mínimo por desistência; retenção; obrigações das partes; foro de Iguape/SP). **Os dados bancários são sempre conferidos com ela; não os copie de contratos antigos.**
