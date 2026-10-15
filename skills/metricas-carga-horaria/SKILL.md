---
name: metricas-carga-horaria
description: Estima a carga horária efetiva de um curso Moodle a partir do inventário de recursos (páginas, palavras, imagens, vídeos, atividades, fóruns, bibliografia, navegação) e de parâmetros de tempo com fontes citadas. Use quando o usuário pedir a "carga horária", o "tempo de dedicação" ou a "carga efetiva" de um curso, quando for preciso separar carga obrigatória de carga opcional, quando for necessário produzir/atualizar um relatório imprimível (PDF/DOCX) ou um resumo executivo (1–2 páginas) com a estimativa de tempo do curso, ou quando for preciso reexecutar a estimativa depois que um módulo previsto (estimado por analogia) for produzido. Projeto de origem: Vaga Lume (Moodle 4.5).
---

# Métricas de Carga Horária — Curso Moodle

Produz a **carga horária efetiva** de um curso Moodle por **categoria de recurso**: é uma
**estimativa** (não medição), com **quantidades exatas e rastreáveis** e **parâmetros de tempo
com fonte citada**. Exportável para qualquer projeto Moodle.

> ⚠️ **LEIA PRIMEIRO — vai usar a skill em OUTRO projeto?** → **`LEIA-PRIMEIRO.md`**: a regra
> **adaptar × generalizar**, o **checklist dos pontos de instância** e o **oráculo** (paridade byte a byte).

## Quando usar

- Pedido explícito de **carga horária / tempo de dedicação / carga efetiva** de um curso.
- Necessidade de **separar carga obrigatória × carga opcional**.
- Produção/atualização de **relatório imprimível** (PDF A4 + DOCX + XLSX) com a estimativa.
- Produção de um **resumo executivo de 1–2 páginas** (para a coordenação) a partir do relatório.
- **Reexecução** quando o curso cresce (novo módulo, novas atividades, novo encontro) — inclusive para
  **substituir pela medição** um módulo que antes havia sido **estimado por analogia**.

## Quando NÃO usar

- Se existir **relatório oficial de duração/conclusão do Moodle** — aí se **mede**, não se estima.
- Para **avaliação de aprendizagem** — isto não mede o que o aluno aprendeu.
- Com **todo** o conteúdo **ainda não escrito** (sem inventário algum) — primeiro produza o material.
  **Exceção:** um **módulo isolado** ainda não produzido **não invalida** o método — ele entra como
  **estimativa por analogia** com um módulo já existente, **com ressalva declarada** (ver Passo 4 e
  `reference/metodo-e-cenarios.md`).

## Princípios (não negociáveis)

1. **É ESTIMATIVA, não medição** — o relatório **declara isso** na metodologia.
2. **Quantidade ≠ parâmetro** — quantidades são **exatas e rastreáveis** (arquivo, página, pacote);
   os tempos são **parâmetros**.
3. **Nível de confiança sempre explícito** por parâmetro: 🟢 **científico** (com DOI),
   🟡 **benchmark** (referência institucional/mercado), 🔴 **heurística do projeto** (sem fonte
   canônica — a derivação é explicitada). **Nunca apresentar heurística como ciência.**
   ⚠️ **No entregável imprimível os emojis saem PRETOS** — ali eles viram **badges coloridos + rótulo
   textual** (`Científico` · `Benchmark` · `Heurística`); os emojis ficam **só** na documentação interna.
4. **Separar sempre** carga **obrigatória** × **opcional/complementar** (protege o número principal).
5. **Sem dupla contagem** — ver `reference/metodo-e-cenarios.md`.
6. **Três cenários + recomendado** (mínimo · referência · máximo · recomendado).
7. **Módulo previsto e ainda não produzido** → pode entrar como **estimativa por analogia** com um
   módulo existente (medido), **sempre com ressalva declarada** e substituição pela **medição** na
   reexecução (Passo 6). **Nunca** apresentar a analogia como se fosse medição.

## Método — 6 passos

### Passo 1 · Inventariar (quantidades)

Rode o script e/ou conte manualmente. Item a item, por página:

| O que contar | Como obter |
|---|---|
| **Páginas** de conteúdo | arquivos de página do curso (ex.: `templates/pages/**/*.html`) |
| **Palavras visíveis** por página | texto sem tags/comentários/`<script>`/`<style>` |
| **Imagens** | marcadores de imagem oficiais (ex.: `[cole a imagem aqui]`) |
| **Vídeos** | embedados (iframe) + **instruídos por link** + **trechos**; **duração real** dos créditos |
| **Atividades** | nº de atividades + **nº de itens/questões** (lidos do `content.json` dentro do `.h5p`) |
| **Fóruns** | nº de fóruns (contar o **ciclo completo** exigido no enunciado) |
| **Bibliografia** | nº de itens (separar **texto** × **vídeo**) |
| **Navegação** | páginas + labels de parte + páginas de frontpage |
| **Anexos** | PDFs/arquivos (ex.: Sequências Didáticas) e suas páginas |

**Regras de contagem (validadas no projeto de origem):**
- Vídeo **embedado ou instruído** → **conta**; vídeo **sugerido** ("Quer saber mais?", bibliografia)
  → é **registrado** e **não** conta no tempo efetivo.
- Instrução de **trecho** (ex.: "assista do minuto 34:29 até 54:15") → conta **só o trecho**.
- Pacote de atividade **sem página vinculada** (órfão) → **não conta** (registrar como aviso).

**Durações de vídeo:** as minutagens costumam estar nos **créditos da própria página** — prefira-as.
Quando faltar, obter por **oEmbed**/*lengthSeconds* e **nunca estimar no escuro**.
Receita pronta (comandos), regra do **trecho** e o **cruzamento bibliografia × curso** (anti-dupla-contagem):
`reference/duracoes-e-cruzamento.md`. Onde mora a **contagem de itens** de cada tipo de H5P:
`reference/h5p-tipos.md`.

### Passo 1b · Rodar o script (`assets/inventario-recursos.py`)

```bash
python3 inventario-recursos.py --root <raiz-do-projeto> --config <config-do-projeto>.json
```

Copie `assets/exemplo-config-vagalume.json`, ajuste as **5 chaves** e mantenha o config **dentro do
projeto** (versionado) — é ele que torna a reexecução reproduzível:

| Chave | O que é |
|---|---|
| `modulos` | pasta do módulo → sigla usada no relatório |
| `ref_paginas` | páginas de Referências Bibliográficas (relativas à pasta de páginas) |
| `ignorar` | pastas de **interface** (labels, frontpage, base) — não são conteúdo |
| `padroes` | strings que identificam o **tipo** de cada página (referências, fórum, síntese, abertura) |
| `duracoes` | id do YouTube → segundos (vídeos **sem** minutagem nos créditos) |

⚠️ **Sem `--config`** o script roda, mas com `modulos`/`ref_paginas`/`duracoes` **vazios**: o módulo vira
o **nome da pasta**, a seção de bibliografia sai **vazia** e os vídeos sem crédito entram como
**“duração não localizada”**. Rode sempre com o config e passe pela **validação de paridade**.

⚠️ **`padroes` é a falha silenciosa nº 1 em projeto novo:** se os títulos das páginas forem outros, **tudo**
cai como `conteudo` (some a distinção entre conteúdo, abertura, síntese, referências e fórum). Ajuste as 4
listas ao vocabulário do projeto e confira a tabela “Distribuição das páginas por tipo” na saída.

### Passo 2 · Parametrizar (tempos)

Use a tabela de referência em `reference/parametros.md` (cada parâmetro com valor, faixa e **fonte**).
Ajuste ao contexto: **idioma**, **público** (adulto especialista × não especialista), **mídia**
(tela × papel) e **tipo de recurso**. Mantenha o **rótulo de confiança** e registre cada ajuste numa
tabela de **decisões do cliente**.

Regra de segurança: na dúvida, escolha o valor **mais lento** (estimativa maior) — **nunca otimista**.

### Passo 3 · Cenários

| Cenário | Como obter |
|---|---|
| **Mínimo** | todos os parâmetros na ponta **rápida** (menos tempo) |
| **Referência** | valores da tabela |
| **Máximo** | todos na ponta **lenta** (mais tempo) |
| **Recomendado** | **referência + overhead** de estudo (pausas e retomadas) |

O **overhead** e a sua justificativa (âncora real do curso — ex.: uma página que ensina o Método
Pomodoro) estão em `reference/metodo-e-cenarios.md`.

### Passo 4 · Calcular e agregar (planilha de cálculo)

`tempo(categoria) = quantidade × parâmetro × fator de cenário`

**Duas camadas, nesta ordem:**

1. **Ajustes finos** (entre os Passos 1 e 2) — o que o inventário automático **não** faz: classificar as
   **imagens por tipo**, revisar os **enunciados de fórum**, cruzar **bibliografia × vídeos** e medir os
   **textos externos instruídos**. Vivem em **arquivo próprio do projeto** (no projeto de origem:
   `ajustes-finos.md`) — o **inventário fica INTACTO** (reprodutibilidade). **Regra de ouro:** nunca
   editar o CSV/MD do inventário à mão.
2. **Cálculo página a página** — uma **linha por página** + as **linhas de ajuste** (itens que **não** são
   página: navegação de interface, encontros, gravações, estimativas por analogia). Agregue por **parte**,
   **módulo**, **categoria** e **bucket**; aplique as **regras anti-dupla-contagem** de
   `reference/metodo-e-cenarios.md`.

O **modelo da planilha**, o **dicionário das colunas** e a **reconciliação com âncoras** (verificação de
sanidade contra os subtotais já conhecidos) estão em **`reference/calculo-e-planilha.md`**. O script que
aplica os parâmetros e gera o `.csv` + as tabelas-resumo é **`assets/calculo-carga-horaria.py`**
(instância de exemplo: `assets/exemplo-calc-vagalume.json`).

> ⚠️ O script é uma **instância** (traz os parâmetros e os ajustes finos do projeto de origem **no código**).
> Ao exportar a skill, **revise o cabeçalho** e troque os dicionários/config pelos **do seu projeto**.

### Passo 5 · Relatar (relatório completo + resumo executivo)

**Dois entregáveis imprimíveis**, ambos por **esteira** (nunca montados à mão):

1. **Planilha + relatório completo** — planilha de cálculo (`.csv` / `.xlsx`) + **relatório** a partir de
   `assets/esqueleto-relatorio.md`: `.md` → **espelho HTML A4** → **PDF por Chrome headless**; **DOCX** por
   `pandoc --reference-doc` + pós-processadores. Esteira, comandos e armadilhas: **`reference/esteira-documento.md`**.
2. **Resumo executivo de 1–2 páginas** — mesma identidade, **cabeçalho compacto** (sem a capa inteira).
   Padrão e **técnica de fechar em N páginas**: **`reference/resumo-executivo.md`**
   (modelo: `assets/esqueleto-resumo-executivo.md`).
3. **Validação final** — conferir contra a lista do esqueleto e declarar natureza, fontes, cenários,
   buckets, limitações **e** o que ficou **estimado por analogia** (Passo 6).

> **Níveis de confiança no entregável:** **não** use os emojis 🟢🟡🔴 no PDF/DOCX (saem **preto**). No
> imprimível eles viram **badges coloridos + rótulo textual**; os emojis ficam **só** na documentação interna.
> Ver `reference/esteira-documento.md` e os espelhos em `assets/`.

### Passo 6 · Reexecutar (quando o curso mudar)

1. **Rode o Passo 1 de novo** — o script pega as páginas novas **automaticamente**; atualize o **snapshot**.
2. **Recalcule** com a **mesma** tabela de parâmetros e o **mesmo** config; **substitua** as estimativas
   **por analogia** (Passo 4) pelas **medições reais**; **reincorpore** o que estava fora por falta de quantidades.
3. **Regerar** PDF + DOCX + XLSX e o resumo executivo; **reentregar**.
4. **Bloqueio por inércia, revisão por gatilho:** os parâmetros e as **decisões do cliente** **não** se
   rediscutem por padrão. Reabra **só** com gatilho declarado — **(a)** pedido do cliente, **(b)** mudança do
   curso que **invalide** a decisão, ou **(c)** **evidência/fonte nova**. Ao reabrir: registre **motivo +
   valor novo + data** na **tabela de decisões do cliente** e **refaça a paridade**. Ver
   `reference/metodo-e-cenarios.md`.

## Validação de paridade (obrigatória ao **exportar** a skill)

Antes de confiar numa nova exportação, prove que o script reproduz o projeto de origem:

1. rode com o **config do projeto de origem**, com **as saídas fora do projeto** (`--csv /tmp/check.csv --md /tmp/check.md`) — **sempre com `--md` também**: sem ele o MD é gravado no caminho **padrão** e **sobrescreve o inventário oficial** (armadilha nº 19);
2. compare com o inventário oficial: `diff /tmp/check.csv <inventario-oficial>.csv` → **tem de ser idêntico**;
3. **se divergir, investigue antes de usar** — quase sempre é (a) `modulos`/`padroes` do config ou
   (b) uma correção que existe num script e não no outro;
4. **valide também o Passo 4:** o script de cálculo da v1.2 **não tem CLI** — grava nos **caminhos fixos** do
   projeto. Rode-o **numa cópia** do projeto (`cp -r <projeto> /tmp/paridade`, coloque o script doado em
   `/tmp/paridade/scripts/`) e compare o `calculo-*.csv` gerado com o **oficial** (`diff`) — tem de ser idêntico;
5. registre o resultado (data + “idêntico”/divergências) no relatório ou no checkpoint do projeto.

> **Fonte da verdade:** o **script do projeto** é a instância viva; o da skill é a **versão doada**.
> Ao corrigir um bug em um, **corrija no outro e rode a paridade de novo**.
> *Teste de 14/10/2026 (Vaga Lume, Passo 1): CSV **idêntico byte a byte** — 147 páginas, todos os totais.*

## Adaptar a outro projeto — checklist

**Troca (é do projeto):**
- [ ] Caminhos (páginas, pacotes `.h5p`, anexos, saída dos relatórios).
- [ ] Nomes/siglas dos módulos e a estrutura de pastas.
- [ ] Definição dos **buckets** (o que é obrigatório × opcional naquele curso).
- [ ] **Âncora interna** de tempo (a regra/página que o curso dá ao aluno).
- [ ] Decisões do cliente (registradas e versionadas) — inclusive a **tabela** delas.
- [ ] **Identidade do imprimível**: logos, cores, título do curso, responsável e o **espelho A4**.

**NÃO troca (é do método):**
- [ ] Estrutura em **6 passos** e a separação obrigatório × opcional.
- [ ] Rótulo de confiança (**badges no imprimível**, emojis só na documentação) e **citação das fontes**.
- [ ] Cenários + overhead; regras anti-dupla-contagem; declaração "estimativa, não medição".
- [ ] **Dois entregáveis** (relatório completo + resumo executivo) e a **esteira** que os gera.

## Arquivos da skill

```
skills/metricas-carga-horaria/
├── SKILL.md                           ← este arquivo (a skill)
├── LEIA-PRIMEIRO.md                   ← onboarding: adaptar × generalizar (LER em projeto novo)
├── reference/
│   ├── parametros.md                  ← tabela de parâmetros + fontes citadas
│   ├── metodo-e-cenarios.md           ← fórmula, cenários, overhead, anti-dupla-contagem, decisões do cliente
│   ├── calculo-e-planilha.md          ← modelo/dicionário da planilha de cálculo + reconciliação (Passo 4)
│   ├── esteira-documento.md           ← .md → espelho A4 → PDF/DOCX/XLSX (Passo 5) + as travas
│   ├── resumo-executivo.md            ← resumo de 1–2 páginas + técnica de fechar em N páginas
│   ├── armadilhas.md                  ← o que dá errado e como evitar (lições) + checklist final
│   ├── h5p-tipos.md                   ← onde mora a contagem de itens em cada tipo de H5P
│   └── duracoes-e-cruzamento.md       ← durações (créditos/oEmbed), trecho e cruzamento bibliografia × curso
└── assets/
    ├── inventario-recursos.py         ← script generalizável (CLI) do Passo 1
    ├── exemplo-config-vagalume.json   ← config de inventário de exemplo (projeto de origem)
    ├── calculo-carga-horaria.py       ← script do Passo 4 (instância de exemplo, verificada na paridade)
    ├── exemplo-calc-vagalume.json     ← ajustes finos de exemplo (imagens, fóruns, bibliografia, H5P, encontros)
    ├── esqueleto-relatorio.md         ← modelo do relatório completo
    ├── esqueleto-resumo-executivo.md  ← modelo do resumo executivo
    └── esteira/                       ← espelhos A4 + pós-processadores DOCX + scripts de geração + LEIA-ME
```

## Versionamento e reuso

- **Versão atual: 1.2.1 (15/10/2026)** — projeto de origem **Vaga Lume** (Moodle 4.5).
- **Exportar para outro projeto:** **copie a pasta inteira** `skills/metricas-carga-horaria/` e ajuste
  apenas o que o **checklist de adaptação** indica; depois rode a **validação de paridade**.
- **Reexecutar:** rode o script (Passo 1) com o **config do projeto** e recalcule com a **mesma** tabela de
  parâmetros; as **decisões do cliente** ficam guardadas no projeto — **não se refaz a discussão**
  (revisão só por gatilho declarado; ver Passo 6).
- **Ao publicar o relatório, cite as fontes** de `reference/parametros.md` e a **versão da skill**.

| Versão | Data | Mudanças |
|---|---|---|
| 1.0 | 14/10/2026 | Primeira versão: SKILL.md (5 passos), `parametros.md` (13 parâmetros + 8 fontes), `metodo-e-cenarios.md`, `armadilhas.md`, script CLI e esqueleto do relatório. |
| **1.1** | **14/10/2026** | **`padroes` parametrizável** no script (fim dos títulos fixos; falha silenciosa documentada) + **paths relativos resolvidos a partir de `--root`**; **`exemplo-config-vagalume.json`**; **seção “Validação de paridade”**; novos arquivos **`h5p-tipos.md`** e **`duracoes-e-cruzamento.md`** (com o erro 60× do trecho, o falso positivo do cruzamento e a receita oEmbed/`lengthSeconds`); **critérios de classificação de imagens** e **dicionário de dados do CSV**; armadilhas nº 14–18. |
| **1.1.1** | **14/10/2026** | **Revisão pós-auditoria** (sessão nova): `--md` **obrigatório** na validação de paridade + **armadilha nº 19** (testar sem `--md` sobrescreve o inventário oficial); descrição de `reference/`/`assets/` corrigida no mapa do projeto; `--config` (help) passa a citar **`padroes`**; o esqueleto passa a citar `v{{versão da skill}}`. |
| **1.2.1** | **15/10/2026** | **Onboarding da skill:** novo **`LEIA-PRIMEIRO.md`** (a ler ao usar em outro projeto) com a regra **adaptar × generalizar**, o **checklist dos pontos de instância** (§3) e o **oráculo** de paridade (§4); aviso no topo do `SKILL.md`. **Sem mudança de código.** |
| **1.2** | **15/10/2026** | **Lições dos Ciclos 0–6 do relatório de carga horária (Vaga Lume).** Nova **arquitetura da skill** com mais 3 `reference/` (`calculo-e-planilha.md`, `esteira-documento.md`, `resumo-executivo.md`); **Passo 4** ganha o **modelo da planilha** + o script `calculo-carga-horaria.py` (antes pendência do roadmap); **Passo 5** ganha a **esteira de documento** (espelho A4 → PDF Chrome headless; DOCX por pandoc + `ajustar-tabelas-docx.py` + `adicionar-logos-docx.py`; XLSX) e o **resumo executivo de 1–2 páginas** (com a técnica de fechar em N páginas); **novo Passo 6 — Reexecutar** + regra **“bloqueio por inércia, revisão por gatilho”**; **estimativa por analogia** (módulo não produzido, com ressalva) reconciliada com o “Quando NÃO usar”; **níveis de confiança** passam a **badges coloridos + rótulo textual** no imprimível; **decisões do cliente** e **anti-dupla-contagem** ampliadas; **armadilhas nº 20–26**; esqueletos (relatório e resumo executivo) e assets da esteira doados. |

### Roadmap / pendências desta skill

- [x] **Modelo da planilha de cálculo** — **doada na v1.2** (`reference/calculo-e-planilha.md` + `assets/calculo-carga-horaria.py` + `assets/exemplo-calc-vagalume.json`).
- [ ] **Generalizar os scripts** — hoje são **instâncias** (parâmetros e ajustes finos no código): migrar
      `calculo-carga-horaria.py` e os pós-processadores DOCX para **config JSON** (mesmo padrão do
      `--config` do inventário), para exportação sem editar código. **Gatilho declarado: quando houver
      2º projeto/exportação à vista — ver `LEIA-PRIMEIRO.md` §2 (adaptar × generalizar).**
- [ ] Avaliar um **modo `--h5p-itens`** que liste, por pacote, a chave usada e o valor lido (auditoria rápida
      da contagem do Passo 1).
- [ ] Se um projeto usar **outra plataforma** (não Moodle), registrar no `armadilhas.md` o que muda
      (o script é acoplado ao HTML de página + pacotes `.h5p`).
