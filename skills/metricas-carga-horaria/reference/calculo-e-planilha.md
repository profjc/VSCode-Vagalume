# Planilha de cálculo — modelo, dicionário e reconciliação (Passo 4)

> Como transformar o **inventário** (quantidades) em uma **planilha de cálculo** — **uma linha por
> página** + **linhas de ajuste** — com o tempo de cada **categoria** nos **4 cenários** e o **bucket**.
> **Versão 1.2 (15/10/2026)** — projeto de origem: Vaga Lume. Complementa `reference/metodo-e-cenarios.md`.
> Saídas: `calculo-<curso>.csv` (a planilha) e `calculo-<curso>.md` (as **tabelas-resumo**). Gera-as o
> script `assets/calculo-carga-horaria.py`.

## 1 — Estrutura

- **Uma linha por página** do inventário (a chave é o **caminho relativo do arquivo** — rastreabilidade).
- **Mais as linhas de ajuste** — itens que **não** são página (navegação de interface, encontros, gravações,
  **estimativa por analogia**).
- Colunas: **identidade** · **quantidades** · **tempo por categoria × cenário** · **totais por bucket**.
- Precedente: **147 páginas + 4 ajustes = 151 linhas de dados** (+ cabeçalho). O nº de ajustes **cresce a
  cada decisão** — não é fixo.

## 2 — Dicionário das colunas

| Grupo | Colunas | O que é |
|---|---|---|
| **Identidade** | `arquivo` · `modulo` · `parte` · `licao` · `tipo_pagina` · `bucket` | `arquivo` = chave de rastreabilidade. `tipo_pagina` ∈ `conteudo` · `abertura` · `sintese` · `referencias` · `forum` · `navegacao` · `encontro` · `gravacao` · `estimativa`. `bucket` = `A` (obrigatória) ou `A/B` quando a linha alimenta os dois |
| **Quantidades** | `palavras` · `imagens` · `video_s` · `h5p_n` · `h5p_itens` · `h5p_tipo` · `forum_min_ref` · `biblio_itens` · `ext_palavras` · `sd_palavras` · `nav_s_ref` | vindas do **inventário** (Passo 1) + dos **ajustes finos** (Passo 4.1). `h5p_n` = nº de atividades; `h5p_itens` = itens somados |
| **Tempo — bucket A** | `A_leitura_{min,ref,max}` · `A_imagem_…` · `A_video_…` · `A_h5p_…` · `A_forum_…` · `A_nav_…` · `A_ext_…` · `A_encontro_…` · `A_total_{min,ref,max}` | cada categoria **nos 3 cenários** + o total da linha |
| **Tempo — bucket B** | `B_biblio_…` · `B_sd_…` · `B_gravacao_…` · `B_imagem_…` · `B_total_{min,ref,max}` | idem, para a carga opcional/complementar |
| **Rastro** | `obs` | a decisão que gerou a linha (ex.: “mural repete o carrossel”) |

> **Recomendado** não é coluna: é calculado no fim — `recomendado = referência × (1 + overhead)`, e o
> overhead incide **somente** sobre o recomendado.

## 3 — Linhas de ajuste (o que não é página)

| `tipo_pagina` | Exemplo (`arquivo`) | Bucket | Observação |
|---|---|---|---|
| `navegacao` | `(ajuste) labels + frontpage` | A | labels + páginas de frontpage × parâmetro de navegação |
| `encontro` | `(ajuste) encontros sincronos (participacao)` | A | nº de encontros × duração por encontro |
| `gravacao` | `(ajuste) Nª gravacao do Encontro (declarada)` | B | **só** a gravação nova/declarada — a página do encontro já carrega as demais |
| `estimativa` | `(ajuste) Módulo X (estimado = Módulo Y)` | A | **estimativa por analogia** — copia, categoria a categoria, um módulo-modelo (ver `metodo-e-cenarios.md` §6) |

## 4 — Reconciliação com âncoras (verificação de sanidade)

Antes de publicar, compare o resultado de cada categoria com **âncoras já conhecidas** do projeto (os
subtotais fechados nos ajustes finos). Divergência > alguns segundos = erro de conta ou de parâmetro.

| Âncora (ajustes finos) | Esperado | Calculado | Confere? |
|---|---|---|---|
| Imagens (bucket A) | 16min40s | 16min40s | ✅ |
| Fóruns (bucket A) | 7h55min00s | 7h55min00s | ✅ |
| Bibliografia (bucket B) | 22min30s | 22min30s | ✅ |
| Textos externos (leitura pura) | 7min37s | 7min37s | ✅ |

> *Valores do projeto de origem (Ciclo 4).* A planilha traz essa tabela pronta na seção “Reconciliação”.

## 5 — O script (`assets/calculo-carga-horaria.py`)

```bash
python3 calculo-carga-horaria.py        # lê o inventário + os ajustes finos; escreve o .csv e o .md
```

- **É uma INSTÂNCIA** (escopo A da v1.2): os **parâmetros** e os **ajustes finos** estão **no código**
  (blocos `PPM`, `ESTUDO`, `IMG_FATOR`, `H5P_PAR`, `FORUM`, `BIBLIO`, `NAV`, `OVERHEAD`, `IMG_S`,
  `BIBLIO_ITENS`, `EXT_PALAVRAS`, `H5P_TIPO`, `ENC_*`).
- **Ao exportar:** revise o **cabeçalho** e troque esses blocos pelos **do seu projeto** (os nomes das
  chaves se mantêm — é a “instanciação”). A **generalização** (config JSON) está no roadmap da skill.
- **Regra dos scripts que escrevem** (lição de 14/10/2026): ao **testar**, redirecione **todas** as saídas
  para fora do projeto (`/tmp`) e confirme com `git status`. Caminho padrão = arquivo oficial do projeto.
- A **validação de paridade** (em `SKILL.md`) roda este script com as saídas em `/tmp` e compara com o
  `calculo-*.csv` oficial: tem de ser **idêntico**.

## 6 — Checklist do Passo 4

- [ ] Inventário **INTACTO** (nada editado à mão); ajustes finos em **arquivo separado**.
- [ ] **Uma linha por página** + as linhas de ajuste com `obs` explicando a decisão.
- [ ] As **4 colunas de cenário** por categoria; **recomendado = ref × (1 + overhead)** só no fim.
- [ ] **Buckets A/B** separados; fórum e página de SD conforme as regras anti-dupla-contagem.
- [ ] **Reconciliação** com as âncoras ✅ (ou divergência investigada).
- [ ] Saídas `.csv` + `.md` gravadas **no projeto**; teste feito **em `/tmp`**.
- [ ] `git status` conferido **antes** de commitar.
