<!-- ╔══════════════════════════════════════════════════════════════════════════╗ -->
<!-- ║  AJUSTES FINOS DO INVENTÁRIO — CARGA HORÁRIA (Vaga Lume)                 ║ -->
<!-- ║  Ciclo 3 do relatório de carga horária — aberto em 14/10/2026            ║ -->
<!-- ║  Companheiros: inventario-recursos.md/.csv (INTOCADOS) ·                 ║ -->
<!-- ║  parametros-carga-horaria.md · PLANO-carga-horaria.md                    ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════════╝ -->

# 🔍 Ajustes finos do inventário — Ciclo 3

> **O que é:** registro dos **ajustes finos** que o inventário automático **não** faz — classificação das **imagens por tipo**, revisão dos **enunciados de fórum**, cruzamento **bibliografia × vídeos** e medição do **artigo externo**. É a **segunda metade** da contagem: o **Cálculo (Ciclo 4)** lê *inventário + este arquivo*.
> **Decisão (i) do mestre (14/10/2026):** os ajustes vivem **aqui**, em arquivo separado — o **inventário gerado (`inventario-recursos.md`/`.csv`) fica INTACTO** (reprodutibilidade preservada). **Regra de ouro da skill:** nunca editar o CSV/MD do inventário à mão.
> **Método (skill `metricas-carga-horaria` v1.1.1):** `reference/parametros.md` (parâmetros com fonte e nível de confiança 🟢/🟡/🔴) · `reference/metodo-e-cenarios.md` (buckets e anti-dupla-contagem) · `reference/armadilhas.md`.
> **Status:** **🏁 CICLO 3 FECHADO ✅ (14/10/2026)** — **3A** imagens ✅ · **3B** fóruns ✅ · **3C** bibliografia × vídeos ✅ · **3D** textos externos instruídos ✅. **Bucket A:** imagens **16min40s** · fóruns **7h55min** · textos externos instruídos **7min37s**. **Bucket B:** bibliografia **22,5 min** · ENC **90 s**. **Próximo: CICLO 4 (Cálculo página a página + cenários)**, que lê *inventário + este arquivo*.

---

## §0 — Critério de classificação das imagens (documentado para reprodutibilidade)

Parâmetro: **imagens por tipo** (`parametros-carga-horaria.md` §4, linha 3 — 🔴 heurística do projeto; faixa −50 % ↔ +50 %).

| Tipo | Como reconhecer | Tempo (ref.) |
|---|---|---|
| **Foto / ilustração simples** | **cena única**, **sem texto a ler e sem quadros** (fotografia, retrato, ilustração de cena) | **15 s** |
| **Tirinha / charge / cartum / cartaz / HQ** | a peça **exige leitura**: há **texto na peça** (balões, falas, título, legenda) **ou** está **quadrinizada** (2+ quadros) **ou** traz **crítica a decifrar** | **45 s** |
| **Gráfico / infográfico / linha do tempo** | há **dados ou hierarquia** a interpretar (ex.: formulários com estrutura) | **90 s** |
| **Carrossel / imagem sequencial** | **várias imagens no mesmo bloco** | **20 s por imagem** |

**Regras de aplicação (da skill):** 1) classificar **olhando a imagem**, **nunca** pelo nome do arquivo; 2) **na dúvida entre dois tipos, o mais lento**; 3) **registrar a escolha** (sem registro, a próxima reexecução classifica diferente); 4) **fora da conta:** imagens **dentro de atividade H5P** (cobertas pelo item da atividade — anti-dupla-contagem) e **ícones/logos/tiles/banners** de interface.

> **Refinamento do critério (14/10/2026, decidido no PLAN do 3A.2):** a primeira redação ("peça com texto → 45 s") era **frouxa** e classificaria **toda** peça com qualquer palavra como 45 s. A regra passou a ser **discriminativa**: o degrau de **45 s** exige **texto na peça** (balões/falas/título/legenda), **ou quadrinização** (2+ quadros), **ou crítica a decifrar**; **cena única, sem texto e sem quadros** fica em **15 s**. **Reaplicado ao Módulo 1: nenhum número muda** (capa com título 45 s · carrossel 20 s/imagem · retrato 15 s).

**Como cada imagem foi classificada:** abrindo o **arquivo real** em `assets/images/ilustracoes/<Módulo>/` (fonte oficial versionada) e cruzando com o `alt`/`figcaption` do HTML e o trecho correspondente do DI (`content/<Módulo>/…`). Onde **não há arquivo versionado**, a classificação é feita por contexto e **declarada** na coluna de evidência.

> **Nota de escopo:** os **41 marcadores** do inventário = **39 de conteúdo (M1–M3)** + **2 da página dos Encontros** (decisão em §1.4).

---

## §1 — Imagens

### §1.1 — Módulo 1 (Primeira Infância) — **13 marcadores / 5 páginas** ✅ 3A.1

| # | Página (arquivo) | Marca. | Arquivo da imagem (`assets/images/ilustracoes/M1/`) | Tipo atribuído | Tempo | Evidência da decisão |
|---|---|---|---|---|---|---|
| 1 | `M1/Parte1/Licao1/M1P1L1p3.html` | 1 | `M1P1L1p3.jpg` | **peça gráfica com texto a ler** (capa de livro: título, autor, edição e editora) | **45 s** | imagem vista + `figcaption` ("Capa da obra História Social da Criança e da Família…") |
| 2–6 | `M1/Parte1/Licao1/M1P1L1p4.html` | 5 | `M1P1L1p5img1-carroussel_Roberta_Asse.png` · `…img2…Anna_Cunha.jpg` · `…img3…Isabel_Hojas.jpg` · `…img4…Catherine_Eleonore.jpg` · `…img5…Criancas_e_acesso_sem_cuidado.jpg` | **carrossel** (`#carouselInfancias`, 5 slides; cada um com "Clique para saber mais") | **100 s** (5 × 20 s) | 5 imagens **vistas** + HTML (bloco `carousel`; o parâmetro de carrossel é **20 s por imagem**) |
| 7–11 | `M1/Parte1/Licao1/M1P1L1p5.html` | 5 | *(as **mesmas 5 imagens** do carrossel)* | **recapitulação de bloco já contado** — não é conteúdo novo | **0 s** | HTML (mural `d-flex flex-wrap` de miniaturas, sem legenda nem interação) + **decisão (1)** do mestre |
| 12 | `M1/Parte3/Licao2/M1P3L2p1.html` | 1 | `M1P3L2p2-James_Heckman-500x500.jpg` | **foto / retrato** (retrato de autor) | **15 s** | imagem vista + `alt` ("Retrato fotográfico de James Heckman…") |
| 13 | `M1/Parte4/Licao1/M1P4L1p2.html` | 1 | `M1P4L1img-Brinca_e_aprende_comigo_3.png` | **thumb de vídeo instruído** (interface do player) | **0 s** | imagem vista (card de abertura do ChildFund, "2:20") + HTML (vídeo **já contado** no tempo efetivo: 2min20s) + **decisão (2)** |

**Subtotal M1 — bucket A (= 45 + 100 + 15): 160 s = 2min40s.**
*Linhas zeradas por decisão: mural da p5 (alternativa = +100 s) e thumb do vídeo (alternativa = +15 s) — ver §5.*

### §1.2 — Módulo 2 (Leitura e Primeira Infância) — **9 marcadores / 9 páginas** ✅ 3A.2

| # | Página (arquivo) | Marca. | Arquivo da imagem (`assets/images/ilustracoes/M2/`) | Tipo atribuído | Tempo | Evidência da decisão |
|---|---|---|---|---|---|---|
| 14 | `M2/Parte1/Licao1/M2P1L1p1.html` | 1 | `M2P1L1p1img-cosquinha_na_mamae.png` | **cartum com texto na peça** (título "Cosquinha na mamãe" + falas "HA! HA! HA!") | **45 s** | imagem vista + `figcaption` (pipipum.com.br) |
| 15 | `M2/Parte1/Licao1/M2P1L1p2.html` | 1 | *(**sem cópia versionada**)* | **cartum com legenda** — **classificação por contexto** | **45 s** | `alt` transcreve o texto da peça ("Como me sinto quando… solto a minha voz para fazer ela dormir") — **não há imagem no repo para inspecionar** |
| 16 | `M2/Parte3/Licao1/M2P3L1p1.html` | 1 | `M2P3L2p1img-tirinha-magali.png` (nome fora do padrão) | **tirinha** (2 quadros, balões — Magali, Mauricio de Sousa) | **45 s** | imagem vista + `sr-only` (transcreve os balões) |
| 17 | `M2/Parte3/Licao2/M2P3L2p1.html` | 1 | `M2P3L2p1-garoto_piscina_livros.png` | **ilustração simples** (cena única, sem texto nem quadros) | **15 s** | imagem vista (garoto no trampolim sobre livros; o "LER" na touca é parte da cena, não texto a ler) |
| 18 | `M2/Parte4/Licao1/M2P4L1p1.html` | 1 | `M2P4L1p1img-tirinha-canuto.png` | **tirinha** (3 quadros, balões — Liniers, Macanudo) | **45 s** | imagem vista + `sr-only` |
| 19 | `M2/Parte4/Licao3/M2P4L3p1.html` | 1 | `M2P4L3p1-acervo_vaga_lume.jpeg` | **fotografia** (acervo visto de cima) | **15 s** | imagem vista + `sr-only` (descrição do acervo) |
| 20 | `M2/Parte4/Licao4/M2P4L4p1.html` | 1 | `M2P4L4p1img-May_1.png` | **peça quadrinizada (HQ)** + crítica sobre representatividade a decifrar | **45 s** | imagem vista (quadros internos) + `sr-only` ("em estilo de história em quadrinhos") |
| 21 | `M2/Parte4/Licao4/M2P4L4p2.html` | 1 | `M2P4L4p1img-May_2.png` (nome fora do padrão) | **peça quadrinizada (HQ)** (balão de pensamento) | **45 s** | imagem vista + `sr-only` (confirma **1:1** qual May pertence a qual página) |
| 22 | `M2/Parte5/M2P5L2p1.html` | 1 | `M2P5L2p1img-Kaio.png` | **cartum com texto na peça** ("estou tentando cuidar mais de mim") | **45 s** | imagem vista (cartum do Kaio) + `alt` |

**Subtotal M2 — bucket A (= 7 × 45 s + 2 × 15 s): 345 s = 5min45s.** *(Alternativa agregada na §5.)*

### §1.3 — Módulo 3 (Bibliotecas Comunitárias) — **17 marcadores / 10 páginas** ✅ 3A.3

| # | Página (arquivo) | Marca. | Arquivo da imagem (`assets/images/ilustracoes/M3/`) | Tipo atribuído | Tempo | Evidência da decisão |
|---|---|---|---|---|---|---|
| 23 | `M3/Parte1/Licao1/M3P1L1p1.html` | 1 | `M3P1L1p1-tirinha-quino.png` | **tirinha** (quadro único **com balão de fala** — Mafalda, Quino) | **45 s** | imagem vista + `sr-only` (transcreve a fala) |
| 24 | `M3/Parte1/Licao2/M3P1L2p1.html` | 1 | `M3P1L2p1-acervo_vaga_lume.jpg` | **fotografia** (árvore com livros pendurados por cordões) | **15 s** | imagem vista + `sr-only` |
| 25–29 | `M3/Parte1/Licao3/M3P1L3p1.html` | 5 | `M3P1L3p1-card1-encontro_e_convivencia.jpg` · `…card2-producao_cultural.jpg` · `…card3-troca_de_saberes.jpg` · `…card4-escuta_e_participacao.jpg` · `…card5-mobilizacao_comunitaria.jpg` | **5 fotografias** (roda de leitura · apresentação de dança · roda de conversa ao ar livre · roda de conversa em varanda · roda aérea comunitária) — **nenhum texto a ler** | **75 s** (5 × 15 s) | 5 imagens **vistas** + `sr-only` (fotografia em cada) |
| 30–33 | `M3/Parte2/Licao4/M3P2L4p1.html` | 4 | `M3P2L4p1img1-canoa.png` · `…img2-livros_sobre_mesa.png` · `…img3-criancas_bananeira.png` · `…img4-livro_sobre_cabeca.png` | **4 ilustrações estilizadas**, cores planas, **sem texto** (mulher remando · livros sobre a mesa · três crianças de ponta-cabeça · livro equilibrado na cabeça) | **60 s** (4 × 15 s) | 4 imagens **vistas** + `sr-only` ("ilustração estilizada em cores planas") |
| 34 | `M3/Parte3/Licao2/M3P3L2p1.html` | 1 | `M3P3L2p1-cuidado_em_comunidade.jpg` | **fotografia** (jovem lendo "Tango de Gato" para uma idosa, com uma nutriz ao fundo) | **15 s** | imagem vista + `sr-only` |
| 35 | `M3/Parte4/Licao3/M3P4L3p1.html` | 1 | `M3P4L3p1-tirinha-stahler.png` | **cartum** de um quadro **com balões** ("A carteira da biblioteca" — Stahler, 2010) | **45 s** | imagem vista + `sr-only` (transcreve as falas) |
| 36 | `M3/Parte4/Licao3/M3P4L3p2.html` | 1 | `M3P4L3p2-carteirinha.png` | **documento estruturado** (modelo de carteirinha: campos Biblioteca/Comunidade/Município/Nome/Idade + **tabela** de retirada/devolução/carimbo + regras de validade) | **90 s** | imagem vista + **decisão (3a)** |
| 37 | `M3/Parte4/Licao3/M3P4L3p3.html` | 1 | `M3P4L3p3-caderno_de_memorias.png` | **peça com texto a ler** (capa: título "Caderno de Memórias", "Biblioteca – 2026", logo e campos Município/Comunidade) | **45 s** | imagem vista + `figcaption` — **decisão (3c)** (coerente com a capa do Ariès) |
| 38 | `M3/Parte4/Licao3/M3P4L3p4.html` | 1 | `M3P4L3p4-regimento.png` | **documento estruturado** (formulário: título "Preencha o regimento da sua biblioteca:", cabeçalho e **cinco seções** com espaços) | **90 s** | ⚠️ **imagem não inspecionável** ("media omitted") — evidência: `sr-only` da página + `descricoes.md`; **decisão (3a)** |
| 39 | `M3/Parte4/Licao3/M3P4L3p5.html` | 1 | `M3P4L3p5-plano_de_acao.png` | **ilustrativo** — modelo de Plano de Ação (tabela de 4 linhas; **os detalhes dos quadros não precisam ser lidos**) | **15 s** | ⚠️ **imagem não inspecionável** ("media omitted") — evidência: `descricoes.md` + **decisão explícita do mestre (10/10/2026)**: "a imagem **apenas ilustra**…" — **decisão (3b)** |

**Subtotal M3 — bucket A (= 45 + 15 + 75 + 60 + 15 + 45 + 90 + 45 + 90 + 15): 495 s = 8min15s.** *(Alternativas nas decisões (3a), (3b) e (3c) — ver §5.)*

### §1.4 — Página dos Encontros Síncronos (ENC) — **2 cards** ✅ 3A.3

| # | Página (arquivo) | Marca. | Arquivo da imagem (`assets/images/ilustracoes/Encontros-sincronos/`) | Tipo atribuído | Tempo | Evidência da decisão |
|---|---|---|---|---|---|---|
| 40 | `Encontros-sincronos/encontros_sincronos_galeria.html` | 1 | `Encontro_Sincrono_1_card.jpg` | **cartaz de divulgação** (título, tema, data/hora, convidada, mediadora, programação, logos) | **45 s** | imagem **vista** + `sr-only` ("Card de divulgação do Encontro Síncrono…") — **decisão (4)** |
| 41 | `Encontros-sincronos/encontros_sincronos_galeria.html` | 1 | `Encontro_Sincrono_2_card.png` | **cartaz de divulgação** (mesmo padrão do card 1) | **45 s** | ⚠️ **imagem não inspecionável** ("media omitted") — evidência: `sr-only` ("Card de divulgação do Segundo Encontro Síncrono…") + **analogia com o card 1**; **decisão (4)** |

**Subtotal ENC — bucket B (= 2 × 45 s): 90 s = 1min30s.** *(Vai com as **gravações** dos encontros, já opcionais.)*

### §1.5 — Totais das imagens (Ciclo 3A fechado)

| Módulo | Marcadores | Tipo dominante | Bucket A | Bucket B |
|---|---|---|---|---|
| M1 | 13 | carrossel (5) + fotos/peças | **160 s = 2min40s** | 0 |
| M2 | 9 | tirinhas/cartuns/HQ (7) + 2 simples | **345 s = 5min45s** | 0 |
| M3 | 17 | 5 fotos + 4 ilustrações + tirinha/cartum + 3 documentos/capas | **495 s = 8min15s** | 0 |
| ENC | 2 | cartazes de divulgação | 0 | **90 s = 1min30s** |
| **Total** | **41 de 41** | **Ciclo 3A fechado ✅** | **1.000 s = 16min40s** | **90 s = 1min30s** |

---

## §2 — Fóruns (14) ✅ 3B

> **Parâmetro:** **35 min/fórum** = ciclo completo **ler instruções · escrever · ler colegas · responder a dois** (🟡 decisão do mestre, 14/10/2026; faixa **20 ↔ 45 min**). **Regra da skill:** o valor é **por fórum** (ciclo **completo**), **nunca** por postagem — por isso os **14 enunciados foram lidos um a um** para confirmar (ou excepcionar) o ciclo.

| # | Fórum (página) | Título | Exigência no enunciado | Tempo |
|---|---|---|---|---|
| 1 | `Boas-vindas/Boas-vindas_Forum_Espaco_de_apresentacao.html` | Espaço de apresentação | **livre** — "Se quiser…", "A apresentação é livre!", "leia algumas… e, **se desejar**, deixe uma mensagem" → **sem** os dois comentários | **20 min** ⚖️ |
| 2 | `M1/Parte1/M1P1F1.html` | Memórias da infância | postar (1 pergunta) + **comentar em ≥2** | 35 min |
| 3 | `M1/Parte3/M1P3F1.html` | Infâncias no território - olhar, escutar e refletir | postar (1 pergunta + orientação) + **comentar em ≥2** | 35 min |
| 4 | `M1/Parte4/M1P4F1.html` | Inspirando ações comunitárias para quem cuida da Primeira Infância | postar (2 alternativas + explicação) + **comentar em ≥2** + **estudo de caso** | 35 min *(vídeo e artigo já contados — ver nota)* |
| 5 | `M2/Parte1/M2P1F1.html` | Quando começa a história de um leitor ou leitora? | postar (1 pergunta) + **comentar em ≥2** | 35 min |
| 6 | `M2/Parte3/M2P3F1.html` | Relembrando uma experiência de mediação em sua vida | postar (**3 itens**) + **comentar em ≥2** | 35 min |
| 7 | `M2/Parte4/M2P4F1.html` | A importância da bibliodiversidade para a formação leitora | postar (**2 perguntas**) + **comentar em ≥2** | 35 min |
| 8 | `M2/Parte5/M2P5F1.html` | Cuidar de si também é cuidar do coletivo | postar (**4 pontos**) + **comentar em ≥2** | 35 min |
| 9 | `M3/Parte1/M3P1F1.html` | Como você imagina uma Biblioteca Comunitária em seu território? | postar (**3 itens**) + **comentar em ≥2** | 35 min |
| 10 | `M3/Parte2/M3P2F1.html` | Olhando a Biblioteca Comunitária com olhos de criança | postar (1 pergunta + justificativa) + **comentar em ≥2** | 35 min |
| 11 | `M3/Parte3/M3P3F1.html` | Como a Biblioteca Comunitária pode promover acolhimento, cuidado e bem-estar? | postar (**2 itens**) + **comentar em ≥2** | 35 min |
| 12 | `M3/Parte4/M3P4F1.html` | Pensando a gestão da Biblioteca Comunitária da qual faço parte | postar (**3 itens**) + **comentar em ≥2** | 35 min |
| 13 | `M4/Parte1/M4P1F1.html` | O que é ser mediador ou mediadora de leitura? | postar (2 caminhos) + **comentar em ≥2** | 35 min |
| 14 | `M4/Parte2/M4P2F1.html` | Boas práticas para organizar atividades na biblioteca | postar (2 cenários + **3 itens**) + **comentar em ≥2** | 35 min |

**Subtotal — bucket A: 13 × 35 min + 20 min = 475 min = 7h55min.**

> **Anti-dupla-contagem — `M1P4F1` (o único com estudo de caso):** o **vídeo** (19min46s) **já está contado no bucket de vídeos** do inventário (`videos_instruidos=1` · `video_segundos=1186`) → **não somar aqui**; o **artigo** dos 2 links externos entra no bucket A **medido no 3D**; o "**ler instruções**" **já está dentro dos 35 min** (regra nº 6 da skill). **Nada disso se soma duas vezes.**

> **Observação de densidade:** **6 dos 13** fóruns padrão trazem **enunciado extenso** (3+ itens de reflexão ou dois cenários): `M2P3F1` · `M2P4F1` · `M2P5F1` (**4 pontos**) · `M3P1F1` · `M3P4F1` · `M4P2F1`. A referência **mantém 35 min** (decisão flat do mestre) — alternativa **+5 min cada** na §5 (linha 17).

## §3 — Bibliografia × vídeos (38 itens) ✅ 3C

> **Composição:** **38 itens** nas 4 páginas de Referências — **17 de texto** (14 no M1 + 3 no M2) e **21 de vídeo** (6 no M1 · 3 no M2 · 10 no M3 · 2 no M4). Parâmetros: **1,5 min/item** para item de **texto** (🔴 heurística; faixa 0,5↔3 min) e **duração real ×1,0** para item de **vídeo** — **sem somar o que já está no bucket A**.
> **Método:** a identidade dos **21 vídeos** foi conferida **1 a 1 pelo `oEmbed`** (título + canal), que é exatamente o que afasta os **dois falsos positivos** que a skill manda vigiar (`reference/duracoes-e-cruzamento.md` §4).

### §3.1 — Cruzamento dos 21 itens de vídeo (identidade conferida por `oEmbed`)

| # | Item — canal/autor (bibliografia) | Item — título (bibliografia) | ID | `oEmbed` — canal | `oEmbed` — título | Situação |
|---|---|---|---|---|---|---|
| 1 | FUNDAÇÃO MARIA CECILIA SOUTO VIDIGAL | O que é Primeira Infância? | `ttJtRokJJIk` | Fundação Maria Cecilia Souto Vidigal | O que é Primeira Infância? | ✅ **já contado em A** (1min29s) |
| 2 | CHILDFUND BRASIL | O que é Parentalidade | `KrMfedDRUhw` | ChildFund Brasil | O que é Parentalidade | ✅ já contado em A (crédito da página: 02min19s) |
| 3 | SESC SÃO PAULO | Quem cuida de cuidadores da Primeira Infância? | `dIyr6srurC0` | Sesc São Paulo | SESC IDEIAS — QUEM CUIDA DE CUIDADORES DA PRIMEIRA INFÂNCIA? | ✅ já contado em A (**trecho** de 19min46s) |
| 4 | DORRICO, Julie | A literatura indígena: conhecendo outros Brasis | `gKVOXmuEbwU` | TEDx Talks | A literatura indígena: conhecendo outros brasis (Julie Dorrico) | ✅ já contado em A (14min55s) |
| 5 | LEITE, Patrícia Bohrer Pereira | Ler para bebê: a importância da leitura na primeira infância | `bz0WYDtpR5g` | Ler é Uma Viagem | Ler para bebê… — Com Patrícia Bohrer Pereira Leite | ✅ já contado em A (22min07s) |
| 6 | VAGA LUME | Representatividade nos livros | `CLm7tYSlPbE` | Vaga Lume | Representatividade nos livros | ✅ já contado em A (14min06s) |
| 7 | A UM LIVRO DE DISTÂNCIA | Surgimento: Saiba como nasce uma Biblioteca Comunitária | `frcDs0p5SXw` | A Um Livro De Distancia | Surgimento — Saiba como nasce uma Biblioteca Comunitária | ✅ já contado em A (7min03s) |
| 8 | CONTÔ GENIAL | Os direitos do pequeno leitor | `bBDU_2-HYjU` | Conto Genial | OS DIREITOS DO PEQUENO LEITOR — BIBLIOTECA LIVRE | ✅ já contado em A (1min48s) |
| 9 | ITAÚ CULTURAL | Bel Mayer: Rede Nacional de Bibliotecas Comunitárias — gestão cultural (2018) | `BcKH3nxcMWE` | Itaú Cultural | Bel Mayer — Rede Nacional de Bibliotecas Comunitárias – gestão cultural (2018) | ✅ já contado em A (11min42s) |
| 10 | LEONARDO ASSIS | Gestão de Bibliotecas Comunitárias: Desafios e Engajamento Comunitário | `ol5CRV6CDC4` | **Leonardo Assis** | Gestão de Bibliotecas Comunitárias: Desafios e Engajamento Comunitário | ✅ já contado em A (48s) — 🎯 **par de título genérico resolvido pelo canal** |
| 11 | MANOS E MINAS | Matéria: Biblioteca Comunitária | `IyrSM12ctEs` | Manos e Minas | Matéria: Biblioteca Comunitária | ✅ já contado em A (3min32s) |
| 12 | MULTIVOZES NA ESCOLA | O que é acolhimento? | `cGDSSRtlKl0` | Multivozes na escola | O que é acolhimento? | ✅ já contado em A (1min18s) |
| 13 | PALAVRA CANTADA | Brincar de Ler: Leia para uma Criança | `iM9UO3eJ6WE` | Palavra Cantada Oficial | Brincar de Ler — Leia para uma Criança | ✅ já contado em A (2min33s) |
| 14 | UNAS HELIÓPOLIS | O papel transformador de uma Biblioteca Comunitária dentro da maior favela de São Paulo | `vOUPq400mUA` | UNAS Heliópolis | O papel transformador de uma Biblioteca Comunitária dentro da maior Favela de São Paulo | ✅ já contado em A (4min28s) |
| 15 | VAGA LUME | Bibliotecas Amazônicas — Mini Documentário Vaga Lume | `MO86dcxz2yU` | Vaga Lume | Bibliotecas Amazônicas — Mini Documentário Vaga Lume | ✅ já contado em A (16min37s) |
| 16 | VAGA LUME | Gestão de Bibliotecas Comunitárias | `pZohuyYUyjg` | **Vaga Lume** | Gestão de Bibliotecas Comunitárias | ✅ já contado em A (3min48s) — 🎯 **par de título genérico resolvido pelo canal** |
| 17 | CAÇANDO ESTÓRIAS | Eu li na Ení: mediação de leitura e formação de leitores | `77MwhhfnYp0` | Caçando Estórias | EU LI NA ENÍ — Tema: Mediação de leitura e formação de leitores | ✅ já contado em A (6min51s) |
| 18 | VAGA LUME | O que é mediação de leitura? | `tva28rNVdMU` | Vaga Lume | O que é mediação de leitura? | ✅ já contado em A (2min33s) |
| 19 | FUNDAÇÃO MARIA CECILIA SOUTO VIDIGAL | 5 dicas para gestantes de primeira viagem | `olFTlBgnzGA` | Fundação Maria Cecilia Souto Vidigal | 5 dicas para gestantes de primeira viagem | 📌 **sugestão** ("Quer saber mais?") — registrada, **não conta** |
| 20 | FUNDAÇÃO MARIA CECILIA SOUTO VIDIGAL | Mudanças Físicas e Emocionais na Gestante: O que fazer? | `NVRm2tjoeqw` | Fundação Maria Cecilia Souto Vidigal | Mudanças Físicas e Emocionais na Gestante — O que fazer? | 📌 **sugestão** — registrada, **não conta** |
| 21 | FUNDAÇÃO MARIA CECILIA SOUTO VIDIGAL | Gestação, Pré-Natal e Saúde do Bebê: O que fazer? | `TmNf3cDnM1Q` | Fundação Maria Cecilia Souto Vidigal | Gestação, Pré-Natal e Saúde do Bebê — O que fazer? | 📌 **sugestão** — registrada, **não conta** |

**Resultado do cruzamento: 18 itens = o mesmo vídeo já contado no bucket A (≈ 0 min na bibliografia) · 3 itens = sugestões (registradas, não contam).**

**Falsos positivos vigiados e descartados:** (i) **por canal** — os **4** itens da Fundação MC foram conferidos **um a um** e o `oEmbed` devolve **4 títulos distintos** (Primeira Infância · 5 dicas · Mudanças Físicas · Gestação) → **não houve casamento por canal**; (ii) **por título genérico** — "Gestão de Bibliotecas Comunitárias" (**Vaga Lume**, `pZohuyYUyjg`) × "Gestão de Bibliotecas Comunitárias: Desafios…" (**Leonardo Assis**, `ol5CRV6CDC4`) → **canais diferentes confirmados** → itens distintos, cada um com o seu vídeo (linhas 10 e 16).

### §3.2 — Itens de texto e subtotal da bibliografia (bucket B)

| Página de Referências | Itens de texto | Tempo (1,5 min/item) |
|---|---|---|
| `M1/Parte5/M1P5P2.html` | 14 | 21 min |
| `M2/Parte6/M2P6P2.html` | 3 | 4,5 min |
| `M3/Parte5/M3P5P2.html` | 0 | 0 |
| `M4/Parte4/M4P4P2.html` | 0 | 0 |
| **Subtotal** | **17** | **25,5 min** |

**Ajuste por sobreposição (anti-dupla-contagem) — princípio firmado por você (14/10/2026):** "*textos e vídeos citados na bibliografia que já tenham sido computados no corpo do curso **não se contam duas vezes** (obviamente)*". **Dois itens de texto** caem nesse caso:

1. **FUNDAÇÃO TELEFÔNICA VIVO — "Da alimentação à poesia, mulheres atuam pela Primeira Infância em Parelheiros"** → é o **estudo de caso do Fórum 4 do M1** → computado no **bucket A** (medido no **3D**);
2. **BBC NEWS BRASIL — "O que é o estresse tóxico e como ele pode afetar a saúde e o desenvolvimento das crianças"** → **instruída** em `M1P3L1p2` ("*leia a reportagem*") → computada no **bucket A** (medida no **3D**).

**Subtotal da bibliografia (bucket B): 15 × 1,5 = 22,5 min** (17 itens de texto **− 2 sobrepostos**). *(Alternativa: 25,5 min, se os dois itens fossem somados também aqui — §5, linhas 18 e 19.)*
*Os **21 itens de vídeo** não somam na bibliografia: 18 são o **mesmo vídeo já contado no bucket A** e 3 são **sugestões** (registradas, não contam) — §3.1.*

### §3.3 — Durações externas: fonte e limitação de re-verificação

As **5 durações** que o plano do Ciclo 3 listava como "a localizar" estão **resolvidas desde o Ciclo 1** e **documentadas no próprio script**: `scripts/inventario-recursos.py` → bloco `DUR_EXTERNAS`, com o comentário "*Durações reais de vídeos externos (**verificadas em 14/10/2026 via oEmbed + lengthSeconds**)*" — `olFTlBgnzGA` 72 s · `NVRm2tjoeqw` 268 s · `TmNf3cDnM1Q` 224 s (as 3 sugestões da Fundação MC) · `KrMfedDRUhw` 140 s (ChildFund) · `dIyr6srurC0` 5805 s (Sesc — **vídeo completo**; no curso conta só o **trecho** de 19min46s).

⚠️ **Limitação do ambiente (testada em 14/10/2026):** a **re-verificação automática das durações não é possível aqui** — o YouTube **não devolve mais `lengthSeconds`** por `curl` (testado sem e com User-Agent, com cookie `CONSENT` e via `POST` innertube), **`yt-dlp` não está instalado** e Invidious/Piped não respondem. O **`oEmbed` funciona** e foi a ferramenta da conferência de **identidade** (§3.1). **Impacto no total: nenhum** — as 3 sugestões **não contam** em bucket algum, o vídeo do ChildFund é **corroborado pelo crédito da própria página** (02min19s ≈ 139 s; 1 s de diferença vs. os 140 s do script — a skill prevê essa divergência) e o do Sesc entra apenas pelo **trecho**.

### §3.4 — Observações de fidelidade (registradas; **nada alterado**)

1. **📖 Leitura instruída no conteúdo (fora do radar do inventário) — DECIDIDA por você (14/10/2026):** `M1/Parte3/Licao1/M1P3L1p2.html` instrui "*Para saber mais sobre esse tema, **leia a reportagem da BBC News Brasil***" — é a **mesma** reportagem listada na bibliografia do M1 (item BBC NEWS BRASIL). Pela régua da **decisão (b)** ("instruído conta"), é **leitura computada no bucket A** → **medida no 3D** e **não somada** na bibliografia (§5, linha 19).
2. **🔗 Recurso interativo instruído:** `M1/Parte3/Licao2/M1P3L2p2.html` instrui "*Acesse a plataforma **Primeira Infância em Dados***" — recurso **interativo**, **sem parâmetro** na skill → registrado **sem contar** (alternativa registrada: 1,5 min como item de consulta → **+1,5 min** em A; a confirmar com o mestre).
3. **⚖️ Legislação em dois lugares, sem soma dupla:** as **7 leis + 2 documentos** do M1 aparecem **no conteúdo** (`M1/Parte3/Licao2/M1P3L2p3.html` — timeline expansível cujo texto **já está contado nas palavras da página**, bucket A) **e** na bibliografia (1,5 min/item, bucket B) → **buckets diferentes** ✅.
4. **🖨️ Botão de PDF do M4:** as 13 páginas de SD têm o botão "Baixar atividade (PDF)" com `href="#"` — **não é pendência**: é o **placeholder** cujo link o mestre define **no Moodle** ao publicar (esclarecido por você em 14/10/2026).

## §4 — Textos externos instruídos (bucket A) ✅ 3D

> **O que mede:** o **tempo de leitura** dos **textos externos que o curso instrui a ler** (bucket A). Ambos **já foram retirados** da soma da bibliografia (§3.2) — são computados **uma única vez**, aqui.

| # | Texto (onde o curso instrui) | URL | Palavras | **200 ppm (ref.)** | 250 ppm (mín.) | 150 ppm (máx.) |
|---|---|---|---|---|---|---|
| 1 | **Fórum 4 do M1** — "*Da alimentação à poesia, mulheres atuam pela primeira infância em Parelheiros*" (Fundação Telefônica Vivo) | `fundacaotelefonicavivo.org.br/noticias/da-alimentacao-a-poesia-mulheres-atuam-pela-primeira-infancia-em-parelheiros/` | **954** | **4min46s** | 3min49s | 6min22s |
| 2 | **`M1/Parte3/Licao1/M1P3L1p2.html`** — "*O que é o estresse tóxico — e como ele pode afetar a saúde e o desenvolvimento das crianças*" (BBC News Brasil) | `bbc.com/portuguese/geral-42625980` | **570** | **2min51s** | 2min17s | 3min48s |
| | **Total (bucket A)** | | **1.524** | **7min37s** | 6min06s | 10min10s |

### §4.1 — Como foi medido (método documentado, para reprodutibilidade)

1. **Extração do texto** por **`r.jina.ai`** (`curl 'https://r.jina.ai/<url>'` → artigo em markdown). Foi **necessário** porque: o site da FTV **bloqueia o acesso direto** (resposta "Access Denied", 523 B — testado com 2 User-Agents) e a página da BBC **não tem `<article>`** (a contagem crua daria **1.424** palavras = menu + rodapé + "Mais lidas").
2. **Delimitação do corpo:** do **1º parágrafo** ao **fim do texto**. **Não entram:** título, linha de apoio, data/"Tempo de leitura", categoria, botões de compartilhar, blocos de relacionados ("Leia também", "Mais lidas", "Outras Notícias"), legendas/créditos de imagem e rodapé.
3. **Contagem de palavras:** expressão regular `[A-Za-zÀ-ÿ0-9]+` → **954** (FTV) e **570** (BBC); total **1.524**.
4. **Tempo:** `palavras ÷ ppm` — parâmetro **§4, linha 1** do `parametros-carga-horaria.md` (🟢🟡): **200 ppm** de referência; pontas **250** (mín.) e **150** (máx.).
5. **Fator de cenário:** aqui entra a **contagem + o tempo de referência** (e as pontas); o **estudo ativo (×1,3)** e o overhead são aplicados no **Cálculo (Ciclo 4)**.

🎯 **Contraprova (FTV):** a própria página declara "**Tempo de leitura: 6 minutos**" — cai **dentro da faixa** (ref 4min46s ↔ máx 6min22s), corroborando a contagem.

### §4.2 — Observações de fidelidade

1. **Vídeo embutido no artigo da FTV** (YouTube `UALS_mPdlTw`): **não instruído** pela página do curso → **não computado** (registrado). A duração não foi localizada e, em 14/10/2026, o ambiente **não permite** extrair `lengthSeconds` (§3.3).
2. **Limitação declarada:** a contagem **depende da extração do `r.jina.ai`** (serviço de terceiro). Se a extração do site mudar, o número muda — por isso ficam registrados **URL + critério + expressão de contagem + contraprova da própria página**.
3. **Recorrência futura:** este é o **único** par de leituras externas instruídas do curso até aqui (varredura em 14/10/2026); novos módulos podem trazer outras — a §8 do `parametros-carga-horaria.md` remete a esta seção.

---

## §5 — Decisões registradas (rastreabilidade das escolhas)

| # | Decisão | Escolha aplicada | Alternativa registrada | Status |
|---|---|---|---|---|
| 1 | `M1P1L1p4` (carrossel) × `M1P1L1p5` (mural) — **mesmas 5 imagens** | conta **uma vez**, no carrossel (100 s); mural **não conta** | +100 s (contar o mural como sequência de 5 × 20 s) | ✅ aplicada no 3A.1 |
| 2 | `M1P4L1p2` — thumb de **vídeo instruído** | **não conta** (o vídeo já entra com 2min20s) | +15 s | ✅ aplicada no 3A.1 |
| 3 | `M3P4L3p2/p4/p5` — modelos/formulários | definir **olhando a imagem** (90 s se houver estrutura a interpretar; 15 s se apenas ilustrativo; **na dúvida, 90 s**) | — | ✅ **resolvida no 3A.3 — ver linhas 12 e 13** |
| 4 | ENC — 2 cards de divulgação | **45 s cada** ("cartaz de divulgação", exemplo literal da skill), bucket B | 15 s (simples) ou 0 s (interface) | ✅ **resolvida no 3A.3 — ver linha 15** |
| 5 | `M1P1L1p3` — capa de livro (Ariès) | **45 s** — a capa **não é "uma cena sem texto a ler"**: título, autor, edição e editora são lidos | 15 s (tratar como ilustração) | ✅ aplicada no 3A.1 |
| 6 | `M2P1L1p1` — cartum "Cosquinha na mamãe" | **45 s** (cartum **com texto na peça**: título + falas) | 15 s (ilustração de cena) | ✅ aplicada no 3A.2 |
| 7 | `M2P1L1p2` — cartum pipipum | **45 s** (cartum **com legenda**, transcrita no `alt`; **classificação por contexto — sem cópia versionada no repo**) | 15 s | ✅ aplicada no 3A.2 |
| 8 | `M2P4L4p1` — HQ May_1 (representatividade) | **45 s** (peça **quadrinizada** + crítica a decifrar) | 15 s (tratar como ilustração) | ✅ aplicada no 3A.2 |
| 9 | `M2P4L4p2` — HQ May_2 (sonho profissional) | **45 s** (peça **quadrinizada**, com balão de pensamento) | 15 s | ✅ aplicada no 3A.2 |
| 10 | `M2P5L2p1` — cartum Kaio (autocuidado) | **45 s** (cartum **com texto na peça**) | 15 s | ✅ aplicada no 3A.2 |
| 11 | **Critério de classificação (§0)** | **refinado — discriminativo**: 45 s exige texto na peça **ou** quadrinização **ou** crítica a decifrar | redação anterior (frouxa: "peça com texto" pegava tudo) | ✅ aplicada no 3A.2 |
| 12 | `M3P4L3p2` (carteirinha) + `M3P4L3p4` (regimento) — **modelos/formulários** | **90 s cada** — **documento estruturado** (campos + tabela de empréstimo na carteirinha; **cinco seções** no regimento); "na dúvida, o mais lento" | **45 s** (peça com texto → **−90 s**) ou **15 s** (apenas ilustrativo → **−150 s**) | ✅ aplicada no 3A.3 — **decisão (3a)** |
| 13 | `M3P4L3p5` (plano de ação) — modelo de Plano de Ação | **15 s** — **decisão explícita do mestre (10/10/2026)**: "a imagem **apenas ilustra**… os detalhes dos quadros **não precisam ser lidos**" (não é caso de dúvida) | 90 s (uniformizar com carteirinha/regimento → **+75 s**) | ✅ aplicada no 3A.3 — **decisão (3b)** |
| 14 | `M3P4L3p3` (capa do Caderno de Memórias) | **45 s** — peça **com texto a ler** (título, "Biblioteca – 2026", logo, campos), coerente com a **capa do Ariès** (decisão 5) | 15 s (tratar como ilustração → **−30 s**) | ✅ aplicada no 3A.3 — **decisão (3c)** |
| 15 | **ENC** (página dos Encontros) — 2 cards de divulgação | **45 s cada = 90 s**, no **bucket B** ("cartaz de divulgação" é **exemplo literal** da skill; card 1 **visto**) | 15 s (simples → **−60 s**) ou 0 s (interface → **−90 s**) | ✅ aplicada no 3A.3 — **decisão (4)** |
| 16 | Fórum do **Boas-vindas** ("Espaço de apresentação") | **20 min** — **piso da faixa 20↔45 min** da skill: fórum **livre**, **sem** a exigência dos dois comentários ("A apresentação é livre!") | **25 min** (35 − ~10 dos dois comentários → **+5 min**) | ✅ aplicada no 3B — **decisão (16)** |
| 17 | **6 fóruns com enunciado extenso** (`M2P3F1` · `M2P4F1` · `M2P5F1` · `M3P1F1` · `M3P4F1` · `M4P2F1`) | **mantidos em 35 min** — referência **flat**, por decisão do mestre (14/10/2026); o enunciado mais longo **não** altera o parâmetro | **+5 min cada → +30 min** (fóruns = **8h25min**) | ✅ aplicada no 3B — **decisão (17)** |
| 18 | **Artigo da Fundação Telefônica Vivo** — item da bibliografia do M1 **e** estudo de caso do Fórum 4 | **contado uma vez**: no **bucket A**, medido no **3D**; **não somado** na bibliografia (B) | somar o item também no B → **+1,5 min** (bibliografia = 25,5 min) | ✅ aplicada no 3C — **decisão (18)** |
| 19 | **Reportagem da BBC** — **instruída** em `M1P3L1p2` ("leia a reportagem") **e** item da bibliografia do M1 | **leitura computada no bucket A** → **medida no 3D** (junto com o artigo do Fórum 4); na bibliografia **não soma** | somar o item também no B → **+1,5 min** (bibliografia = 24 min) | ✅ aplicada no 3C — **decisão (19)**, confirmada por você em 14/10/2026 ("mesmo caso anterior") |

> **Regra de reversão:** qualquer linha desta tabela pode ser invertida no **Cálculo (Ciclo 4)** sem reclassificar nada — a alternativa já está quantificada.

> **Alternativa agregada do M2 (linhas 6 a 10):** se prevalecer a leitura **estrita** — 45 s **só** para peças com **diálogo/quadros literais**, tratando os cartuns ilustrados como ilustração simples — as **5 linhas em disputa** caem para 15 s → **−150 s** → subtotal do M2 = **195 s = 3min15s**. O subtotal de referência (345 s = 5min45s) é o que entra no Cálculo.

> **Alternativa agregada do M3 (linhas 12 a 14):** se os **três instrumentos** forem tratados como **apenas ilustrativos (15 s)** e a capa do Caderno também cair para 15 s → **−180 s** → subtotal do M3 = **315 s = 5min15s**. O subtotal de referência (495 s = 8min15s) é o que entra no Cálculo.

> **⚖️ PRINCÍPIO FIRMADO POR VOCÊ (14/10/2026) — vale para todo o Ciclo 3:** **textos e vídeos citados na bibliografia que já tenham sido computados no corpo do curso NÃO se contam duas vezes**. Aplicado em: **(a)** os **18 vídeos** da bibliografia (todos já contados no bucket A); **(b)** o **artigo da FTV** (estudo de caso do Fórum 4 → bucket A); **(c)** a **reportagem da BBC** (instruída em `M1P3L1p2` → bucket A). Os 3 textos/18 vídeos ficam **registrados** na bibliografia, mas **fora da soma**.

---

## §6 — Como este arquivo entra no Cálculo (Ciclo 4)

1. O Cálculo **nasce do CSV** do inventário (uma linha por página) e substitui, por categoria, o que **só este arquivo** tem: **imagens** (§1 — nº por tipo e tempo) · **fóruns** (§2 — 35 min, com a exceção do Boas-vindas em 20 min) · **bibliografia** (§3 — 15 itens de texto × 1,5 min) · **textos externos instruídos** (§4 — palavras ÷ ppm) — **sem** alterar o CSV.
2. Cada linha traz **página + arquivo + tipo + tempo + evidência** → rastreável até a peça.
3. **A §8 do `parametros-carga-horaria.md`** (lacunas) foi **atualizada no fecho do Ciclo 3** (14/10/2026): as 4 lacunas estão resolvidas e **remetem às seções deste arquivo** — era a edição única prevista.

## §7 — Notas e limitações

- **É estimativa, não medição** — parâmetros são **escolhas metodológicas** (🔴 heurística do projeto no caso das imagens); as **quantidades** (41 marcadores) vêm do inventário e são exatas.
- **Classificação visual feita sobre a cópia versionada** das imagens (`assets/images/ilustracoes/`) — é a **fonte oficial** do projeto; 2 marcadores do M2 não têm cópia versionada e serão classificados **por contexto** (declarado).
- **Nenhuma imagem** dos 39 está **dentro de atividade H5P** (verificado: o único arquivo com H5P é o `base/base.html`) → a anti-dupla-contagem nº 1 não incide em M1–M3.
- **Arquivos de imagem sem marcador** (observação de fidelidade do inventário — **não** entram nos 41): `M2P2L1p1-img-leitura-bebes.jpg` (a página `M2P2L1p1` tem **vídeo embedado**, não imagem) e `M2P3L1p2img-piscina.png` (**duplicata** da ilustração do trampolim de `M2P3L2p1`; a página `M2P3L1p2` não tem figura). Nenhum deles tem `[cole a imagem aqui]` → fora da contagem.
- **1 marcador sem cópia versionada** (`M2P1L1p2`): a página está **validada no Moodle** (a imagem existe lá), mas o arquivo **não está no repositório** — classificado por contexto e **declarado** na §1.2.
- **3 imagens não foram inspecionadas visualmente** — o leitor devolveu **"media omitted (limite de tamanho)"** em 2 tentativas: `M3P4L3p4-regimento.png`, `M3P4L3p5-plano_de_acao.png` e `Encontro_Sincrono_2_card.png`. A classificação usou o **`sr-only` da página + `descricoes.md`** (no ENC, também a **analogia com o card 1**, que foi visto) — **declarado** nas linhas 38, 39 e 41. Se houver divergência, a correção é de **1 linha** (ver §5).

