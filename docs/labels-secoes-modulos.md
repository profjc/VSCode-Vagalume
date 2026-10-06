# 🏷️ Labels (HTML) dos Títulos das Seções — Cards dos Módulos (formato Tiles)

> **Registro canônico criado em 06/10/2026** (a pedido do mestre). No curso, os **títulos das seções** (os cards/tiles da home) são colados no Moodle como **HTML** no campo de título de cada seção.
> **Fonte da verdade:** o Moodle. Este arquivo reproduz o que está aplicado no curso (print da home validado em 06/10/2026).

---

## Como aplicar no Moodle

1. Na home do curso, editar o **título da seção** (card/tile) → abrir o **código-fonte (`< >`)** do editor de título.
2. Colar o **snippet HTML** correspondente (tabela abaixo).
3. A cor **laranja-escuro `#944B11`** (paleta N3.1.1, mesma cor dos links) é aplicada **via CSS inline** no `<span>`.
   - **Requer** a configuração do Moodle que **permite CSS inline nos títulos** (habilitada pelo mestre; sem ela, o TinyMCE descarta o `style`).
   - Motivo: o título dentro do card é um campo próprio e **não herda** a regra CSS global `.sectiontitle`.

---

## Tabela canônica (6/6)

| # | `tileicon` | Módulo | Snippet HTML (label — colar no código-fonte do título) | Ícone (`assets/images/icones-tiles/`) |
|---|---|---|---|---|
| 1 | `#tileicon_1` | M0 — Boas-vindas | `<span style="color: #944B11;">Boas-vindas!</span>` | `tile-00-boas-vindas.png` |
| 2 | `#tileicon_2` | M1 — Primeira Infância | `<span style="color: #944B11;">Primeira Infância</span>` | `tile-01-primeira-infancia.png` |
| 3 | `#tileicon_3` | M2 — Leitura e Primeira Infância | `<span style="color: #944B11;">Leitura e Primeira Infância</span>` | `tile-02-leitura-primeira-infancia.png` |
| 4 | `#tileicon_4` | M3 — Bibliotecas Comunitárias | `<span style="color: #944B11;">Bibliotecas Comunitárias</span>` | `tile-03-bibliotecas-comunitarias.png` |
| 5 | `#tileicon_5` | M4 — Mãos na massa! (ou nos Livros!) | `<span style="color: #944B11;">Mãos na massa! (ou nos Livros!)</span>` | `tile-04-mao-na-massa.png` |
| 6 | `#tileicon_6` | Encerramento — Certificação e Avaliação do curso | `<span style="color: #944B11;">Certificação e Avaliação do curso</span>` | `tile-05-certificacao-avaliacao.png` |

---

## Observações

- **Estados do Moodle** (`Restrito`, `Oculto para estudantes`) são controles de **disponibilidade da seção** — **não** fazem parte do label.
- **Ícones dos tiles:** substituídos por CSS (`#tileicon_N .tile-icon { background-image: url('...') }`) — ver `docs/css-icones-tiles-para-colar.css` e o bloco no início de `assets/css/vagalume-tema.css`.
- **URLs dos ícones (Moodle):** `https://vagalume.educagir.com.br/pluginfile.php/145/block_html/content/<arquivo>.png` (detalhes em `docs/teste-icones-tiles.md` §1.1). O bloco HTML que hospeda os ícones deve **permanecer no curso** (pode ficar oculto, nunca excluído).
- **Nome de arquivo do ícone do M4** usa o padrão antigo `tile-04-mao-na-massa.png` (sem acento) — mantido por estabilidade do CSS.

## Histórico

| Data | Mudança |
|---|---|
| 06/10/2026 | Criação do arquivo (registro dos 6 labels). Mestre corrigiu o nome do M4 no Moodle: "Mão na massa" → **"Mãos na massa! (ou nos Livros!)"**. |
