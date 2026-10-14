---
name: metricas-carga-horaria
description: Estima a carga horária efetiva de um curso Moodle a partir do inventário de recursos (páginas, palavras, imagens, vídeos, atividades, fóruns, bibliografia, navegação) e de parâmetros de tempo com fontes citadas. Use quando o usuário pedir a "carga horária", o "tempo de dedicação" ou a "carga efetiva" de um curso, quando for preciso separar carga obrigatória de carga opcional, ou quando for necessário produzir/atualizar um relatório imprimível (PDF/DOCX) com a estimativa de tempo do curso. Projeto de origem: Vaga Lume (Moodle 4.5).
---

# Métricas de Carga Horária — Curso Moodle

Produz a **carga horária efetiva** de um curso Moodle por **categoria de recurso**: é uma
**estimativa** (não medição), com **quantidades exatas e rastreáveis** e **parâmetros de tempo
com fonte citada**. Exportável para qualquer projeto Moodle.

## Quando usar

- Pedido explícito de **carga horária / tempo de dedicação / carga efetiva** de um curso.
- Necessidade de **separar carga obrigatória × carga opcional**.
- Produção/atualização de **relatório imprimível** (PDF A4 + DOCX) com a estimativa.
- **Reexecução** quando o curso cresce (novo módulo, novas atividades, novo encontro).

## Quando NÃO usar

- Se existir **relatório oficial de duração/conclusão do Moodle** — aí se **mede**, não se estima.
- Para **avaliação de aprendizagem** — isto não mede o que o aluno aprendeu.
- Com conteúdo **ainda não escrito** (sem inventário) — primeiro produza o material.

## Princípios (não negociáveis)

1. **É ESTIMATIVA, não medição** — o relatório **declara isso** na metodologia.
2. **Quantidade ≠ parâmetro** — quantidades são **exatas e rastreáveis** (arquivo, página, pacote);
   os tempos são **parâmetros**.
3. **Nível de confiança sempre explícito** por parâmetro: 🟢 **científico** (com DOI),
   🟡 **benchmark** (referência institucional/mercado), 🔴 **heurística do projeto** (sem fonte
   canônica — a derivação é explicitada). **Nunca apresentar heurística como ciência.**
4. **Separar sempre** carga **obrigatória** × **opcional/complementar** (protege o número principal).
5. **Sem dupla contagem** — ver `reference/metodo-e-cenarios.md`.
6. **Três cenários + recomendado** (mínimo · referência · máximo · recomendado).

## Método — 5 passos

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

### Passo 4 · Calcular e agregar

`tempo(categoria) = quantidade × parâmetro × fator de cenário`

Calcule **página a página** (uma linha por página) e agregue por **parte**, **módulo**, **categoria**
e **bucket** (obrigatório/opcional). Aplique as **regras anti-dupla-contagem** de
`reference/metodo-e-cenarios.md`.

### Passo 5 · Relatar

1. Saída de cálculo: planilha (`.csv`) com uma linha por página + tabelas-resumo.
2. Relatório imprimível: **PDF A4** (com a identidade do projeto) + **DOCX** editável — use o
   esqueleto `assets/esqueleto-relatorio.md`.
3. Validação final: conferir contra a lista de conferência do esqueleto e declarar natureza,
   fontes, cenários, buckets e limitações.

## Validação de paridade (obrigatória ao **exportar** a skill)

Antes de confiar numa nova exportação, prove que o script reproduz o projeto de origem:

1. rode com o **config do projeto de origem**, com o CSV **fora** do projeto (`--csv /tmp/check.csv`);
2. compare com o inventário oficial: `diff /tmp/check.csv <inventario-oficial>.csv` → **tem de ser idêntico**;
3. **se divergir, investigue antes de usar** — quase sempre é (a) `modulos`/`padroes` do config ou
   (b) uma correção que existe num script e não no outro;
4. registre o resultado (data + “identico”/divergências) no relatório ou no checkpoint do projeto.

> **Fonte da verdade:** o **script do projeto** é a instância viva; o da skill é a **versão generalizada**.
> Ao corrigir um bug em um, **corrija no outro e rode a paridade de novo**.
> *Teste de 14/10/2026 (Vaga Lume): CSV **idêntico byte a byte** — 147 páginas, todos os totais.*

## Adaptar a outro projeto — checklist

**Troca (é do projeto):**
- [ ] Caminhos (páginas, pacotes `.h5p`, anexos, saída dos relatórios).
- [ ] Nomes/siglas dos módulos e a estrutura de pastas.
- [ ] Definição dos **buckets** (o que é obrigatório × opcional naquele curso).
- [ ] **Âncora interna** de tempo (a regra/página que o curso dá ao aluno).
- [ ] Decisões do cliente (registradas e versionadas).

**NÃO troca (é do método):**
- [ ] Estrutura em 5 passos e a separação obrigatório × opcional.
- [ ] Rótulo de confiança 🟢🟡🔴 e **citação das fontes**.
- [ ] Cenários + overhead; regras anti-dupla-contagem; declaração "estimativa, não medição".

## Arquivos da skill

```
skills/metricas-carga-horaria/
├── SKILL.md                          ← este arquivo (a skill)
├── reference/
│   ├── parametros.md                 ← tabela de parâmetros + fontes citadas
│   ├── metodo-e-cenarios.md          ← fórmula, cenários, overhead, anti-dupla-contagem + dicionário do CSV
│   ├── armadilhas.md                 ← o que dá errado e como evitar (lições) + checklist final
│   ├── h5p-tipos.md                  ← onde mora a contagem de itens em cada tipo de H5P
│   └── duracoes-e-cruzamento.md      ← durações (créditos/oEmbed), trecho e cruzamento bibliografia × curso
└── assets/
    ├── inventario-recursos.py        ← script generalizável (CLI) do Passo 1
    ├── exemplo-config-vagalume.json  ← config de exemplo (calibrado no projeto de origem)
    └── esqueleto-relatorio.md        ← modelo do relatório final
```

## Versionamento e reuso

- **Versão atual: 1.1 (14/10/2026)** — projeto de origem **Vaga Lume** (Moodle 4.5).
- **Exportar para outro projeto:** **copie a pasta inteira** `skills/metricas-carga-horaria/` e ajuste
  apenas o que o **checklist de adaptação** indica; depois rode a **validação de paridade**.
- **Reexecutar:** rode o script (Passo 1) com o **config do projeto** e recalcule com a **mesma** tabela de
  parâmetros; as **decisões do cliente** ficam guardadas no projeto (não se refaz a discussão).
- **Ao publicar o relatório, cite as fontes** de `reference/parametros.md` e a **versão da skill**.

| Versão | Data | Mudanças |
|---|---|---|
| 1.0 | 14/10/2026 | Primeira versão: SKILL.md (5 passos), `parametros.md` (13 parâmetros + 8 fontes), `metodo-e-cenarios.md`, `armadilhas.md`, script CLI e esqueleto do relatório. |
| **1.1** | **14/10/2026** | **`padroes` parametrizável** no script (fim dos títulos fixos; falha silenciosa documentada) + **paths relativos resolvidos a partir de `--root`**; **`exemplo-config-vagalume.json`**; **seção “Validação de paridade”**; novos arquivos **`h5p-tipos.md`** e **`duracoes-e-cruzamento.md`** (com o erro 60× do trecho, o falso positivo do cruzamento e a receita oEmbed/`lengthSeconds`); **critérios de classificação de imagens** e **dicionário de dados do CSV**; armadilhas nº 14–18. |

### Roadmap / pendências desta skill

- [ ] **Modelo da planilha de cálculo** (Passo 4: uma linha por página + tempos por cenário): doar para a
      skill o `calculo-carga-horaria.csv` do projeto de origem **quando o Ciclo 4 o produzir**.
- [ ] Avaliar um **modo `--h5p-itens`** que liste, por pacote, a chave usada e o valor lido (auditoria rápida
      da contagem do Passo 1).
- [ ] Se um projeto usar **outra plataforma** (não Moodle), registrar no `armadilhas.md` o que muda
      (o script é acoplado ao HTML de página + pacotes `.h5p`).
