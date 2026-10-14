# Esqueleto do relatório de carga horária

> Modelo do **relatório imprimível** (PDF A4 + DOCX) — preencha os `{{placeholders}}`.
> **Versão 1.1.1 (14/10/2026).**

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
- Como **reexecutar** quando o curso mudar.

## 7. Fontes (ABNT)

- Lista completa (ver `reference/parametros.md`).

## 8. Anexos

- Planilha de cálculo (**página a página**).
- Tabela completa de parâmetros.
- **Dicionário de dados** do inventário (o que cada coluna do CSV significa) — `reference/metodo-e-cenarios.md` §5.

## Checklist de publicação

- [ ] Totais conferem com a planilha de cálculo.
- [ ] Buckets **A/B** separados.
- [ ] Cenários + **overhead** explicitados (com a decisão do cliente registrada).
- [ ] **Natureza** (estimativa) e **limitações** declaradas.
- [ ] **Fontes citadas.**
- [ ] **PDF A4** (identidade do projeto) + **DOCX** editável gerados.
- [ ] Nomes de arquivo padronizados (`Relatorio-carga-horaria-{{curso}}.{pdf,docx}`).
