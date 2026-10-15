# 🚨 LEIA PRIMEIRO — usar esta skill em outro projeto

> **O que é:** o *onboarding* da skill `metricas-carga-horaria`. O `SKILL.md` é o **método**; este
> arquivo é o que **você lê antes de começar** num projeto novo, para decidir se vai **ADAPTAR** ou
> **GENERALIZAR**.
> **Versão 1.2.1 (15/10/2026)** — projeto de origem: Vaga Lume.

## 1 — O que foi doado (e o que ainda NÃO é genérico)

| Artefato | Estado |
|---|---|
| `reference/` (método, parâmetros, armadilhas…) | ✅ **genérico** — escrito para qualquer curso Moodle |
| `assets/inventario-recursos.py` | ✅ **já generalizado** — CLI (`--root`/`--config`/`--csv`/`--md`) + config JSON |
| `assets/calculo-carga-horaria.py` | ⚠️ **INSTÂNCIA** — parâmetros e ajustes finos **no código**; **sem CLI** (caminhos fixos) |
| `assets/esteira/*.py` e `*.sh` | ⚠️ **INSTÂNCIA** — produto, cores, logos e caminhos do projeto de origem |
| `assets/esteira/espelho-*.html` | ⚠️ **IDENTIDADE** — marca/CSS; **sempre manual** ao adaptar |
| `assets/*.json` + os 2 esqueletos | ✅ exemplos/documentos — ponto de partida |

> **Origem da doação:** projeto **Vaga Lume** (Moodle 4.5). Escopo **A** — doado “como está”, para
> adaptação no destino; a generalização dos scripts ficou **de propósito** no roadmap.

## 2 — A decisão: ADAPTAR ou GENERALIZAR?

- **ADAPTAR** = trocar os **valores** da instância (rápido; os scripts ficam como estão).
- **GENERALIZAR** = mover o que é do projeto para **config JSON / CLI** (mexe no código).

| Situação | Escolha | Por quê |
|---|---|---|
| **Sem 2º projeto/curso à vista** | **ADAPTAR** | o *schema* de um config seria **inventado**, não derivado (risco de over-engineering) |
| **2º projeto/exportação à vista** | **GENERALIZAR PRIMEIRO** — naquele front, **antes** de adaptar o curso novo | aí o *schema* é **derivado** do caso real e o **oráculo** (§4) ainda prova byte a byte |
| **Só quer coerência interna** | **Meio-termo:** dar ao cálculo a **mesma CLI** do inventário (`--root`/`--config`/`--csv`/`--md`) e mover **só** parâmetros + ajustes para o JSON | uniformiza a validação de paridade nos dois scripts |
| **Quer só não esquecer** | Marcar no roadmap/issue | sem código |

> ⚠️ **Não generalize “por precaução”.** O custo de exportar **não** está no código — está no **dado**
> do curso (ajustes finos, `padroes`/`modulos`) e na **identidade** (espelho/logos), que continuam
> **manuais** de qualquer forma.

## 3 — Checklist dos PONTOS DE INSTÂNCIA (o trabalho real de adaptar)

**3.1 `inventario-recursos.py` — via `--config` (já pronto)**
- `modulos` (pasta → sigla) · `padroes` (**falha silenciosa nº 1**) · `ignorar` · `ref_paginas` · `duracoes` · `paths`.
- Ao terminar, confira na saída a tabela **“Distribuição das páginas por tipo”**.

**3.2 `calculo-carga-horaria.py` — no código, hoje**
- **Paths (4):** `INV_CSV` · `PDF_DIR` · `OUT_CSV` · `OUT_MD`.
- **Parâmetros (10):** `PPM` · `ESTUDO` · `IMG_FATOR` · `VID_FATOR` · `H5P_FATOR` · `FORUM` · `BIBLIO` · `NAV` · `ENCONTRO_S` · `OVERHEAD`.
- **Dicionários (5):** `IMG_S` · `BIBLIO_ITENS` · `EXT_PALAVRAS` · `H5P_TIPO` · `H5P_PAR`.
- **Escalares (5):** `ENC_ENCONTROS` · `ENC_GRAVACOES_S` · `ENC_GRAVACAO_3_S` · `NAV_LABELS` · `NAV_FRONTPAGE`.
- Valores de referência da instância: `assets/exemplo-calc-vagalume.json`.

**3.3 Esteira (`assets/esteira/`)**
- Produto/nome de saída · cores · **logos** · fonte · título do curso · responsável · caminhos.
- Detalhes: `assets/esteira/LEIA-ME.md` + `reference/esteira-documento.md`.

**3.4 Espelhos (identidade)**
- `espelho-relatorio.html` e `espelho-resumo-executivo.html` — logo, cores, `@page`, **badges**.
- **Sempre manual** — config não cobre CSS/identidade.

## 4 — O ORÁCULO (não expira) — como refatorar com segurança

Os artefatos oficiais do projeto de origem ficam **no repositório** e servem de **gabarito byte a
byte**, em **qualquer momento futuro**:

| Passo | Como rodar o script doado | Comparação |
|---|---|---|
| **1 — inventário** | `python3 <skill>/assets/inventario-recursos.py --root . --config <config>.json --csv /tmp/check.csv --md /tmp/check.md` | `diff /tmp/check.csv docs/relatorios/carga-horaria/inventario-recursos.csv` |
| **4 — cálculo** | rodar `calculo-carga-horaria.py` numa **cópia** do projeto (ele **não tem CLI**) | `diff` do `calculo-carga-horaria.csv` **e** do `.md` oficiais |

> **Regra de ouro dos scripts que escrevem:** em teste, saída **sempre** fora do repositório (`/tmp`)
> e confirme com `git status` (armadilha nº 26). Sem CLI (o cálculo), rode numa **cópia** do projeto.

## 5 — Ordem no projeto novo

1. **Decidir** — adaptar × generalizar (§2).
2. **`padroes`/`modulos`** do inventário; conferir a distribuição das páginas por tipo.
3. **Parâmetros + ajustes finos** — imagens por tipo, fóruns, bibliografia, textos externos, H5P.
4. **Marca/espelho** — logos, cores, título do curso, responsável.
5. **Rodar a paridade** (§4) e **registrar** o resultado.

## 6 — Remissões

- Método: `SKILL.md` · Planilha de cálculo: `reference/calculo-e-planilha.md` · Esteira: `reference/esteira-documento.md`
- Resumo executivo: `reference/resumo-executivo.md` · Parâmetros e fontes: `reference/parametros.md`
- Instância da esteira: `assets/esteira/LEIA-ME.md` · Valores de exemplo: `assets/exemplo-calc-vagalume.json`
