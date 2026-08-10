# 📋 Relatório de Auditoria de Acessibilidade — Módulo 2

> **Data:** 10/08/2026
> **Escopo:** 36 arquivos HTML do Módulo 2 (Apresentação + Partes 1 a 6 + fóruns)
> **Foco:** VLibras e leitores de tela
> **Natureza:** Auditoria apenas (sem correção — correções serão feitas uma página por vez, após autorização)

---

## Resumo geral

| Parte | Páginas | Conformes | Com pendência |
|-------|---------|-----------|---------------|
| Apresentação | 1 | ✅ 1 | — |
| Parte 1 (Lição 1 + Fórum) | 4 | ✅ 4 | — |
| Parte 2 (Lição 1) | 2 | ✅ 2 | — |
| Parte 3 (Lições 1-2 + Fórum) | 7 | ✅ 5 | ⚠️ 2 |
| Parte 4 (Lições 1-4 + Fórum) | 14 | ✅ 10 | ⚠️ 4 |
| Parte 5 (Lição 2 + Fórum) | 6 | ✅ 5 | ⚠️ 1 |
| Parte 6 (Síntese) | 2 | ✅ 2 | — |
| **TOTAL** | **36** | **29** | **7 pendências** |

## ✅ Pontos fortes verificados

- **Nenhuma página com snippet VLibras** (correto — já é global no Moodle)
- **Nenhuma imagem sem alguma forma de descrição** (todas têm `alt` ou `sr-only`)
- **Todos os ícones** com `aria-hidden="true"`
- **Todos os vídeos** (YouTube) com `title` acessível
- **Blocos bege** usam `<strong>` (sem `.vagalume-destaque`)
- **Hierarquia de headings** sem saltos severos

---

## 📌 Pendências identificadas (7)

| # | Parte | Página | Imagem | Problema |
|---|-------|--------|--------|----------|
| 1 | Parte 3 | `M2P3L1p1.html` | Tirinha da Magali | `alt` genérico ("Tirinha da Magali sobre leitura") sem descrever o conteúdo da tirinha |
| 2 | Parte 3 | `M2P3L2p1.html` | Garoto na piscina de livros | `alt=""` + `<span class="sr-only">` fora do padrão N2.4.7 (falta `<p class="sr-only" id="figX-desc">` + `aria-labelledby`) |
| 3 | Parte 4 | `M2P4L1p1.html` | Tirinha Macanudo | Mesma questão do item 2 (`alt=""` + `<span class="sr-only">`) |
| 4 | Parte 4 | `M2P4L3p1.html` | Acervo Vaga Lume | `alt=""` + `<span class="sr-only">` + **falta `height`** no `<img>` |
| 5 | Parte 4 | `M2P4L4p1.html` | Quadrinho May_1 | **Descrição duplicada** (`<div class="sr-only">` + `alt` preenchido) |
| 6 | Parte 4 | `M2P4L4p2.html` | Quadrinho May_2 | **Descrição duplicada** (`<div class="sr-only">` + `alt` preenchido) |
| 7 | Parte 5 | `M2P5L2p1.html` | Kaio (ilustração) | Faltam `width`, `height`, `loading="lazy"` |

## Natureza das pendências

- **Nenhuma imagem está sem descrição absoluta** — todas têm alguma descrição acessível a leitores de tela/VLibras.
- **6 de 7** pendências são de **adequação ao padrão N2.4.7** (`<p class="sr-only" id="figX-desc">` + `aria-labelledby`) ou **duplicação de leitura** (sr-only + alt) — correções de qualidade, não bloqueios.
- **1 pendência** (#7) é de **atributos de imagem** (checklist N2.1.1.4).

---

## Detalhamento por parte

### Parte: Apresentação do Módulo 2 (1 arquivo)
- `M2-Apresentacao_do_modulo_2.html` — ✅ OK (sem imagens; ícones com `aria-hidden`; headings h1→h2→h3)

### Parte 1 — O Bebê e a Linguagem (4 arquivos)
- `M2P1L1p1.html` — ✅ OK (imagem "cosquinha na mamãe" com `alt` descritivo completo)
- `M2P1L1p2.html` — ✅ OK (imagem do homem cantando com `alt` detalhado)
- `M2P1L1p3.html` — ✅ OK (H5P; sem imagens)
- `M2P1F1.html` — ✅ OK (sem imagens; ícones ok)

### Parte 2 — Por que ler com bebês e crianças pequenas? (2 arquivos)
- `M2P2L1p1.html` — ✅ OK (vídeo com `title`; sem imagens)
- `M2P2L1p2.html` — ✅ OK (H5P; sem imagens)

### Parte 3 — O que é mediar leitura com a Primeira Infância? (7 arquivos)
- `M2P3L1p1.html` — ⚠️ **Pendência #1** (Tirinha da Magali — `alt` genérico)
- `M2P3L1p2.html` — ✅ OK
- `M2P3L1p3.html` — ✅ OK (H5P)
- `M2P3L2p1.html` — ⚠️ **Pendência #2** (Garoto na piscina — `sr-only` fora do padrão)
- `M2P3L2p2.html` — ✅ OK (blockquote/citação acessível)
- `M2P3L2p3.html` — ✅ OK (H5P)
- `M2P3F1.html` — ✅ OK (fórum)

### Parte 4 — Escolhendo livros para ler com a Primeira Infância (14 arquivos)
- `M2P4L1p1.html` — ⚠️ **Pendência #3** (Tirinha Macanudo — `sr-only` fora do padrão)
- `M2P4L1p2.html` — ✅ OK (ícones `fa-book`/`fa-child`/`fa-globe` ok)
- `M2P4L1p3.html` — ✅ OK (H5P)
- `M2P4L2p1.html` — ✅ OK (vídeo com `title`)
- `M2P4L2p2.html` — ✅ OK (H5P)
- `M2P4L3p1.html` — ⚠️ **Pendência #4** (Acervo Vaga Lume — `sr-only` + falta `height`)
- `M2P4L3p2.html` — ✅ OK (galeria de cards com ícones ok)
- `M2P4L3p3.html` — ✅ OK (H5P)
- `M2P4L4p1.html` — ⚠️ **Pendência #5** (May_1 — descrição duplicada)
- `M2P4L4p2.html` — ⚠️ **Pendência #6** (May_2 — descrição duplicada)
- `M2P4L4p3.html` — ✅ OK (vídeo com `title`)
- `M2P4L4p4.html` — ✅ OK (vídeo com `title`)
- `M2P4L4p5.html` — ✅ OK (H5P)
- `M2P4F1.html` — ✅ OK (fórum)

### Parte 5 — A pessoa mediadora de leitura também é cuidadora? (6 arquivos)
- `M2P5L1p1.html` — ✅ OK (sem imagens)
- `M2P5L1p2.html` — ✅ OK (sem imagens)
- `M2P5L1p3.html` — ✅ OK (H5P; ícones ok)
- `M2P5L2p1.html` — ⚠️ **Pendência #7** (Kaio — faltam `width`/`height`/`loading="lazy"`)
- `M2P5L2p2.html` — ✅ OK (sem imagens)
- `M2P5F1.html` — ✅ OK (fórum)

### Parte 6 — Síntese do Módulo 2 (2 arquivos)
- `M2P6P1.html` — ✅ OK (7 ícones com `aria-hidden`; sem imagens)
- `M2P6P2.html` — ✅ OK (sem imagens; link externo ok)

---

## Próximos passos

- [ ] **Corrigir as 7 pendências** — uma página por vez (ciclo N1.3.3): PLAN → ACT → validação do mestre
- [ ] Atualizar o `Onde-paramos.md` com o registro desta auditoria
- [ ] Commit + push quando autorizado (regra N1.8)