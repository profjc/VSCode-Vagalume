# 📊 Relatório — Auditoria de Templates × Uso Real (Boas-vindas, M1, M2)

> **Data:** 22/08/2026 · **Fases 1–3 do plano de reorganização da galeria**
> **Fontes:** `components-library.md` (25 componentes ativos), livro atual (`docs/templates-galeria/`, 3 páginas), varredura automatizada de ~90 páginas em `templates/pages/` (2 matrizes de assinaturas + 5 leituras pontuais).
> **Objetivo:** subsidiar a Fase 4 (decisões do mestre) e a Fase 5 (reescrita do livro).

---

## 1. Tabela mestra — Componentes catalogados × uso real

| # | Template (nome atual) | Onde consta | Onde é usado (páginas reais) | Para que é usado | Qtd. |
|---|---|---|---|---|---|
| 1 | Botão Primário (CTA) | Biblioteca comp. 1 + livro (texto) | **Nenhuma página real** (links externos usam texto estilizado, regra 6.1) | Links de download/ação | **0** |
| 2 | Card de Destaque (Jumbotron) | Biblioteca comp. 2 + livro | M1P1L1p1, M1P2L1p1, M1P2L1p3, M1P4L1p1 | Citações com autoria | **4** |
| 3 | Bloco de Destaque (Sinopse) | Biblioteca comp. 3 + livro | ~60 páginas (quase todas) | Destaques, resumos, instruções, avisos | **~60** |
| 4 | Player H5P com cabeçalho | Biblioteca comp. 4 + livro | M1P3L2p4 (DragDrop) | Atividade com título no card | **1** |
| 5 | Galeria de Imagens 2/3 colunas | Biblioteca comp. 5 + livro | **Nenhuma no formato documentado** (uso real é faixa fluida `col-4` — ver candidatos) | Múltiplas imagens em linha | **0** |
| 6 | Imagem Flutuante (dir/esq) | Biblioteca comp. 6 + livro | M1P3L2p1, M2P1L1p1, M2P1L1p2, M2P3L2p1, M2P4L3p1, M2P4L4p1, M2P4L4p2, M2P5L2p1 | Ilustração ao lado do texto | **8** |
| 7 | Bloco de Destaque Isolado | Biblioteca comp. 7 | Junto das 8 páginas com float (+ outras) | Bloco colorido ao lado de float | **~10** |
| 8 | Imagem Clicável (Modal) | Biblioteca comp. 8 + livro | **Nenhuma** | Ampliar imagem em pop-up | **0** |
| 9 | Imagem c/ Descrição Longa | Biblioteca comp. 9 + livro | M1P1L1p3, M2P3L1p1, M2P3L2p1, M2P4L1p1, M2P4L3p1, M2P4L4p1, M2P4L4p2 | Acessibilidade (sr-only) | **7** |
| 10 | Vídeo Centralizado (corpo do texto) | Biblioteca comp. 10 | Substituído na prática pelo comp. 23 | Vídeo simples | **0** |
| 11 | Título com Destaque | Biblioteca comp. 11 + livro | Títulos de fóruns/atividades (todas) | Destacar palavra do título | **~15** |
| 12 | Texto com Destaque no Parágrafo | Biblioteca comp. 12 + livro | Várias páginas | Destacar conceito-chave | **~20** |
| 13 | Aviso/Nota (💡) | Biblioteca comp. 13 | Raro (variação da sinopse) | Alertas pontuais | **~2** |
| 14 | Grid de Texto 2 Colunas | Biblioteca comp. 14 + livro | **Nenhuma** | Comparar conceitos | **0** |
| 15 | Img Flutuante c/ Legenda + Desc. Longa | Biblioteca comp. 15 | Incluído nas 8 páginas com float | Float + acessibilidade completa | **(8)** |
| 16 | Cabeçalho de Módulo (H1) | Biblioteca comp. 16 + livro | **Nenhuma** (títulos são inseridos no Moodle, não no HTML) | Título principal | **0** |
| 17 | Grid Objetivo + Expectativas | Biblioteca comp. 17 + livro | M1-Apresentacao, M2-Apresentacao | Abertura de módulo | **2** |
| 18 | Apresentação de Módulo (completo) | Biblioteca comp. 18 | M1-Apresentacao, M2-Apresentacao | Página de abertura do módulo | **2** |
| 19 | Carrossel com Collapse | Biblioteca comp. 19 + livro | M1P1L1p4 (5 slides) | Galeria interativa "saiba mais" | **1** |
| 20 | Padrão de Encerramento (mb-0) | Biblioteca comp. 20 | Regra transversal (todas as páginas) | Economia de espaço no Moodle | transversal |
| 21 | Página Final de Lição c/ H5P | Biblioteca comp. 21 + livro | M1P2L1p10, M1P3L1p4, M1P4L1p7, M2P1L1p3, M2P2L1p2, M2P3L1p3, M2P3L2p3, M2P4L1p3, M2P4L2p2, M2P4L3p3, M2P4L4p5, M2P5L1p3 | Fechamento de lição com quiz | **12** |
| 23 | Vídeo 560px c/ Legenda + Sinopse | Biblioteca comp. 23 | M1P1L1p2, M2P2L1p1, M2P4L2p1, M2P4L4p3, M2P4L4p4 | Vídeo do YouTube com créditos | **5** |
| 24 | Rótulo de Parte (Label) | Biblioteca comp. 24 + template base | 11 labels (M1 P1–P5, M2 P1–P6) | Demarcar partes no curso | **11** |
| 25 | Página de Fórum | Biblioteca comp. 25 + `forum.html` | M1P1F1, M1P3F1, M1P4F1, M2P1F1, M2P3F1, M2P4F1, M2P5F1, BV_Forum_Apresentacao | Atividade de discussão | **8** |
| 26 | Caixa "Para refletir" | Biblioteca comp. 26 | M1P1F1, M1P4F1, M2P3L2p2 | Convite à reflexão (borda laranja) | **3** |

---

## 2. Elementos recorrentes NÃO catalogados — candidatos a novo template

| Candidato (nome simples proposto) | Onde aparece | Para que é usado | Qtd. | Recomendação |
|---|---|---|---|---|
| **Cards de Síntese** | M1P5P1, M2P6P1 | Fechamento de módulo: grid 2 colunas de cards bege (h-100) com ícone grande + título negrito + texto 0.95rem; encerra com celebração (troféu) | **2** | ✅ **PROMOVER** |
| **Referências Bibliográficas** | M1P5P2, M2P6P2 | Página final do módulo: título h4 com borda inferior + lista ABNT com recuo deslocado (padding-left/text-indent) | **2** | ✅ **PROMOVER** |
| **Imagem Centralizada com Legenda** | M2P3L1p1 (Magali), M2P4L1p1 (Canuto), M2P4L4p1/p2 (May), M2P5L2p1 (Kaio), M2P3L2p1, M2P4L3p1 | Tirinhas/ilustrações centralizadas com `figure-caption text-center` (muitas com sr-only) | **~8** | ✅ **PROMOVER** (padrão dominante do M2) |
| **Bloco de Orientação com Ícone (Template B)** | Dicas BV (8×), M1P2L1p4–p9, M1P4L1p3/p4, M2P4L3p2 (5×), M2P5L1p3 (4×), M2P4L2p2... | Dicas/orientações passo a passo: `d-flex align-items-center` + ícone + título/texto dentro de bloco bege | **~20** | ✅ **PROMOVER** (já citado como N3.2.9/10 no `.clinerules`, mas SEM seção própria na biblioteca/livro) |
| **Linha do Tempo Interativa** | M1P3L2p3 | Sequência cronológica expansível: accordion vertical com eixo marrom, pontos e cards bege clicáveis | **1** | 🟡 **AVALIAR** (1 uso, mas alto valor para conteúdos históricos/legais futuros) |
| **Cards de Módulos** | BV Apresentação | Lista dos módulos do curso em cards (`course-card`) com título negrito + descrição | **1** | 🟡 **AVALIAR** (uso único, mas reaparecerá na home/encerramento?) |
| **Faixa Fluida de Imagens** | M1P1L1p5 | 5 imagens lado a lado (`col-4 col-sm px-0`) — formato real usado, diferente do comp. 5 | **1** | 🟡 **AVALIAR** (ou atualizar o comp. 5 para este formato) |
| **Caixa de Convite (fórum)** | BV_Forum_Apresentacao | Card branco borda laranja com texto `.h5` centralizado sem ícone/título | **1** | 🟡 **AVALIAR** (variante do comp. 26 sem título) |
| **Celebração de Fechamento** | M1P5P1, M2P6P1 | Linha centralizada com ícone `fa-trophy` + parabéns | **2** | Incluir como sub-bloco do template "Cards de Síntese" |

---

## 3. Componentes sem uso real — avaliar destino na Fase 4

| Componente | Qtd. usos | Opções |
|---|---|---|
| 1. Botão Primário (CTA) | 0 | Manter (uso previsto) ou remover do livro |
| 5. Galeria 2/3 colunas | 0 (formato não usado) | Substituir pela "Faixa Fluida" ou manter como alternativa |
| 8. Imagem Clicável (Modal) | 0 | Remover da galeria (nunca usado; TinyMCE pode remover scripts) |
| 10. Vídeo Centralizado | 0 (absorvido pelo 23) | Fundir com comp. 23 |
| 14. Grid de Texto 2 Colunas | 0 | Remover ou manter como opção de layout |
| 16. Cabeçalho de Módulo | 0 | Remover (títulos vêm do Moodle) — rever comp. 18 |

---

## 4. Divergências biblioteca × uso real (corrigir na Fase 5)

1. **Comp. 18 (Apresentação de Módulo):** a biblioteca prevê jumbotron de apresentação; as páginas reais usam blocos `.vagalume-destaque-bloco` (objetivo/expectativas) — atualizar snippet.
2. **Comp. 5 (Galeria):** formato documentado (col-md-6/4) nunca usado; o real é a faixa fluida `col-4`.
3. **Template B (N3.2.9/10):** citado no `.clinerules` mas sem seção própria em `components-library.md` — lacuna a preencher.
4. **Comp. 22:** numeração saltada (excluído em 08/08) — renumerar na reescrita.

---

## 6. DECISÕES DA FASE 4 — APROVADAS PELO MESTRE (22/08/2026)

### Promoções (todos os candidatos aprovados)
Os 8 candidatos da seção 2 foram **APROVADOS** como novos templates: Cards de Síntese, Referências Bibliográficas, Imagem Centralizada com Legenda, Bloco de Orientação com Ícone, Linha do Tempo Interativa, Cards de Módulos, Faixa Fluida de Imagens, Caixa de Convite. Celebração de Fechamento entra como sub-bloco dos Cards de Síntese.

### Destino dos componentes sem uso
| Componente | Decisão |
|---|---|
| 1. Botão Primário (CTA) | **RESERVA** (entra no livro, seção Reserva) |
| 5. Galeria de Imagens 2/3 Colunas | **RESERVA** (substituída em uso pela Faixa Fluida) |
| 8. Imagem Clicável (Modal) | **EXCLUIR** |
| 10. Vídeo Centralizado | **EXCLUIR** — mas o template "Vídeo" ganha variante **SEM sinopse** (modelo atual real: vídeo + legenda) |
| 14. Grid de Texto 2 Colunas | **RESERVA** (opção para o autor) |
| 16. Cabeçalho de Módulo (H1) | **EXCLUIR** |

### Nomes simples aprovados
Conforme propostos, com o vídeo dividido em duas variantes: **Vídeo** (vídeo + legenda) e **Vídeo com Sinopse** (vídeo + legenda + caixa).

### Estrutura do novo livro (padrão PSG adaptado)
Layout por template: card branco arredondado com pills (número+nome · etiqueta "não precisa explicitar" quando aplicável · status 🟢 Em uso / 🟡 Reserva), exemplo renderizado, "Onde já foi usado" (dados da auditoria) e "Como pedir no DI".

**Capítulos:**
1. Texto e Destaques (8 templates)
2. Imagens e Vídeos (6 templates)
3. Atividades e Interação (5 templates)
4. Estrutura de Página + Reserva (6 ativos + 3 reserva)

---

## 5. Próximos passos (Fases 4–5)

1. **Fase 4:** mestre decide promoções/rejeições da seção 2 e destino dos componentes sem uso (seção 3)
2. **Fase 5:** reescrita do livro em `docs/templates-galeria/` — categorias propostas:
   - **A. Texto e Destaques** (sinopse, jumbotron, destaque inline, aviso, Template B, para refletir)
   - **B. Imagens e Mídia** (flutuante, centralizada c/ legenda, descrição longa, faixa fluida, vídeo 560px)
   - **C. Atividades e Interação** (H5P c/ e s/ cabeçalho, página final de lição, carrossel, linha do tempo)
   - **D. Estrutura de Página** (apresentação de módulo, objetivo+expectativas, cards de síntese, referências, fórum, label, cards de módulos)
   - **E. Elementos de Sistema** (encerramento mb-0, links externos 6.1, placeholder de imagem) — regras, não templates visuais
3. Atualizar `components-library.md` (renumeração + novos templates) e `.clinerules` N3.2