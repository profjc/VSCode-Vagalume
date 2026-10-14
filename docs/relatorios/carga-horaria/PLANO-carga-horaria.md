<!-- ╔══════════════════════════════════════════════════════════════════════════╗ -->
<!-- ║  PLANO DE ESTIMATIVA DE CARGA HORÁRIA — DOCUMENTO VIVO                  ║ -->
<!-- ║  Criado em 14/10/2026 (Ciclo 0) · Projeto Vaga Lume (Moodle 4.5)        ║ -->
<!-- ║  Reexecutável: quando o Módulo de Encerramento chegar (§8)              ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════════╝ -->

# 📊 Plano — Estimativa de Carga Horária Efetiva do Curso

> **O que é:** plano de trabalho e registro de método para produzir o **relatório de carga horária efetiva** do curso, com base nos módulos já produzidos e validados no Moodle.
> **Status:** em execução por ciclos — **Ciclo 0 concluído em 14/10/2026** (plano salvo + registro no checkpoint + git).
> **Documento vivo:** atualizar a cada ciclo e **reexecutar** quando o Módulo de Encerramento (Certificação e Avaliação) for produzido — ver §8.

---

## §1 — Objetivo e natureza do documento

- **Objetivo:** produzir um **relatório imprimível** (PDF A4 com identidade Vaga Lume **+ DOCX** editável) com a **carga horária efetiva** do curso, detalhada por **categoria de recurso** (quantidade + tempo total) e por **módulo**.
- **Categorias exigidas pelo mestre:** (1) ler textos; (2) observar e analisar imagens; (3) assistir vídeos; (4) fazer as atividades; (5) consultar a bibliografia; (6) navegar pela plataforma; (7) participar dos fóruns. Acrescentadas pelo inventário: (8) encontros síncronos; (9) Sequências Didáticas (PDFs); (10) navegação estrutural (labels/frontpage).
- **Natureza:** **ESTIMATIVA, não medição.** O mestre confirmou (14/10/2026) que **não há relatórios de conclusão/duração do Moodle**. Portanto:
  - **inventário (quantidades) = exato**, rastreável até o arquivo de origem;
  - **tempo = parâmetros** validados pelo mestre (§4), aplicados por recurso;
  - resultado apresentado em **três cenários** (mínimo · **referência** · máximo) + **recomendado**.
- **Separação obrigatória:** **carga obrigatória** × **carga opcional/complementar** (§2), para proteger o número principal.

## §2 — Escopo

| Situação | Material | Entra na conta? |
|---|---|---|
| **No ar e validado no Moodle** | M0 Boas-vindas + M1 + M2 + M3 + M4 (**146 páginas**) | **SIM** |
| **No ar** | Página dos **Encontros Síncronos** (2 encontros com gravação, card e minutagem) | **SIM** |
| **Previsto — computado como executado** (decisão do mestre, 14/10/2026) | **3º Encontro Síncrono (1h30)** + **novo bloco (texto + imagem + vídeo)** a inserir na página dos Encontros | **SIM** |
| **Não produzido** | **Módulo de Encerramento** (Certificação e Avaliação do curso) — única pendência aberta do projeto | **NÃO** — entra como nota e é incorporado na reexecução (§8) |

**Buckets do relatório:**

- **A — Carga obrigatória:** leitura das páginas · imagens · vídeos de conteúdo · atividades H5P · fóruns · navegação · encontros síncronos (participação) · bloco novo dos encontros.
- **B — Carga opcional/complementar:** referências bibliográficas (38 itens, sendo 21 vídeos) · PDFs das Sequências Didáticas (13) · gravações dos encontros síncronos (3h06).
- **Notas obrigatórias do relatório:** (i) Módulo de Encerramento fora do escopo; (ii) **sobreposição** entre vídeos da bibliografia (bucket B) e vídeos já contados no conteúdo (bucket A) — evitar dupla contagem; (iii) tempo de fórum considera o ciclo completo exigido (ler · postar · ler os colegas · **responder a dois**).

## §3 — Decisões do mestre (14/10/2026)

| # | Questão | Decisão |
|---|---|---|
| 1 | Âncora das “24 horas” do DI do M1 | Refere-se ao **curso todo**, mas é tratada como **provavelmente desatualizada** (DI de ago/2026; o curso hoje tem 4 módulos + Encerramento) — usada apenas como **comparação de sanidade**, sem efeito no cálculo |
| 2 | Tempo por fórum | **35 min** confirmado como valor de **referência** (5 ler instruções + 20 escrever + 10 ler colegas e responder a dois) |
| 3 | Cenários | **Confirmado:** mínimo · **referência** · máximo + **recomendado** |
| 4 | 3º encontro e bloco novo dos encontros | **Computar como executados**, com os **mesmos parâmetros dos encontros anteriores** (vídeos de ~1h26–1h39; card/imagem + sinopse + minutagem) |
| 5 | Git | **Atualizar antes de iniciar** e depois **no final** ou **a cada ~20 atualizações acumuladas** (com autorização) |
| 6 | Bibliografia — duração do vídeo “Representatividade nos livros” | **Link fornecido pelo mestre em 14/10/2026:** `https://www.youtube.com/watch?v=CLm7tYSlPbE` |

---

## §4 — Método (fórmula, parâmetros e cenários)

### §4.1 Fórmula

`tempo(categoria) = quantidade × parâmetro × fator de cenário`

O cálculo é feito **página a página** (uma linha por página no arquivo de cálculo) e depois agregado por **parte**, **módulo**, **categoria** e **bucket** (obrigatório/opcional). Toda quantidade precisa ser **rastreável até o arquivo** (`templates/pages/...`, `assets/h5p/...`, `assets/pdf/...`).

### §4.2 Tabela de parâmetros (proposta — a fixar no Ciclo 2)

| Categoria | Unidade medida no inventário | Parâmetro de **referência** | Faixa (mín ↔ máx) |
|---|---|---|---|
| **Leitura de textos** | palavras visíveis por página | **200 ppm** | 250 ppm ↔ 150 ppm |
| **Estudo ativo** (anotar, reler) | fator sobre a leitura | **×1,3** | ×1,0 ↔ ×1,5 |
| **Imagens** | nº de imagens, **classificadas por tipo** | simples **15 s** · tirinha/charge/cartaz **45 s** · gráfico/infográfico **90 s** · carrossel **20 s/imagem** | −50% ↔ +50% |
| **Vídeos de conteúdo** (bucket A) | duração real (créditos das páginas) | **×1,0** | ×1,0 ↔ ×1,25 |
| **Vídeos da bibliografia** (bucket B) | duração real (créditos + busca na internet) | **×1,0** | — |
| **Atividades H5P** | nº de atividades + nº de questões/itens (lidos do `content.json` do pacote) | **1,5 min/questão** (escolha única, múltipla e V/F) · **3 min** (associação, arrastar, desafio de palavras) · **20 s/carta** (virar cartões) · **5 min** (caça-palavras) | −50% ↔ +50% |
| **Fóruns** | nº de fóruns (14) + exigências do enunciado | **35 min/fórum** (5 ler instruções + 20 escrever + 10 ler colegas e **responder a dois**) | 20 ↔ 45 min |
| **Bibliografia** (bucket B) | nº de itens (38, sendo 21 vídeos) | **1,5 min/item** (consulta/seleção) | 0,5 ↔ 3 min/item |
| **Navegação** | nº de páginas (146) + labels (21) + frontpage (3) | **30 s por página nova** | 15 ↔ 45 s |
| **Encontros síncronos** | nº de encontros (**3**) | **1h30 por encontro** (participação) | — |
| **Gravações dos encontros** (bucket B) | duração (1h26min36 + 1h39min29 + 3º encontro) | **×1,0** | — |
| **SDs em PDF** (bucket B) | nº de PDFs (13) e nº de páginas de cada um | leitura a **200 ppm** sobre o texto do PDF | — |

> **Fontes dos parâmetros:** a preencher no Ciclo 2 (`parametros-carga-horaria.md`) — velocidade de leitura de adultos em português e benchmarks de e-learning, com **citação da fonte** (o mestre autorizou a pesquisa na internet em 14/10/2026).

### §4.3 Cenários

| Cenário | Como é obtido |
|---|---|
| **Mínimo** | todos os parâmetros na ponta “rápida” (250 ppm, imagens −50%, atividades −50%, fórum 20 min, bibliografia 0,5 min, navegação 15 s, vídeo ×1,0) |
| **Referência** | valores da tabela §4.2 |
| **Máximo** | ponta “lenta” (150 ppm, estudo ativo ×1,5, imagens +50%, vídeo ×1,25, atividades +50%, fórum 45 min, bibliografia 3 min, navegação 45 s) |
| **Recomendado** | **referência + 10% de overhead de estudo** (pausas, retomadas, espera por feedback do fórum) — *percentual a confirmar no Ciclo 2* |

### §4.4 Regras de contagem (anti-dupla-contagem)

1. **Página da SD × PDF da SD:** a página do curso (`M4P3L2p2`–`M4P3L5p3`) conta como leitura do **bucket A**; o **PDF** correspondente conta no **bucket B**. Nunca somar os dois ao mesmo bucket.
2. **Vídeo que está na bibliografia e também no conteúdo:** contado **uma vez**, no bucket A (é o vídeo já assistido na página). A bibliografia registra o item e o relatório traz a nota de sobreposição.
3. **Labels e frontpage** entram **apenas** na navegação (não são leitura de conteúdo).
4. **Páginas de abertura, síntese e referências** contam como leitura normal (bucket A), sem tratamento especial.
5. **Fórum:** um valor de tempo **por fórum** (o enunciado descreve o ciclo completo), não por postagem.
6. **Bloco novo dos encontros e 3º encontro:** contam **como executados**, com os parâmetros dos encontros anteriores (decisão de 14/10/2026).

---

## §5 — Inventário (snapshot de 14/10/2026)

> **Fonte oficial das quantidades:** `docs/relatorios/carga-horaria/inventario-recursos.md` e `.csv`, gerados por `scripts/inventario-recursos.py` (**Ciclo 1**, 14/10/2026). A tabela abaixo é o snapshot resumido; **havendo divergência, vale o arquivo gerado**.

| Recurso | M0 | M1 | M2 | M3 | M4 | **Total** |
|---|---|---|---|---|---|---|
| Páginas de conteúdo | 3 | 34 | 36 | 42 | 31 | **146** |
| Palavras (texto visível) | 1.145 | 6.885 | 4.956 | 8.041 | 7.930 | **28.957** |
| Imagens (marcadores oficiais) | 0 | 13 | 9 | 17 | 0 | **39** |
| Vídeos de conteúdo (iframes) | 0 | 1 | 4 | 10 | 2 | **17** (≈ **2h03**) |
| Atividades H5P | 0 | 4 | 9 | 12 | 1 | **26** |
| Fóruns | 1 | 3 | 4 | 4 | 2 | **14** |
| Referências bibliográficas (itens) | — | 20 | 6 | 10 | 2 | **38** (21 são vídeos) |

**Complementos:** 21 labels de parte · 3 páginas de frontpage · 1 galeria de Encontros Síncronos · **13 PDFs** de Sequências Didáticas (`assets/pdf/M4`, 1–2 páginas cada) · **2 encontros síncronos** no ar (gravações de **1h26min36** e **1h39min29**) · 6 ícones de tile e 3 banners (interface).

**Achados relevantes (a favor da precisão):**

1. **A minutagem dos vídeos já está nos créditos das páginas** (`22min07s`, `7min08s`, `48s`…), o que dispensa consulta externa para os 17 vídeos de conteúdo.
2. **As questões de cada H5P podem ser contadas** lendo `content/content.json` dentro do pacote `.h5p` (já testado: quizzes de 9, 8, 5, 4, 3 questões; associação com 8 itens).
3. **Boa parte dos 21 vídeos da bibliografia é o mesmo vídeo já contado no conteúdo** (match por canal + título): ~12 já mapeados (ex.: “Surgimento…” = `07min03s`; “Os direitos do pequeno leitor” = `01min48s`; “Bel Mayer…” = `11min42s`; “Mini Documentário Vaga Lume” = `16min37s`; “A literatura indígena” = `14min55s`).
4. **Vídeo “Representatividade nos livros” (Programa Vaga Lume):** identificado com o link do mestre (14/10/2026) — é o vídeo de **`M2P4L4p3`**, com **14min06s**. Isso **resolve a pendência 7** do `docs/pendencias-projeto.md` (*“link direto do vídeo”*) — a registrar no Ciclo 3.
5. **M4 não tem nenhuma imagem** — o peso do M4 é texto + SDs + fórum.
6. **`assets/h5p/M2/M2P1L1p4-caca-palavras.h5p` não tem página vinculada** (pacote órfão) → **não entra** no bucket A.

## §6 — Artefatos e onde ficam

| Artefato | Caminho | Ciclo | Status |
|---|---|---|---|
| **Este plano** | `docs/relatorios/carga-horaria/PLANO-carga-horaria.md` | 0 | ✅ criado |
| Script de inventário (versionado) | `scripts/inventario-recursos.py` | 1 | ⏳ a criar |
| Inventário (máquina + leitura) | `docs/relatorios/carga-horaria/inventario-recursos.csv` · `.md` | 1 | ⏳ a criar |
| Parâmetros + fontes citadas | `docs/relatorios/carga-horaria/parametros-carga-horaria.md` | 2 | ⏳ a criar |
| Ajustes finos (imagens, fóruns, bibliografia) | seção/arquivo do inventário (`.md`) | 3 | ⏳ a criar |
| Cálculo página a página + tabelas | `docs/relatorios/carga-horaria/calculo-carga-horaria.csv` | 4 | ⏳ a criar |
| **Relatório imprimível (PDF A4)** | `docs/relatorios/carga-horaria/Relatorio-carga-horaria-vagalume.pdf` | 5 | ⏳ a criar |
| **Relatório editável (DOCX)** | `docs/relatorios/carga-horaria/Relatorio-carga-horaria-vagalume.docx` | 5 | ⏳ a criar |
| Espelho de impressão (HTML A4) | `docs/relatorios/carga-horaria/espelho-relatorio.html` | 5 | ⏳ a criar |

> Ferramentas verificadas no ambiente (14/10/2026): `pandoc` (DOCX), `libreoffice`, `reportlab`, `markdown` e o pipeline de PDF do projeto (`scripts/gerar-pdf-sd.sh` → Chrome headless + espelho A4).

## §7 — Ciclos de execução

| Ciclo | Entrega | Status |
|---|---|---|
| **0** | Git sincronizado + este plano salvo + registro no `Onde-paramos.md` | ✅ concluído (14/10/2026) |
| **1** | `scripts/inventario-recursos.py` + `inventario-recursos.csv`/`.md` + entrada no `docs/project-map.md` | ✅ concluído (14/10/2026) |
| **2** | `parametros-carga-horaria.md` (parâmetros + **fontes citadas**) | ⏳ próximo |
| **3** | Ajustes finos: classificar as 39 imagens · revisar os 14 enunciados de fórum · cruzar bibliografia ↔ vídeos · buscar as durações faltantes na internet | ⏳ |
| **4** | `calculo-carga-horaria.csv` + tabelas-resumo (módulo, parte, categoria, cenários, buckets) | ⏳ |
| **5** | Relatório imprimível: **PDF A4 + DOCX** + planilha | ⏳ |
| **6** *(opcional)* | Resumo executivo de 1–2 páginas | ⏳ |

**Regra de execução:** uma entrega por ciclo, com **parada para validação** do mestre (nunca em lote); saídas grandes vão para arquivo, e no chat vão apenas os totais.

## §8 — Reexecução futura (quando o Módulo de Encerramento chegar)

1. Produzir o material do **Módulo de Encerramento** pelo fluxo normal do projeto (`.docx` → `.md` em `content/Encerramento/` → páginas em `templates/pages/Encerramento/` → validação no Moodle).
2. Rodar `python3 scripts/inventario-recursos.py` — as páginas novas entram **automaticamente** no inventário.
3. Atualizar a **§5** deste plano (novo snapshot) e a contagem de módulos/espaços.
4. Recalcular em `calculo-carga-horaria.csv` com a **mesma tabela §4.2**; se houver decisão nova do mestre, registrá-la na **§3** antes de recalcular.
5. Regerar **PDF + DOCX** (§6) e reentregar ao mestre.
6. Atualizar a **§10** (histórico) e o `Onde-paramos.md`.

## §9 — Riscos, limitações e pendências

1. **Estimativa ≠ medição:** não há relatórios do Moodle (confirmado em 14/10/2026) — o relatório declara isso na metodologia.
2. **Módulo de Encerramento fora do escopo** → o total crescerá na reexecução (§8).
3. **21 vídeos da bibliografia sem link:** uso dos créditos das páginas quando houver match seguro; os demais serão buscados por título + canal na internet. Sem match seguro, o item entra como **“duração não localizada”** (não estimar no escuro).
4. **Imagens:** os 39 marcadores são placeholders (as imagens finais estão no Moodle) — a contagem é por marcador e a **classificação por tipo** (foto, tirinha, gráfico, carrossel) é inferência do conteúdo, validada no Ciclo 3.
5. **Overhead de 10%** (cenário recomendado) — decisão a confirmar no Ciclo 2.
6. **Fóruns:** confirmar no Ciclo 3 se **todos** os 14 enunciados pedem o mesmo ciclo (postar · ler colegas · responder a dois); havendo exceção, registrá-la.
7. **Git:** consolidação a cada **~20 atualizações acumuladas** ou no fecho da etapa (decisão de 14/10/2026).

## §10 — Histórico deste plano

| Data | Mudança |
|---|---|
| **14/10/2026** | **Ciclo 0** — criação do plano; decisões do mestre incorporadas; inventário preliminar registrado; link do vídeo “Representatividade nos livros” recebido e mapeado para `M2P4L4p3` (**14min06s**); git sincronizado (commit `ebe1292`); frente registrada no `Onde-paramos.md`. |
| **14/10/2026** | **Ciclo 1** — criados `scripts/inventario-recursos.py` (versionado) e `inventario-recursos.md`/`.csv` (147 páginas, 29.366 palavras, 41 imagens, 26 atividades H5P com 110 itens, 14 fóruns, 13 PDFs, 19 vídeos contados em 2h24min52s + 2 gravações de encontros em 3h06min05s); cruzamento dos 21 vídeos da bibliografia (16 já contados no tempo efetivo + 5 presentes como sugestão); entradas novas no `docs/project-map.md` (`scripts/` e `docs/relatorios/`); decisões de contagem (embedado/instruído conta; sugerido não conta; trecho conta só o trecho) aplicadas no script. |

