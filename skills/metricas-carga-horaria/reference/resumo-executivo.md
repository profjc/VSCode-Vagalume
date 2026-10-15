# Resumo executivo de 1–2 páginas (Passo 5.2)

> O **segundo entregável** do Passo 5: um resumo **curto** (1–2 páginas A4) para a coordenação, com a
> **mesma identidade** do relatório, mas **cabeçalho compacto** (sem a capa inteira).
> **Versão 1.2 (15/10/2026)** — projeto de origem: Vaga Lume (Ciclo 6).

## 1 — Quando e por quê

O relatório completo (10+ páginas) é para **auditar**; o resumo executivo é para **decidir e comunicar**.
Regra: quem lê o resumo tem de sair sabendo **o número principal**, **o recomendado**, **o que o compõe** e
**as ressalvas** — sem abrir o relatório.

## 2 — Estrutura (ordem comprovada)

1. **Cabeçalho compacto** — `kicker` (ex.: “Resumo executivo · Relatório de Carga Horária”) + **logos** +
   título + curso + `v<versão> · <data>`. **Sem capa.**
2. **Parágrafo de abertura** — o número principal em **1 frase** (obrigatória + recomendada + opcional).
3. **Os números** — tabela de **cenários** (mín · ref · máx · recomendado × A · B · A+B).
4. **O que compõe a carga** — os 2–3 itens mais pesados (com tempos) por bucket.
5. **Natureza do número** — “estimativa, não medição” + as quantidades exatas + rastreabilidade.
6. **Onde está a carga (por módulo)** — tabela curta + **1 gráfico** (o de módulos).
7. **Recomendação** — adotar o **recomendado**; a opcional comunicada **à parte**.
8. **Limitações** — o que ficou **estimado por analogia** e o que ficou **fora** (reincorporado na reexecução).

## 3 — Técnica: fechar em N páginas (1–2 é o alvo)

O alvo é **não passar de 2 páginas**. O laço é: **medir → ver a borda → ajustar a densidade**.

```bash
pdfinfo <arquivo>.pdf | awk '/^Pages:/{print $2}'      # 1) contagem de páginas
pdftoppm -r 100 -png <arquivo>.pdf /tmp/pg             # 2) renderiza para inspecionar
# 3) nas imagens: medir o bbox de tinta da última página e comparar com o LIMITE ÚTIL
#    A4 a 100 dpi = 1169 px de altura; margem inferior 18 mm ≈ 71 px  ⇒  limite útil ≈ y 1099
```

- Se a última página **extrapola** o limite útil, **aumente a densidade**; se sobra pouca coisa na última
  página, **reduza** a densidade para **fechar em N** páginas.
- **Botões de densidade** (na ordem em que se mexe): tamanho do **título**; corpo das **tabelas**
  (`font-size`); **largura do gráfico** (`max-width`); **margens**; espaçamento de blocos.
- *Precedente: o resumo do projeto de origem saiu de **4 → 3 → 2 páginas** assim.*
- ⚠️ **DOCX não tem o mesmo fechamento**: o `reference-docx` sai em Letter e o DOCX decide como **fluxo
  natural** (ver `reference/esteira-documento.md` §4). O alvo de páginas vale para o **PDF**.

## 4 — O que NÃO fazer

- **Não** repetir o relatório inteiro “resumido” — é um resumo, não uma versão curta.
- **Não** usar emojis 🟢🟡🔴 (saem **pretos**) — usar os **badges** onde o nível de confiança aparecer.
- **Não** apresentar a analogia (módulo estimado) sem a **ressalva** ao lado.
- **Não** omitir a **carga opcional** — ela é comunicada **à parte**, nunca somada à obrigatória no número principal.

## 5 — Checklist do resumo executivo

- [ ] O **número principal** (obrigatória) e o **recomendado** aparecem na **primeira tela**.
- [ ] Tabela de **cenários** + **composição** + **por módulo** (com **1 gráfico**).
- [ ] **Natureza** (estimativa × medição) e **limitações** (analogia/fora) declaradas.
- [ ] **PDF A4 em ≤ 2 páginas** (medido por `pdfinfo`) + **DOCX** gerado pela esteira.
- [ ] Mesma **identidade** do relatório (logos/v.+ data) no rodapé.
