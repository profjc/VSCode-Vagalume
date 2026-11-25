# Pendências — Módulo 5 — Certificação e Avaliação do curso (Encerramento)

> Arquivo central de pendências do módulo, criado em 22/11/2026 (ciclo 0 — preparação: plano registrado + pendências).
> Atualizado conforme o mestre entrega os recursos ou o Cline conclui cada ciclo.
> **Fonte:** `content/Encerramento/Módulo_V_Versão_para_DI.md` (as linhas referem-se a esse arquivo).
> **Recursos brutos:** `temp/5. Módulo 5/` (rito aprovado em 22/11/2026 — eu solicito, o mestre baixa do SharePoint para a `temp/`).
> **Saídas do módulo:** `templates/pages/Encerramento/` (páginas e atividades — `M5-Apresentacao_do_modulo_5.html`, `Parte1/Licao1..4`, `Parte2/M5P2P1`, `M5P2P2`, `M5P2AT1-Envio_do_Plano_de_Acao`, `Parte3/M5P3P1`, `M5P3AT1-Certificado_de_Conclusao`, `M5P3P2-Ficha_Tecnica`) · `templates/pages/labels/` (labels das Partes 1, 2 e 3) · `assets/images/ilustracoes/Encerramento/` (24 fotos tratadas + `descricoes.md`) · `assets/images/certificados/` (frente e verso do certificado).

> **🔄 DI ATUALIZADO — versão final v2 (24/11/2026, 23:10).** O autor enviou uma **segunda versão** (`temp/5. Módulo 5/Módulo V - Versão para DI - v2.docx`, 114.749 B, 24/11/2026 23:10 — `unzip -t` OK). O `.md` atual passou a vir **desta versão**: `content/Encerramento/Módulo_V_Versão_para_DI.md` (**416 linhas / 36.139 B**). Limpeza **apenas de formatação**: `--` → `—` (11 ocorrências) · 0 `{=html}` · 4 NBSP preservados · **texto do autor intocado (N2.5)** · **conferência byte a byte**: o `.md` é **idêntico** ao bruto do pandoc após a troca dos travessões. A versão de 24/11 16:35 (359 linhas) foi **descartada**. ⚠️ **As linhas citadas nas tabelas abaixo referem-se às versões anteriores** — conferir pelo conteúdo.

## 🟢 STATUS DO MÓDULO — CONCLUÍDO EM CONTEÚDO (25/11/2026)

> **Todos os elementos do DI v2 foram entregues, validados pelo mestre e inseridos no Moodle** — 14 entregas nos ciclos 1–12, mais os ciclos intermediários 7a (label da Parte 2), 8b (Tarefa), 9b (Carta) e 11a (imagens do certificado).
> **Pendência única de produção:** reexecução da **carga horária do curso** (ciclo 13 — §8 do `docs/relatorios/carga-horaria/PLANO-carga-horaria.md`).
> **Pendências administrativas:** **commit + push** das entregas de 25/11 (≈13 arquivos — aguardando autorização do mestre). **Limpeza da `temp/5. Módulo 5/` — ✅ CONCLUÍDA (25/11/2026)** (ver seção de auditoria abaixo).
> **Correção de estrutura (mestre, 25/11/2026):** a Parte 2 e a Parte 3 têm **PÁGINAS HTML**, não "lições" — os arquivos **não usam `Licao` no caminho**: `Parte2/M5P2P1.html`, `Parte2/M5P2P2.html`, `Parte2/M5P2AT1-Envio_do_Plano_de_Acao.html`, `Parte3/M5P3P1.html`, `Parte3/M5P3AT1-Certificado_de_Conclusao.html`, `Parte3/M5P3P2-Ficha_Tecnica.html`. As Lições 1–4 da Parte 1 continuam **lições** (como no DI).

## 🔍 Auditoria de fechamento do módulo (25/11/2026) — 14/14 APROVADAS

> **Método:** auditoria página a página contra o `docs/checklist-entrega.md` completo (estrutura/segurança, higienização, identidade visual, acessibilidade, flutuação, funcionamento no Moodle) + verificações por terminal (tags balanceadas, 0 proibidos, travessões, `|`, hífens visíveis, `aria-hidden`, `sr-only`, placeholders). Precedente: revisão do Módulo 4 (22–23/10/2026).
>
> **Resultado:** **14 de 14 entregas aprovadas, sem erro bloqueante.** Global: 0 `<style>/<link>/<script>/onclick/@@PLUGINFILE@@/fa-solid/data:image/<html>/<body>` · 0 en dash (`–`) · 0 pipe (`|`) · 0 links `<a>` (tudo embedado/anexado — correto) · `aria-hidden` em **todos** os ícones · `sr-only` só em `<p>` · hierarquia de headings sem saltos · `mb-0` no último elemento em todas · fotos com `width`/`height`/`loading="lazy"` e alturas conferindo com o `identify` de 24/11 (21×853 + 855 + 960 + 720).
>
> **Observações registradas:** (1) hífen `-` no **título oficial do vídeo** da Carta (oEmbed: "Vaga Lume 25 anos - Ler o mundo, ler todo mundo") — **mantido por fidelidade ao título do YouTube**, não é resíduo de conversão (decisão do mestre: nenhuma página precisa de edição); (2) **Área de Upload Temporária removida** das 4 lições na limpeza de 25/11 (ver abaixo); (3) 3 arquivos sem newline final — cosmético, sem efeito.
>
> **Limpeza das áreas de upload (25/11/2026, ordem do mestre):** removidos os blocos `INÍCIO/FIM DA ÁREA DE UPLOAD TEMPORÁRIA` (card tracejado + 6 linhas de upload) das 4 lições — as páginas ficaram com **6 blocos temporários por slide** (mantidos, como nos demais módulos) e 6 `[cole a imagem aqui]`. Tamanhos: L1 **22.010 B** (div 54/54, p 26/26) · L2 **20.711 B** (53/53, 25/25) · L3 **21.642 B** (53/53, 25/25) · L4 **21.511 B** (53/53, 25/25); `img` 12, `i` 10/10, `span` 6/6, `figure` 6/6, `button` 16/16 em todas.



## 🔄 Alterações da versão v2 (24/11/2026, 23:10) — aprovadas pelo mestre

> **Contexto:** as linhas **1–234 são idênticas** às da versão anterior — **nenhuma alteração nas páginas já entregues e validadas** (Apresentação + Lições 1–4 "Recordar é viver"). Todas as mudanças estão na reta final do módulo.

| # | Onde | Antes (16:35) | Agora (v2) | Avaliação do DI |
|---|---|---|---|---|
| 1 | Delimitadores | Resíduos quebrados: `[CARD LIÇÃO 2]` / `[CARD LIÇÃO 3]` / `INICIODA LIÇÃO 1` / `FIM DA LIÇÃO 1` | `[Parte II - Avaliação final]` · `[Página html 1]`…`[/Página html 1]` (Avaliação) · `[Página html 2]`…`[/Página html 2]` (Plano de Ação) · `[/Parte 2]` · `[Parte 3]` · `[Página html ]` · `[/Parte 3]` | ✅ concordo — arquitetura explícita; normalizar "Parte II" → **"Parte 2"** (decimal, decisão de 22/11) |
| 2 | **Plano de Ação** | Passos de entrega (Baixe → Imprima → Preencha → Foto → Envie + WhatsApp) **dentro da página** | Bloco próprio **`[Tarefa de entrega do Moodle]`…`[/Tarefa de entrega]`** — **Tarefa (Assignment) do Moodle separada** | ✅ **concordo — mudança mais valiosa**: a entrega vira atividade rastreável (essencial para a certificação, como a "Dica 2" do autor aponta) e separa instrução (página) de ação (atividade) |
| 3 | Carta | "Atividade: Carta ao cursista", dentro da página "Antes de sair" | **Página própria "Carta ao cursista"** (o título "Antes de sair" saiu) · conteúdo idêntico, vídeo `2tqEMOjbeq0` incluído | ✅ concordo — carta é conteúdo de fechamento, não atividade |
| 4 | Certificado | "Página: certificado" | **"[Atividade: certificado]"** (link do modelo mantido) | ✅ concordo — é atividade no Moodle (**`mod_customcert` já instalado e configurado pelo mestre**) |
| 5 | Ficha Técnica | Só o placeholder "Verificar onde inserir" | **Conteúdo completo inline**: Equipe Vaga Lume (Gestão · Coordenação e lideranças · Equipe de Educadores) + créditos (Concepção · Conteudistas · Projeto gráfico · Revisão e Validação · **Designer instrucional e plataforma: Professor J.C. / AGIR**) — a marca ~~Verificar onde inserir~~ segue riscada | ✅ concordo — resolve a pendência que estava para o ciclo 9 |

> **Pontos de atenção registrados:** (a) **"Parte II" (romano) × "Parte 3" (arábico)** → normalizar para decimal; (b) **`[Página html ]` sem número** na Carta (cosmético, sem impacto); (c) **"Dica 2" do Plano de Ação com gramática quebrada** ("Não se esqueça que será certificado as pessoas que junto com o envio do plano de ação, finalizaram seu percurso. Garante a finalização de seu percurso, mas motive as pessoas que façam o mesmo.") → **correção será sugerida no ciclo 8 e validada pelo mestre com o autor**; (d) o **título "Antes de sair"** desapareceu do DI (a página passa a se chamar "Carta ao cursista") — confirmar no ciclo 9.

## 🔄 Alterações da versão de 24/11/2026 (16:35) do DI

| # | Local | Alteração | Efeito no projeto |
|---|---|---|---|
| 1 | Apresentação — 3ª expectativa (l. 31) | "vínculos **a** primeira infância" → "vínculos **com** a primeira infância" | ✅ já aplicado no HTML do ciclo 1 (correção autorizada em 22/11) — agora oficializada pelo autor |
| 2 | Lição 1 — box de destaque (l. 49) | Texto **reescrito** (novo texto sobre as fotografias do trabalho da Vaga Lume) | usar o texto novo no ciclo 3 |
| 3 | Lição 1 — slide 1 (l. 53-80) | **`[Novo Formato]`** do carrossel: `[Original]` preservado + `[Imagem: Foto 1]` + `[Legenda]` (título + texto) + **`[Botão: Saiba mais sobre essa imagem]`** com a identificação da foto | **decisão do mestre (24/11): o novo formato vale para TODAS as lições com carrossel, em TODOS os 6 slides** — o DI traz o modelo só no primeiro |
| 4 | Legendas de fotos (L1–L4) | Limpeza: sai o sufixo ", sem comunidade identificada" (maioria) e o ".jpg" residual; na L1/L2 a identificação aparece **sublinhada** (`<span class="underline">`) | legendas/descrições do ciclo 3 em diante seguem o DI novo |
| 5 | Lição 5 — Avaliação (l. 249-251) | Acrescentado o **embed iframe do Microsoft Forms** (640×480) além do link | decidir no ciclo 7 (embed por padrão — `docs/rotina-entrega.md` §5 item 12) |
| 6 | Lição 6 — Plano de ação (l. 305-325) | Roteiro reescrito/reordenado (Baixe → Imprima → Preencha + "Atenção" → Tire uma foto → Envie a foto → WhatsApp como parágrafo final). ⚠️ **numeração quebrada no original (1, 3, 5, 4, 6)** | decidir no ciclo 8 (normalizar a sequência?); texto do autor intocado |
| 7 | Lição 7 — Antes de sair (l. 333+) | Nova instrução `[Carta: Formatar como carta]` (fecha com `[/Carta]` após "Parabéns pela finalização deste curso!") · aspas curvas no provérbio · **"Página: certificado"** substitui "Criar Botão para gerar certificado" · **"Página: Ficha Técnica"** substitui "Ficha Técnica" | ciclos 9 e seguintes (certificado e Ficha Técnica) |
| 8 | Delimitadores | `> INÍCIO/FIM DA LIÇÃO N` mantidos como na versão anterior (typos de numeração permanecem) · link malformado do ponto 3 da L1 **preservado como está** | sem ação (texto do autor) |

## ✅ Verificações concluídas (22/11/2026)

### Links externos (5 — recursos do módulo)

| # | Link | Local no DI | Situação |
|---|---|---|---|
| 1 | Formulário de avaliação — `https://forms.cloud.microsoft/r/28bAEX1fGN` | Lição 5 — Avaliação do curso | ✅ válido (Microsoft Forms) — **a versão de 24/11 do DI acrescentou o embed iframe** (640×480) além do link |
| 2 | Vídeo dos 25 anos da Vaga Lume — `https://www.youtube.com/watch?v=2tqEMOjbeq0&t=2s` | Lição 7 — Carta ao cursista | ✅ embedável (oEmbed: título/canal a conferir no ciclo 9; duração entra na carga horária) |
| 3 | `Plano de Ação_Curso Bibliotecas Comunitárias_Espaços da primeira infância.pdf` | Parte 2 — Tarefa "Atividade: Envio do Plano de Ação" | ✅ **RESOLVIDO (25/11/2026):** o PDF é **anexado à Tarefa** do Moodle; o HTML da descrição **não tem link de download** (decisão do mestre — `M5P2AT1-Envio_do_Plano_de_Acao.html`) |
| 4 | Modelo de certificado (pasta SharePoint "8. Certificação e Avaliação") | Parte 3 — "Certificado de Conclusão" | ✅ **RESOLVIDO (25/11/2026):** frente/verso preparados como **fundos do `mod_customcert`** — `assets/images/certificados/certificado-conclusao-frente.png` e `-verso.png` (1999×1434, **sem redimensionar/re-encodar**, para não degradar a impressão) |
| 5 | Ficha Técnica (`.docx` no SharePoint) | Parte 3 — página "Ficha Técnica" | ✅ **RESOLVIDO (25/11/2026):** o **DI v2 traz o conteúdo inline** (equipe + créditos) — página própria criada (`M5P3P2-Ficha_Tecnica.html`); o `.docx` **não foi necessário** |

### Recursos em `temp/5. Módulo 5/` (29 arquivos — DI + 4 do certificado + PDF do plano + Ficha Técnica + 24 fotos)

| Recurso | Uso previsto | Situação |
|---|---|---|
| `Módulo V - Versão para DI - v2.docx` (114.749 B — 24/11/2026, 23:10) | **DI vigente** do módulo | ✅ convertido em `content/Encerramento/Módulo_V_Versão_para_DI.md` (**416 linhas / 36.139 B**) e **movido para `content/Encerramento/`** (limpeza de 25/11/2026) |
| `Módulo V - Versão para DI.docx` (111.185 B) | DI anterior (24/11, 16:35) | ✅ histórico — superado pela v2; **excluído na limpeza da `temp/` (25/11/2026)** |
| `Certificado..._Modelo PDF.pdf` · `_Modelo JPG.jpg` · `_Modelo JPG_Pagina 1.png` · `_Modelo JPG_Pagina 2.png` | Modelo do certificado | ✅ **usados** — págs. 1 e 2 copiadas para `assets/images/certificados/` (frente/verso); **modelos excluídos na limpeza da `temp/` (25/11/2026)** |
| `Plano de Ação_Curso Bibliotecas Comunitárias...pdf` | Tarefa "Atividade: Envio do Plano de Ação" | ✅ **anexado à Tarefa** no Moodle (ciclo 8b) e **movido para `assets/pdf/Encerramento/Plano_de_Acao_Curso_Bibliotecas_Comunitarias.pdf`** |
| `Ficha Técnica.docx` | Referência da página "Ficha Técnica" | ✅ **dispensado** (conteúdo inline no DI v2) e **movido para `content/Encerramento/Ficha Técnica.docx`** |
| `Fotos/` — 24 arquivos (6 por lição, L1–L4) | Slides dos carrosséis das Lições 1–4 | ✅ **24/24 tratadas** para `assets/images/ilustracoes/Encerramento/` (1280 px, `-strip -quality 85`); **originais excluídos na limpeza da `temp/` (25/11/2026)** |

> **Limpeza da `temp/5. Módulo 5/` — ✅ CONCLUÍDA (25/11/2026), ordem do mestre:** documentos do autor **preservados em `content/Encerramento/`** (DI v2 + Ficha Técnica), PDF do Plano **movido para `assets/pdf/Encerramento/`**, imagens tratadas em `assets/images/`; **excluídos** o DI v1 (superado), os 4 arquivos do modelo do certificado e as 24 fotos originais. **A pasta `temp/` ficou completamente vazia** (0 arquivos, sem subpastas).

## 🟡 Pendências do mestre (recursos e Moodle)

### 1. Fotos dos carrosséis — 24 no total ✅ **TODAS NA `temp/` (24/11/2026)**

> **Rito:** eu solicito por lição, no ciclo correspondente; o mestre baixa do SharePoint (links no DI) para `temp/`; eu trato para `assets/images/ilustracoes/Encerramento/` e monto os slides.
> **Formato desejado:** **JPEG ou PNG originais** (nunca WebP), nome de arquivo preservado do SharePoint quando possível.
> **✅ Situação (24/11/2026):** as **24 fotos chegaram**, organizadas por lição em `temp/5. Módulo 5/Fotos/` — **6 por lição** (L1 a L4), todas JPEG de alta resolução (3,0 a 21,8 MB; 3600×2400 a 6720×4480). A antiga pasta `Modulo V - Certificação e Validação do Curso/Lição 1 ...` não existe mais (a Foto 4 agora está em `Fotos/Lição 1 .../Foto 4.jpg`). **Bloqueio do ciclo 3 liberado.**
> **Pastas e nomes:** `Lição 1 - Recordar é viver Módulo I Primeira infância/` (Foto 1–6) · `Lição 2 -  Recordar é viver Módulo II Leitura e primeira infância/` (Foto 1–6) · `Lição 3 - Recordar é viver Módulo III/` (Foto 1, Foto2, Foto3, Foto4, Foto 5, Foto 6 — nomes sem espaço variável) · `Lição 4 - Recordar é viver Módulo IV Mãos na Massa! (ou nos livros!)/` (Foto 1–6).


**Lição 1 — "Recordar é viver: Módulo I Primeira infância"** (ciclo 3) — ✅ **6/6 na `temp/`** · nomes/linhas da **versão de 24/11** do DI:

| # | Legenda no DI (versão 24/11) | Linha do DI | Arquivo na `temp/` |
|---|---|---|---|
| 1 | Foto 1 - Implementação de Bibliotecas em Benevides (PA), | l. 57 | `Fotos/Lição 1 .../Foto 1.jpg` |
| 2 | Foto 2 - Implementação de Biblioteca em Uarini (AM) | l. 84 | `Foto 2.jpg` |
| 3 | Foto 3 - Implementação de Bibliotecas em Benevides (PA) *(link malformado preservado — A1)* | l. 89 | `Foto 3.jpg` |
| 4 | Foto 4 - Implementação em Novo Airão (AM) | l. 94 | `Foto 4.jpg` |
| 5 | Foto 5 - Implementação de Bibliotecas em Uarini (AM) | l. 99 | `Foto 5.jpg` |
| 6 | Foto 6 - Implementação de Bibliotecas em Benevides (PA) | l. 104 | `Foto 6.jpg` |

**Lição 2 — "Recordar é viver: Módulo II Leitura e primeira infância"** (ciclo 4) — ✅ **6/6 na `temp/`** (linhas abaixo = versão 22/11; conferir pelo conteúdo):

| # | Nome no DI | Linha do DI |
|---|---|---|
| 1 | Foto 1 - Embelezamento em Menino Deus (Rio Anapú), Portel (Pará) | l. 95 |
| 2 | Foto 2 - Embelezamento em Menino Deus (Rio Anapú), Portel (Pará).jpg | l. 100 |
| 3 | Foto 3 - Implementação de Bibliotecas em Uarini (AM) - 2025 | l. 105 |
| 4 | Foto 4 - Implementação em Novo Airão (AM), sem comunidade indentificada | l. 110 |
| 5 | Foto 5 - Implementação em Novo Airão (AM), sem comunidade identificada | l. 115 |
| 6 | Foto 6 - Implementação de Bibliotecas em Uarini (AM) - 2025 | l. 120 |

**Lição 3 — "Recordar é viver: Módulo III Bibliotecas Comunitárias e Primeira Infância"** (ciclo 5) — ✅ **6/6 na `temp/`** (linhas abaixo = versão 22/11; conferir pelo conteúdo):

| # | Nome no DI | Linha do DI |
|---|---|---|
| 1 | Foto 1 - Construção Sede em São Sebastião, Portel (PA) - 2023 | l. 137 |
| 2 | Foto 2 - Oficina de Livros Artesanais em Uarini | l. 142 |
| 3 | Foto 3 - Oficina de Livros Artesanais em Uarini | l. 147 |
| 4 | Foto 4 - Implementação de Bibliotecas em Graça a Deus, Castanhal (PA) - 2023 | l. 152 |
| 5 | Foto 5 - Oficina de Livros Artesanais em Uarini - 2023 | l. 157 |
| 6 | Foto 6 - Implementação de Bibliotecas em Benevides (PA) - 2026 | l. 162 |

**Lição 4 — "Recordar é viver: Módulo IV Mãos na Massa! (ou nos livros!)"** (ciclo 6) — ✅ **6/6 na `temp/`** (linhas abaixo = versão 22/11; conferir pelo conteúdo):

| # | Nome no DI | Linha do DI |
|---|---|---|
| 1 | Foto 1 - implantação em novo airão AM | l. 179 |
| 2 | Foto 2 - implantação em novo airão AM | l. 184 |
| 3 | Foto 3 - Implementação de Bibliotecas Santarém (PA) - 2023 | l. 189 |
| 4 | Foto 4 - Formação em Uarini (AM), Comunidade Porto Braga | l. 194 |
| 5 | Foto 5 - Embelezamento em Corre Água, Macapá (AP) - 2024 | l. 200 |
| 6 | Foto 6 - Oficina de Livros Artesanais em Uarini - 2023 | l. 206 |

### 2. Upload do PDF do Plano de Ação no Moodle — ✅ **RESOLVIDO (25/11/2026)**

> O PDF virou **anexo da Tarefa "Atividade: Envio do Plano de Ação"** (decisão do mestre: a Tarefa é atividade do Moodle e o HTML traz **apenas as instruções** — sem link de download). Arquivo: `templates/pages/Encerramento/Parte2/M5P2AT1-Envio_do_Plano_de_Acao.html`.

### 3. Botão para gerar o certificado — ✅ **RESOLVIDO (25/11/2026)**

> O certificado é atividade do **`mod_customcert`** (já instalado, configurado pelo mestre). O Cline produziu só o **texto da página** (`M5P3AT1-Certificado_de_Conclusao.html`, aprovado) e as **imagens de fundo** (frente/verso). Título no Moodle: **"Certificado de Conclusão"** (sem a palavra "Atividade").

### 4. Ficha Técnica — ✅ **RESOLVIDO (25/11/2026)**

> Página própria **"Ficha Técnica"** (`M5P3P2-Ficha_Tecnica.html`), com o conteúdo completo inline do DI v2 (4 cards: Gestão · Coordenação e lideranças · Equipe de Educadores · Créditos). O `.docx` da `temp/` não foi necessário.

## 🔴 Pendências do autor (DI)

| # | Item | Local no DI | Situação |
|---|---|---|---|
| A1 | **Links de foto ausentes/malformados** na Lição 1: Foto 1 e Foto 2 sem hyperlink; Foto 3 com link cujo alvo é texto (`[Foto:](https://Foto 3 - ...)`) | l. 55, 60 e 65 | ✅ **RESOLVIDO (24/11/2026):** as 6 fotos foram entregues pelo mestre em `temp/5. Módulo 5/Fotos/Lição 1 ...` e os slides usam as legendas do DI v2 (ciclo 3) — o link malformado não teve efeito |
| A2 | **Fotos possivelmente repetidas**: Lição 2 — Fotos 3 e 6 com o mesmo nome (Uarini, 2025); Lição 3 — Fotos 2, 3 e 5 com o mesmo nome (Oficina de Livros Artesanais em Uarini); Lição 4 — Fotos 1 e 2 com o mesmo nome | l. 105/120 · 142/147/157 · 179/184 | ✅ **RESOLVIDO (24/11/2026):** leitura visual confirmou, nas três lições, que são **imagens distintas** — legendas repetidas permanecem, por decisão do mestre (ver `descricoes.md`) |
| A3 | **Numeração inconsistente dos cards**: "CARD LIÇÃO 2" e "CARD LIÇÃO 3" usados duas vezes; "INICIODA LIÇÃO 1" (sem espaço) e "FIM DA LIÇÃO 1" após a Lição 4 | l. 211, 215, 229, 295 e 209 | ✅ resolvido por decisão do mestre (22/11/2026): **renumerar no padrão dos módulos anteriores** (Lições 1 a 7) — texto do autor intocado |
| A4 | **Pasta do SharePoint da Lição 3** grafa "Primeira Infâncias" (plural) | l. 137–162 (URLs) | ℹ️ informativo — sem ação |

## 🟢 Decisões fechadas (mestre, 22/11/2026)

| # | Decisão |
|---|---|
| 1 | **Título do card no Moodle:** "Certificação e Avaliação do curso" (o typo "Avalaiação" foi só na mensagem) — comentários das páginas espelham esse título |
| 2 | **Numeração das lições:** padrão dos módulos anteriores — sequencial de **1 a 7** (1–4 Recordar · 5 Avaliação · 6 Plano de ação · 7 Antes de sair); correções no DI são de responsabilidade do Cline |
| 3 | **Elementos completos:** criar todas as páginas **e o label da Parte 1** |
| 4 | **Padrões:** prefixos (`M5`), pastas (`Encerramento/`), documentação e comentários seguem os módulos anteriores — mesmo o módulo se parecendo com Boas-vindas |
| 5 | **Fotos:** o Cline solicita; o mestre baixa do SharePoint e coloca na `temp/` |
| 6 | **Grafia (22/11/2026, na entrega da Apresentação):** "primeira infância" → "**Primeira Infância**" quando as demais ocorrências do DI usam maiúscula; e incluir o "**com**" em "fortalecimento dos vínculos **com** a Primeira Infância" (3ª expectativa) |
| 7 | **Novo formato de carrossel (24/11/2026):** o `[Novo Formato]` do DI (imagem + legenda com título e texto + botão "Saiba mais sobre essa imagem" com a identificação da foto) deve ser aplicado em **todas as lições com carrossel** e em **todos os 6 slides** — o DI traz o modelo apenas no primeiro slide da Lição 1 |
| 8 | **DI de 24/11/2026 (24/11/2026):** descartar a versão anterior do `.md` e trabalhar sobre a nova conversão (`content/Encerramento/Módulo_V_Versão_para_DI.md`, 359 linhas) |
| 9 | **DI v2 (24/11/2026, 23:10) — aprovado pelo mestre:** o `.md` passa a vir da **v2** (416 linhas / 36.139 B); as 5 mudanças estruturais (partes explícitas, Tarefa de entrega, Carta como página, certificado como atividade, Ficha Técnica inline) estão **aprovadas** |
| 10 | **Certificado (24/11/2026):** o plugin **`mod_customcert` já está instalado e o certificado já está pronto no Moodle** — o botão de download **é gerado pelo plugin** (não entra no HTML). O Cline produz apenas **o texto da página que acompanha o botão** — texto será **proposto pelo Cline e validado pelo mestre** (ciclo 10) |
| 11 | **"Dica 2" do Plano de Ação (24/11/2026):** o trecho com gramática quebrada fica **como está** por ora; o Cline **sugere a correção no ciclo 8** e o mestre valida com o autor antes de aplicar |
| 12 | **Labels das Partes 2 e 3 (24/11/2026):** os labels das novas partes serão criados; proposta de texto — **"Parte 2 — Avaliação final e Plano de Ação"** e **"Parte 3 — Finalização do curso"** (sujeita a validação do mestre/redação do autor) |
| 13 | **Numeração das lições REINICIA em cada Parte (regra do mestre, 24/11/2026)** — **substitui a decisão 2 (sequencial 1–7) para as Partes 2 e 3:** **Parte 2** → **Lição 1** (Avaliação do curso, `M5P2L1p1`) e **Lição 2** (Plano de ação, `M5P2L2p1`, + Tarefa de entrega); **Parte 3** → **Lição 1** (Carta ao cursista, `M5P3L1p1`) com as páginas seguintes da mesma lição — certificado (`M5P3L1p2`) e Ficha Técnica (`M5P3L1p3`). Parte 1 (Lições 1–4, já entregues) não muda | ⚠️ **PARCIALMENTE SUBSTITUÍDA pela decisão 14** |
| 14 | **As Partes 2 e 3 têm PÁGINAS HTML, não lições (mestre, 25/11/2026)** — delimitadores do DI v2 (`[Página html 1]`, `[Página html 2]`); arquivos sem `Licao` no caminho (`Parte2/M5P2P1.html`, `M5P2P2.html`, `M5P2AT1-…`; `Parte3/M5P3P1.html`, `M5P3AT1-…`, `M5P3P2-…`) e comentários sem "Lição". **As Lições 1–4 da Parte 1 continuam lições** | ✅ aplicada nos ciclos 7b–12 |
| 15 | **Label vem ANTES do conteúdo** em cada Parte (ordem do mestre, 25/11/2026): label da Parte 2 → Página 1 → Página 2 → Tarefa; label da Parte 3 → Carta → Certificado → Ficha Técnica | ✅ aplicada nos ciclos 7a e 9 |
| 16 | **Títulos dos labels aprovados:** Parte 2 — **"Avaliação final e Plano de Ação"** · Parte 3 — **"Finalização do curso"** | ✅ entregues e inseridos no Moodle (25/11/2026) |
| 17 | **Certificado:** título no Moodle **"Certificado de Conclusão"** (sem a palavra "Atividade"; ordem do mestre, 25/11/2026) · texto da página **proposto pelo Cline e aprovado** · botão é do `mod_customcert` · fundos: **frente e verso** (`assets/images/certificados/`, 1999×1434, sem redimensionar/re-encodar) | ✅ entregue, aprovado e inserido (25/11/2026) |
| 18 | **"Dica 2" do Plano de ação:** correção sugerida pelo Cline e **APROVADA pelo mestre** (25/11/2026) — "Se você optou por realizar a construção coletivamente, não esqueça de que serão certificadas as pessoas que, junto com o envio do plano de ação, finalizarem o seu percurso..." | ✅ aplicada no ciclo 8 |
| 19 | **Carta ao cursista:** formato **"folha de carta"** (card branco com borda bege, ornamento `fa-envelope-open-text`) e **vídeo DENTRO da carta**, após o parágrafo que o cita · legenda com **minutagem obrigatória** — `(02min53s); canal: Vaga Lume` (informada pelo mestre; o DI não trazia) | ✅ aprovada (25/11/2026) |

## 🗺️ Panorama do módulo (mapa REAL de páginas/atividades — estrutura v2 fechada em 25/11/2026)

| Ordem | Parte | Elemento no Moodle | Arquivo |
|---|---|---|---|
| 1 | — | Apresentação do Módulo 5 | `templates/pages/Encerramento/M5-Apresentacao_do_modulo_5.html` |
| 2 | Parte 1 | Label — Revisitando os módulos do curso e as aprendizagens adquiridas | `templates/pages/labels/M5_Label_Parte1_Revisitando_os_modulos_do_curso_e_as_aprendizagens_adquiridas.html` |
| 3 | Parte 1 | Lição 1 — Recordar é viver: Módulo 1 — Primeira Infância | `.../Parte1/Licao1/M5P1L1p1.html` |
| 4 | Parte 1 | Lição 2 — Recordar é viver: Módulo 2 — Leitura e Primeira Infância | `.../Parte1/Licao2/M5P1L2p1.html` |
| 5 | Parte 1 | Lição 3 — Recordar é viver: Módulo 3 — Bibliotecas Comunitárias e Primeira Infância | `.../Parte1/Licao3/M5P1L3p1.html` |
| 6 | Parte 1 | Lição 4 — Recordar é viver: Módulo 4 — Mãos na Massa! (ou nos livros!) | `.../Parte1/Licao4/M5P1L4p1.html` |
| 7 | **Parte 2** | Label — Avaliação final e Plano de Ação | `templates/pages/labels/M5_Label_Parte2_Avaliacao_final_e_Plano_de_Acao.html` |
| 8 | **Parte 2** | Página 1 — Avaliação do curso (Forms embedado) | `.../Parte2/M5P2P1.html` |
| 9 | **Parte 2** | Página 2 — Plano de ação | `.../Parte2/M5P2P2.html` |
| 10 | **Parte 2** | Tarefa — Atividade: Envio do Plano de Ação | `.../Parte2/M5P2AT1-Envio_do_Plano_de_Acao.html` |
| 11 | **Parte 3** | Label — Finalização do curso | `templates/pages/labels/M5_Label_Parte3_Finalizacao_do_curso.html` |
| 12 | **Parte 3** | Página 1 — Carta ao cursista | `.../Parte3/M5P3P1.html` |
| 13 | **Parte 3** | Certificado de Conclusão (atividade `mod_customcert` + fundos) | `.../Parte3/M5P3AT1-Certificado_de_Conclusao.html` |
| 14 | **Parte 3** | Página 2 — Ficha Técnica | `.../Parte3/M5P3P2-Ficha_Tecnica.html` |

> **Sem H5P e sem Sequências Didáticas** neste módulo (logo, sem PDFs de SD). **Sem botões de navegação nas páginas HTML** (só lições têm "Anterior/Próximo/Finalizar" — ver `.clinerules` N3.5.1, correção de 25/11/2026).

## 📊 Progresso dos ciclos

| Ciclo | Entrega | Status |
|---|---|---|
| 0 | Plano registrado + este arquivo de pendências | ✅ 22/11/2026 |
| 1 | Apresentação do Módulo 5 (`M5-Apresentacao_do_modulo_5.html`) — **validada e inserida no Moodle (22/11/2026)** | ✅ 22/11/2026 |
| 2 | Label da Parte 1 (`M5_Label_Parte1_...`) — **validado e inserido no Moodle (22/11/2026)** | ✅ 22/11/2026 |
| 3 | Lição 1 — `templates/pages/Encerramento/Parte1/Licao1/M5P1L1p1.html` — 6 fotos tratadas + 6 descrições longas aprovadas uma a uma + carrossel no novo formato + **área de upload temporária** (padrão novo firmado) — **validada e inserida no Moodle (24/11/2026)** | ✅ 24/11/2026 |
| 4 | Lição 2 — `templates/pages/Encerramento/Parte1/Licao2/M5P1L2p1.html` — 6 fotos tratadas + 6 descrições aprovadas + carrossel no novo formato + área de upload temporária — **validada e inserida no Moodle (24/11/2026)** com navegação "Finalizar" | ✅ 24/11/2026 |
| 5 | Lição 3 — `templates/pages/Encerramento/Parte1/Licao3/M5P1L3p1.html` — 6 fotos tratadas + 6 descrições aprovadas + carrossel no novo formato + área de upload temporária — **validada e inserida no Moodle (24/11/2026)** | ✅ 24/11/2026 |
| 6 | Lição 4 — `templates/pages/Encerramento/Parte1/Licao4/M5P1L4p1.html` — 6 fotos tratadas (proporções próprias nas Fotos 4 e 5) + 6 descrições aprovadas + carrossel no novo formato + área de upload temporária (aviso das Fotos 1 e 2) — **validada e inserida no Moodle (24/11/2026)** com navegação "Finalizar" | ✅ 24/11/2026 |
| 7a | Label da Parte 2 (`M5_Label_Parte2_Avaliacao_final_e_Plano_de_Acao.html`) — "Parte 2 · Avaliação final e Plano de Ação" — **validado e inserido no Moodle (25/11/2026)** | ✅ 25/11/2026 |
| 7b | Página 1 — Avaliação do curso (`.../Parte2/M5P2P1.html`) — faixa de título com ícone, 2 parágrafos em destaque, Forms **embedado** (sem link) — **validada e inserida (25/11/2026)** | ✅ 25/11/2026 |
| 8 | Página 2 — Plano de ação (`.../Parte2/M5P2P2.html`) — sem título no corpo, 2 seções em cards, **Dica 2 corrigida** — **validada e inserida (25/11/2026)** | ✅ 25/11/2026 |
| 8b | Tarefa **"Atividade: Envio do Plano de Ação"** (`M5P2AT1-Envio_do_Plano_de_Acao.html`) — apenas instruções, **PDF anexado** à atividade — **validada e inserida (25/11/2026)** | ✅ 25/11/2026 |
| 9 | Label da Parte 3 (`M5_Label_Parte3_Finalizacao_do_curso.html`) — "Parte 3 · Finalização do curso" — **validado e inserido (25/11/2026)** | ✅ 25/11/2026 |
| 9b | Página 1 — Carta ao cursista (`.../Parte3/M5P3P1.html`) — folha de carta + vídeo `2tqEMOjbeq0` **(02min53s)** — **aprovada (25/11/2026)** | ✅ 25/11/2026 |
| 10 + 11a | **Certificado de Conclusão** (`.../Parte3/M5P3AT1-Certificado_de_Conclusao.html`) + fundos frente/verso em `assets/images/certificados/` — **aprovado (25/11/2026)** | ✅ 25/11/2026 |
| 12 | Página 2 — Ficha Técnica (`.../Parte3/M5P3P2-Ficha_Tecnica.html`) — 4 cards (incluindo Créditos) — **aprovada (25/11/2026)** | ✅ 25/11/2026 |
| 13 | **Carga horária do curso** — reexecução pela skill `metricas-carga-horaria` (§8 do `PLANO-carga-horaria.md`) | ⏳ **ÚNICA PENDÊNCIA DE PRODUÇÃO** |
