# Esqueleto do relatório de carga horária

> Modelo do **relatório imprimível** — preencha os `{{placeholders}}`. **Versão 1.2 (15/10/2026).**
>
> **Entregável principal:** **PDF A4** (com a identidade do projeto) + **DOCX** editável + a **planilha**
> (`.csv` / `.xlsx`). O **DOCX** sai em **fluxo natural** (o `reference-docx` padrão é *Letter* — o entregável
> de **impressão** é o **PDF A4**). Quem gera tudo: a **esteira** de `reference/esteira-documento.md`.
> **Companheiro:** o **resumo executivo** de 1–2 páginas — `assets/esqueleto-resumo-executivo.md` +
> `reference/resumo-executivo.md`.

## Capa

- Título: **Carga horária efetiva — {{Nome do Curso}}**
- Subtítulo: *estimativa por categoria de recurso*
- `{{versão}}` · `{{data}}` · responsável: `{{nome}}` · gerado com a skill `metricas-carga-horaria` v{{versão da skill}}

## 1. Apresentação

- O que é o relatório e por que existe.
- **Natureza:** **ESTIMATIVA, não medição** (+ nota: existem/não existem relatórios oficiais do Moodle).
- **Escopo:** módulos/partes que entram — e o que **ficou de fora** (com o motivo).

## 2. Método

- Fórmula, contagens × parâmetros, cenários e buckets.
- **Tabela de parâmetros** (versão resumida) com **nível de confiança** e remissão às fontes.
- **Níveis de confiança no imprimível:** **badges coloridos + rótulo textual** — `[Científico]{.cg}` ·
  `[Benchmark]{.cb}` · `[Heurística]{.ch}` — **não** emojis (🟢🟡🔴 saem **pretos** no PDF/DOCX).

## 3. Resultado — carga **obrigatória** (bucket A)

| Módulo / Parte | Textos | Imagens | Vídeos | Atividades | Fóruns | Encontros | Navegação | **Total** |
|---|---|---|---|---|---|---|---|---|
| {{...}} | | | | | | | | |

*(+ subtotais por categoria)*

## 4. Resultado — carga **opcional/complementar** (bucket B)

| Módulo | Bibliografia | Anexos (PDF) | Gravações | Sugestões | **Total** |
|---|---|---|---|---|---|
| {{...}} | | | | | |

## 5. Cenários

| Cenário | Obrigatória | Opcional | **Total** |
|---|---|---|---|
| Mínimo | | | |
| Referência | | | |
| Máximo | | | |
| **Recomendado** | | | |

*(+ nota do overhead aplicado e sua justificativa)*

## 6. Notas e limitações

- O que **não** entrou e por quê; sobreposições evitadas; itens com **"duração não localizada"**.
- **Módulos estimados por analogia** (ainda não produzidos): declarar o **módulo-modelo**, o valor
  atribuído e a **ressalva** ("estimativa de ordem de grandeza, a substituir pela medição na reexecução").
- Como **reexecutar** quando o curso mudar (Passo 6): reincorporar o que ficou fora, substituir a analogia
  pela medição, **sem rediscutir** parâmetros e decisões já tomadas.

## 7. Fontes (ABNT)

- Lista completa (ver `reference/parametros.md`).

## 8. Anexos

- Planilha de cálculo (**página a página**).
- Tabela completa de parâmetros.
- **Dicionário de dados** do inventário (o que cada coluna do CSV significa) — `reference/metodo-e-cenarios.md` §5.

## Checklist de publicação

- [ ] Totais conferem com a planilha de cálculo — e a **reconciliação com as âncoras** fecha.
- [ ] Buckets **A/B** separados.
- [ ] Cenários + **overhead** explicitados (com a decisão do cliente registrada).
- [ ] **Natureza** (estimativa) e **limitações** declaradas.
- [ ] **Módulos estimados por analogia** declarados **com ressalva**.
- [ ] **Níveis de confiança** em **badges** (não emojis) no PDF/DOCX.
- [ ] **Fontes citadas.**
- [ ] **PDF A4** (identidade do projeto) + **DOCX** editável + **XLSX** gerados pela **esteira**
      (`reference/esteira-documento.md`).
- [ ] **Resumo executivo** (≤ 2 páginas A4) gerado e conferido (`reference/resumo-executivo.md`).
- [ ] Nomes de arquivo padronizados (`Relatorio-carga-horaria-{{curso}}.{pdf,docx}`).
