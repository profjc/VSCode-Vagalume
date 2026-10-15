---
title: "Carga horária efetiva — {{Nome do Curso}}"
subtitle: "Resumo executivo · estimativa por categoria de recurso"
author: "{{responsável}}"
date: "{{data}}"
lang: pt-BR
---

> **Modelo do RESUMO EXECUTIVO** (PDF A4 de **1–2 páginas** + DOCX) — preencha os `{{placeholders}}`.
> **Versão 1.2 (15/10/2026).** Padrão e técnica de fechar em N páginas: `reference/resumo-executivo.md`.
> Gerado pela esteira (`reference/esteira-documento.md`) a partir de um **espelho de cabeçalho compacto**
> (mesma identidade do relatório, **sem** a capa inteira).

> **{{o número principal em uma frase.}}** *(ex.: a carga obrigatória estimada é de X (referência) — ou Y no
> recomendado, que acrescenta 10% de folga; a opcional soma Z.)*

# Os números

| Cenário | Obrigatória (A) | Opcional (B) | **Total (A+B)** |
|---|---|---|---|
| Mínimo | {{…}} | {{…}} | {{…}} |
| **Referência** | **{{…}}** | {{…}} | **{{…}}** |
| Máximo | {{…}} | {{…}} | {{…}} |
| **Recomendado** | **{{…}}** | {{…}} | **{{…}}** |

# O que compõe a carga

**Obrigatória (A):** os itens mais pesados (com tempos) — ex.: fóruns, encontros síncronos, leitura,
vídeos, atividades H5P, navegação, imagens.

**Opcional/complementar (B):** bibliografia, anexos (PDF), gravações.

# Natureza do número

É uma **estimativa**, não uma medição. As **quantidades** ({{…}} páginas, {{…}} palavras, {{…}} imagens,
{{…}} atividades, {{…}} fóruns) são **exatas e rastreáveis** ao arquivo de origem; os **tempos** são
**parâmetros** com fonte citada, aplicados **página a página**.

# Onde está a carga (por módulo) {.quebra-pagina}

| Módulo | Páginas | Carga obrigatória (ref.) |
|---|---|---|
| {{Módulo}} | {{n}} | {{…}} |
| **Total (referência)** | **{{n}}** | **{{…}}** |

![Carga horária obrigatória por módulo, nos três cenários](assets/images/relatorios/grafico-modulos.png)

# Recomendação

Adotar o **cenário recomendado** ({{…}}) como referência de comunicação — parte da referência e acrescenta
**{{overhead}}%** de overhead; é o número mais realista e o mais defensável, porque **cada parcela pode ser
auditada**. A **carga opcional** ({{…}}) é comunicada **à parte**, como aprofundamento.

# Limitações

- **Módulo {{X}}** (não produzido): estimado **por analogia com o módulo {{Y}}** ({{…}}), **com ressalva** —
  substituído pela **medição** na reexecução.
- **{{Bloco}}** fora do cálculo por falta de quantidades — reincorporado na reexecução.
- **{{Item}}** computado como efetivo por decisão da coordenação.

<!--
TÉCNICA (ver reference/resumo-executivo.md):
- a classe {.quebra-pagina} quebra a página SÓ no PDF; o DOCX flui natural (decisão do mestre).
- alvo: ≤ 2 páginas A4 — medir com `pdfinfo` e ajustar a densidade (título, tabelas, largura do gráfico, margens).
- níveis de confiança no imprimível: badges (não emojis).
-->
