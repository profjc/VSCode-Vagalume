# 📋 Relatório de Auditoria de Acessibilidade — Módulo Boas-vindas

> **Data:** 10/08/2026
> **Escopo:** 4 arquivos HTML do Módulo de Boas-vindas
> **Foco:** VLibras e leitores de tela
> **Natureza:** Auditoria concluída — todas as pendências corrigidas e validadas em 10/08/2026

---

## Resumo geral

| Página | Conforme | Pendências |
|--------|----------|------------|
| P1 — Apresentação | ✅ Corrigida | 0 |
| P2 — Dicas para os cursistas | ✅ Corrigida | 0 |
| P3 — Conheça a Vaga Lume | ✅ Corrigida | 0 |
| P4 — Parceria Van Leer e Vaga Lume | ✅ Corrigida | 0 |
| **TOTAL** | **4/4** | **0 pendências (8 corrigidas em 10/08/2026)** |

## ✅ Pontos fortes verificados

- **Nenhuma página com snippet VLibras** (correto — já é global no Moodle)
- **Todos os ícones Font Awesome** com `aria-hidden="true"`
- **Hierarquia de headings** sem saltos severos (h1 → h3/h4)
- **Links externos** com `.nomediaplugin` + `target="_blank"` + `rel="noopener noreferrer"`
- **Vídeo** com `title` acessível (P3 — "Vídeo: Institucional Vaga Lume")

---

## 📌 Pendências identificadas (8) — todas corrigidas

| # | Página | Problema | Correção (10/08/2026) |
|---|--------|----------|------------------------|
| 1 | P1 — Apresentação | `font-size: 1.2rem` inline na mensagem final — viola N2.2.4 | ✅ Classe `.h5 font-italic` + cor via `style` |
| 2 | P2 — Dicas | Classe `font-style-italic` (não existe no Bootstrap 4) | ✅ Corrigido para `font-italic` |
| 3 | P3 — Conheça | **Duplicidade de leitura** (`alt` + `<span class="sr-only">`) | ✅ `<span class="sr-only">` removido (leitura única) |
| 4 | P3 — Conheça | Placeholder com **data URI variável** | ✅ URL fixa (`placeholder-800x600.jpeg`) + marcador |
| 5 | P4 — Parceria | Logotipo Van Leer: faltam `width` e `height` | ✅ `width="1295" height="1801"` (dimensões reais) |
| 6 | P4 — Parceria | Logotipo Vaga Lume: faltam `width` e `height` | ✅ `width="256" height="251"` (dimensões reais) |
| 7 | P4 — Parceria | Placeholders com **data URI variável** | ✅ 2× URL fixa + marcador |
| 8 | P4 — Parceria | Marcador "⚠️ APAGAR ESTE BLOCO" ausente | ✅ Adicionado nos 2 placeholders |

## Natureza das pendências

- **Nenhuma blockagem absoluta** — nenhuma imagem estava sem descrição.
- **3 pendências** foram de **adequação ao padrão N2.4.7 / placeholder** (duplicidade `alt` + `sr-only`, data URI variável).
- **3 pendências** foram de **atributos de imagem** (`width`/`height` nos logotipos da P4 — dimensões reais, sem impacto na exibição de 90px).
- **2 pendências** foram de **higienização** (font-size inline N2.2.4, classe inexistente `font-style-italic`).

---

## Detalhamento por página (status final)

### P1 — Apresentação (`Boas-vindas_Apresentacao.html`) — ✅ Corrigida
- ✅ **Pendência #1 (10/08/2026):** `font-size: 1.2rem; font-style: italic;` inline → classe `.h5 font-italic` + cor via `style` (N2.2.4).

### P2 — Dicas para os cursistas (`Boas-vindas_Dicas_para_os_cursistas.html`) — ✅ Corrigida
- ✅ **Pendência #2 (10/08/2026):** `font-style-italic` → `font-italic` (classe real do Bootstrap 4).

### P3 — Conheça a Vaga Lume (`Boas-vindas_Conheca_a_Vagalume.html`) — ✅ Corrigida
- ✅ **Pendência #3 (10/08/2026):** removido o `<span class="sr-only">` duplicado — o `alt` do logotipo já descreve. Atributos do logotipo corrigidos para dimensões reais (`256×251`).
- ✅ **Pendência #4 (10/08/2026):** data URI variável → URL fixa (`placeholder-800x600.jpeg`) + marcador "⚠️ APAGAR ESTE BLOCO".

### P4 — Parceria Van Leer e Vaga Lume (`Boas-vindas_Parceria_Van_Leer_e_Vagalume.html`) — ✅ Corrigida
- ✅ **Pendência #5 (10/08/2026):** logotipo Van Leer — adicionados `width="1295" height="1801"` (dimensões reais de `VanLeer_block_black.png`).
- ✅ **Pendência #6 (10/08/2026):** logotipo Vaga Lume — adicionados `width="256" height="251"` (dimensões reais de `LOGO_VAGALUME_RGB-transp-pq.png`).
- ✅ **Pendência #7+#8 (10/08/2026):** 2 placeholders com URL fixa + marcador "⚠️ APAGAR ESTE BLOCO".

**Garantia de exibição (validada pelo mestre):** ambos os logotipos mantêm `style="height: 90px; width: auto;"` — exibidos com 90px de altura, sem impacto visual.

---

## Próximos passos

- [x] **Corrigir as pendências** — uma página por vez (ciclo N1.3.3): PLAN → ACT → validação do mestre
- [x] Atualizar o `Onde-paramos.md` com o registro desta auditoria
- [x] Atualizar `docs/pendencias-projeto.md` (item 2 — revisão de acessibilidade do módulo Boas-vindas concluída)
- [x] **AUDITORIA CONCLUÍDA — 4/4 páginas conformes (10/08/2026).**
- [ ] **Moodle:** colar as 4 páginas corrigidas (substituição completa) — validar logotipos (90px) e placeholders.
- [ ] Commit + push quando autorizado (regra N1.8)