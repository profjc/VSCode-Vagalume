<!-- ╔══════════════════════════════════════════════════════════════════════════╗ -->
<!-- ║  PARÂMETROS DE CARGA HORÁRIA — PROJETO VAGA LUME (Moodle 4.5)           ║ -->
<!-- ║  Criado em 14/10/2026 — Ciclo 2 do relatório de carga horária            ║ -->
<!-- ║  Companheiros: PLANO-carga-horaria.md · inventario-recursos.md/.csv      ║ -->
<!-- ║  Documento vivo: reexecutar quando o Módulo de Encerramento chegar       ║ -->
<!-- ╚══════════════════════════════════════════════════════════════════════════╝ -->

# ⏱️ Parâmetros de Carga Horária — Curso Vaga Lume

> **O que é:** tabela-mestra dos **parâmetros de tempo** do relatório de carga horária — cada um com **valor de referência**, **faixa mín ↔ máx** (em tempo), **nível de confiança** e **fonte citada**.
> **Como usar:** o cálculo aplica `tempo = quantidade × parâmetro × fator de cenário` (`PLANO-carga-horaria.md` §4.1). Aqui ficam os **parâmetros**; as **quantidades** vêm de `inventario-recursos.md`/`.csv` (uma linha por página).
> **Status:** fixado no **Ciclo 2** (14/10/2026), incluindo as **4 decisões do mestre** (§6).
> **Governança (14/10/2026):** este documento é a **INSTANCIAÇÃO do projeto**; o **método genérico** —
> com os mesmos parâmetros, fontes e rótulos de confiança — vive na skill **`skills/metricas-carga-horaria/`**
> (`SKILL.md` · `reference/parametros.md`). Mudou um parâmetro aqui? Registre a **decisão do mestre**;
> se a mudança for **regra geral**, proponha a atualização da skill e **rode a validação de paridade** do script.

---

## §1 — Natureza e princípios

1. **É ESTIMATIVA, não medição.** Não existem relatórios de conclusão/duração do Moodle (confirmado pelo mestre, 14/10/2026).
2. **Parâmetro ≠ quantidade.** As quantidades são **exatas e rastreáveis** (arquivo, página, pacote H5P); os tempos são **parâmetros**.
3. **Três níveis de confiança** (declarados em cada linha da tabela):
   - 🟢 **Científico** — estudo publicado/revisado (com DOI).
   - 🟡 **Benchmark** — referência institucional ou prática consolidada de mercado.
   - 🔴 **Heurística do projeto** — decisão do projeto, **sem fonte canônica**; a derivação é sempre explicitada.
4. **Honestidade metodológica:** nenhum número é apresentado como "ciência" quando não é — o relatório final reproduz essa rotulagem.

## §2 — Convenções e unidades

| Símbolo | Significado |
|---|---|
| **ppm** | palavras por minuto (velocidade de leitura) |
| **ref.** | valor de **referência** (base do cenário "referência") |
| **mín ↔ máx** | faixa de **tempo**: *mín* = cenário mais rápido (menos tempo); *máx* = cenário mais lento (mais tempo) |
| **fator de cenário** | multiplicador sobre o valor de referência (plano §4.3) |

## §3 — Âncora interna do curso (por que o Pomodoro)

A única orientação de tempo que **o próprio curso** oferece ao aluno está na página **"Dicas para se organizar"** (Boas-vindas, `templates/pages/Boas-vindas/Boas-vindas_Dicas_para_se_organizar.html`):

- **Dica 3 — "Faça pausas":** "não precisa concluir todo o conteúdo de uma só vez… intercale os momentos de estudo com pequenas pausas".
- **Estratégia 1 — Método Pomodoro:** "dedique **25 minutos** ao curso, faça uma pausa de **5 minutos** e depois retome".

**Uso no relatório:** fundamenta o **overhead de estudo** (§5.11). O Pomodoro (25 + 5) implica **~20 %** de tempo em pausa; o overhead adotado de **10 %** é **metade** disso — conservador. Fontes: Cirillo (Pomodoro Technique); Biwer et al. (2023), *BJEP*; Ogut (2025), *BMC Medical Education*.

## §4 — Tabela-mestra de parâmetros

| # | Categoria | Unidade medida (inventário) | **Referência** | Faixa mín ↔ máx | Conf. | Fundamento |
|---|---|---|---|---|---|---|
| 1 | **Leitura de textos** | palavras visíveis por página | **200 ppm** | 250 ppm ↔ 150 ppm | 🟢🟡 | §5.1 |
| 2 | **Estudo ativo** (anotar, reler) | fator sobre a leitura | **×1,3** | ×1,0 ↔ ×1,5 | 🔴 | §5.2 |
| 3 | **Imagens** | nº de imagens, por tipo | simples **15 s** · tirinha/charge/cartaz **45 s** · gráfico/infográfico **90 s** · carrossel **20 s/imagem** | −50 % ↔ +50 % | 🔴 | §5.3 |
| 4 | **Vídeos de conteúdo** (bucket A) | duração real (créditos das páginas) | **×1,0** | ×1,0 ↔ ×1,25 | 🟡🔴 | §5.4 |
| 5 | **Vídeos da bibliografia** (bucket B) | duração real | **×1,0** | — | 🟡 | §5.4 |
| 6 | **Atividades H5P** | nº de atividades + nº de itens/questões lidos do `content.json` | escolha única/múltipla/V-F **1,5 min/questão** · associação/arrastar/desafio de palavras **3 min** · virar cartões **20 s/carta** · caça-palavras **5 min** | −50 % ↔ +50 % | 🟡 | §5.5 |
| 7 | **Fóruns** | nº de fóruns (14) | **35 min/fórum** | 20 ↔ 45 min | 🟡 | §5.6 |
| 8 | **Bibliografia** (bucket B) | nº de itens (38; 21 são vídeos) | **1,5 min/item** (itens de **texto**) | 0,5 ↔ 3 min/item | 🔴 | §5.7 |
| 9 | **Navegação** | páginas (146) + labels (21) + frontpage (3) | **30 s por página nova** | 15 ↔ 45 s | 🔴 | §5.8 |
| 10 | **Encontros síncronos** | nº de encontros (3) | **1h30 por encontro** | — | 🟡 | §5.9 |
| 11 | **Gravações dos encontros** (bucket B) | duração (1h26min36 + 1h39min29 + 3º) | **×1,0** | — | 🟡 | §5.9 |
| 12 | **SDs em PDF** (bucket B) | nº de PDFs (13) e páginas de cada um | leitura a **200 ppm** sobre o texto do PDF | — | 🟢🔴 | §5.10 |
| 13 | **Overhead de estudo** (cenário recomendado) | % sobre o total | **+10 %** | 0 ↔ +20 % | 🔴🟡 | §5.11 |

> **Nota:** a faixa "mín ↔ máx" é **de tempo**. Ex.: em leitura, **250 ppm** produz o **mínimo** de tempo (leitura rápida) e **150 ppm**, o **máximo**.

---

## §5 — Fundamentação por parâmetro

### §5.1 Leitura de textos — **200 ppm** (ref.)

| Referência | Dado | Fonte |
|---|---|---|
| Brysbaert (2019) — meta-análise | leitura **silenciosa ≈ 238 ppm** (não ficção), **260 ppm** (ficção); **faixa 175–300 ppm**; em voz alta **≈ 183 ppm** | Brysbaert, M. (2019). *Journal of Memory and Language*, 109, 104047. DOI `10.1016/j.jml.2019.104047` |
| Ziefle (1998) | **200 ppm no papel × 180 ppm no monitor** | Ziefle, M. (1998). *Human Factors*, 40(4), 554–568. DOI `10.1518/001872098779649355` |
| IReST (2012) — 17 idiomas | leitura **em voz alta: 184 ± 29 ppm** | Trauzettel-Klosinski, S., & Dietz, K. (2012). *IOVS*, 53(9), 5452–5461. DOI `10.1167/iovs.11-8284` |
| Komeno, Ávila et al. (2015) — **Brasil / português** | leitura **oral** do 9º ano variou **~96–219 ppm**; a **silenciosa foi maior** que a oral; os autores pedem parâmetros brasileiros por idade/escolaridade | *Estudos de Psicologia (Campinas)*, 32(3), 2015. DOI `10.1590/0103-166x2015000300009` |

**Decisão (ver §6d):** adotar **200 ppm** como referência, e não os **238 ppm** da meta-análise. Motivos: (i) o curso é lido **em tela** (180 ppm, Ziefle); (ii) o público é **adulto não especialista** (mediadores de leitura comunitários), com escolaridade variada; (iii) 200 ppm é **conservador** — produz estimativa **maior**, nunca menor. Pontas: **250 ppm** (cenário rápido — abaixo do teto de 300 ppm de não ficção) e **150 ppm** (cenário lento). Cálculo: `minutos = palavras ÷ ppm`.

### §5.2 Estudo ativo (anotar, reler) — **×1,3** (ref.)

Não há fonte canônica para "quanto tempo a mais" o aluno gasta anotando/relando. A heurística ancora-se nas **estratégias do próprio curso** (§3): Pomodoro, pausas e "explique com suas próprias palavras". Faixa: **×1,0** (leitura corrida) ↔ **×1,5** (anotação + releitura). Confiança: 🔴 heurística.

### §5.3 Imagens — **15 s / 45 s / 90 s / 20 s por imagem**

Tempo de permanência (*dwell*) por tipo, para "observar e analisar": leitura simples **15 s**; tirinha/charge/cartaz **45 s**; gráfico/infográfico **90 s**; cada imagem de carrossel **20 s**. Faixa **−50 % ↔ +50 %**. **Não há fonte canônica** — a classificação das 39 imagens por tipo é o ajuste fino do **Ciclo 3**. Confiança: 🔴 heurística.

### §5.4 Vídeos — **duração real ×1,0** (ref.); **×1,25** no máximo

O valor de referência é a **duração real** do vídeo (as minutagens estão nos créditos das próprias páginas — não é preciso consultar o YouTube para os 17 vídeos de conteúdo). O cenário máximo aplica **×1,25**, para cobrir pausas, trechos revistos e **anotação durante o vídeo**. Chen et al. (2024, *Applied Cognitive Psychology*, DOI `10.1002/acp.4166`) estudam exatamente **assistir × assistir anotando** — mas **não fornecem multiplicador canônico**; por isso o fator é heurístico. Vídeos da **bibliografia** (bucket B) usam o mesmo ×1,0 (e **não** o "1,5 min/item" de texto). Confiança: 🟡 na duração / 🔴 no fator.

### §5.5 Atividades H5P — **1,5 min/questão** (ref.)

| Referência | Dado | Fonte |
|---|---|---|
| University of Alberta — Centre for Teaching and Learning | "**≈ 60 segundos (1 minuto) por questão**" de múltipla escolha | ualberta.ca → *FAQs about Assessment* |
| PDFQuiz (mercado) | **30–60 s** por questão de múltipla escolha/V-F; **1–2 min** por resposta curta | pdfquiz.com → *How Long Should a Quiz Be?* |

**Decisão:** **1,5 min/questão** para escolha única, múltipla escolha e verdadeiro/falso — ligeiramente **acima** do benchmark de 60 s porque o público é adulto não especialista e o valor inclui ler o enunciado, pensar e conferir. Interações mais complexas: **associação, arrastar/deslizar e desafio de palavras = 3 min**; **virar cartões = 20 s/carta**; **caça-palavras = 5 min** (a página verbaliza "5 min"). Base quantitativa: **110 itens** em 26 atividades (`inventario-recursos.md` §3). Confiança: 🟡.

### §5.6 Fóruns — **35 min/fórum** (ref.)

Decomposição (decisão do mestre, 14/10/2026): **5 min** ler as instruções + **20 min** escrever a postagem + **10 min** ler as contribuições dos colegas e **responder a pelo menos dois**. Faixa **20 ↔ 45 min**. O tempo é **por fórum** (o enunciado descreve o ciclo completo), não por postagem — ver §7. Os **materiais de estudo de caso do fórum** (vídeo + artigo) são tratados na §6b/§7 para não duplicar. Confiança: 🟡.

### §5.7 Bibliografia — **1,5 min/item** (ref., itens de texto)

**Heurística do projeto** (sem fonte canônica), com derivação explícita: para um item de texto, **ler título + resumo** (~200 palavras ÷ 200 ppm ≈ **1 min**) + **decidir** se aprofunda (~**30 s**) ≈ **1,5 min**. Faixa **0,5 ↔ 3 min/item**. Regras: (i) **itens que são vídeo** entram por **duração real** (×1,0), não pelo 1,5 min; (ii) itens **já contados no bucket A** (sobreposição) **não somam de novo**. Universo: **38 itens**, dos quais **21 são vídeos** (16 já contados no tempo efetivo + 5 como sugestão). Confiança: 🔴.

### §5.8 Navegação — **30 s por página nova** (ref.)

Custo de transição (rolar, localizar o "Próximo", esperar o carregamento, orientar-se) por **página nova**: **30 s**; faixa **15 ↔ 45 s**. Aplicado a **146 páginas** de conteúdo + **21 labels** + **3 frontpage** (labels e frontpage entram **apenas** como navegação — §7). Confiança: 🔴.

### §5.9 Encontros síncronos — **1h30 por encontro**

**Participação** no encontro: **1h30** (duração prevista). **3 encontros** (o 3º computado como executado, decisão de 14/10/2026). As **gravações** (1h26min36 + 1h39min29 + a do 3º) ficam no **bucket B** (opcional), por **×1,0** da duração. Confiança: 🟡.

### §5.10 SDs em PDF (bucket B) — **leitura a 200 ppm**

As **13 Sequências Didáticas** (PDFs A4 de 1–2 páginas) são lidas a **200 ppm** (§5.1) sobre o **texto do PDF**. Regra anti-dupla-contagem: a **página** da SD no curso conta no bucket A; o **PDF** conta no bucket B — **nunca os dois no mesmo bucket**. Confiança: 🟢/🔴.

### §5.11 Overhead de estudo (cenário recomendado) — **+10 %**

Percentual acrescido ao **cenário recomendado** para cobrir pausas, retomadas e espera por feedback do fórum. Ancorado no Pomodoro do próprio curso (§3): 25 + 5 ⇒ **~20 %** de pausa; **10 %** é conservador (metade). **Confirmado pelo mestre em 14/10/2026 (decisão §6a).** Faixa considerada: **0 ↔ +20 %**. **Não incide** sobre os cenários mínimo e máximo — apenas sobre o recomendado.

---

## §6 — Decisões do mestre (Ciclo 2 · 14/10/2026)

| # | Questão | **Decisão** | Fundamento |
|---|---|---|---|
| **a** | Overhead do cenário recomendado | **CONFIRMADO: 10 %** | Pomodoro 25+5 (≈20 % de pausa); 10 % é conservador — §5.11 |
| **b** | Artigo do **Fórum 4 do M1** ("Da alimentação à poesia…", Fundação Telefônica Vivo) | **LEITURA COMPUTADA (bucket A)** | É o **estudo de caso obrigatório** do fórum ("leia o artigo", `templates/pages/M1/Parte4/M1P4F1.html`); consistente com a régua "vídeo instruído conta". **Medir o texto real do artigo no Ciclo 3** |
| **c** | "Consultar a bibliografia" (38 itens) | **MANTER 1,5 min/item** (itens de texto) | Heurística explícita — §5.7; itens de vídeo por duração real; sobreposição não soma |
| **d** | Velocidade de leitura-alvo | **200 ppm** (ref.) · **150/250 ppm** (pontas) | Conservador para leitura em tela e público não especialista — §5.1 |

## §7 — Aplicação e regras anti-dupla-contagem

1. `tempo = quantidade × parâmetro (× fator de cenário)` — cálculo **página a página**, agregado por **parte**, **módulo**, **categoria** e **bucket**.
2. **Página da SD × PDF da SD:** página → bucket A; PDF → bucket B. Nunca somar os dois.
3. **Vídeo que está na bibliografia e também no conteúdo:** contado **uma vez**, no bucket A. A bibliografia registra o item + a nota de sobreposição.
4. **Labels e frontpage:** apenas **navegação** (não são leitura de conteúdo).
5. **Páginas de abertura, síntese e referências:** leitura normal (bucket A).
6. **Fórum:** valor **por fórum** (ciclo completo), não por postagem.
7. **Bloco novo dos encontros + 3º encontro:** computados como executados, com os parâmetros dos encontros anteriores.
8. **Estudo de caso do fórum (vídeo + artigo):** o **vídeo** entra no bucket A pela regra "vídeo instruído conta"; o **artigo** entra no bucket A como **leitura computada** (§6b) — em ambos os casos **sem** somar de novo o "ler instruções" do fórum.

## §8 — Lacunas e pendências (a resolver no Ciclo 3)

- **Imagens:** classificar as **39** por tipo (foto, tirinha, gráfico, carrossel) — a classificação altera o parâmetro (§5.3).
- **Fóruns:** confirmar se **todos os 14** enunciados exigem o mesmo ciclo (postar · ler colegas · responder a dois) — havendo exceção, registrá-la.
- **Bibliografia:** cruzar **1:1** os 21 itens de vídeo com os vídeos do curso (16 já batidos) e buscar as **durações faltantes**; sem match seguro, marcar "duração não localizada" (não estimar no escuro).
- **Artigo do Fórum 4 do M1 (decisão b):** medir o **comprimento real** do texto (para aplicar 200 ppm).
- **Sem fonte canônica:** estudo ativo (§5.2), imagens (§5.3), fator de vídeo anotando (§5.4), bibliografia (§5.7) e navegação (§5.8) — todos rotulados 🔴.

---

## §9 — Referências citadas (acesso em 14/10/2026)

**Científicas**

1. BRYSBAERT, Marc. **How many words do we read per minute? A review and meta-analysis of reading rate**. *Journal of Memory and Language*, v. 109, art. 104047, 2019. DOI: 10.1016/j.jml.2019.104047.
2. TRAUZETTEL-KLOSINSKI, Susanne; DIETZ, Klaus; IReST Study Group. **Standardized Assessment of Reading Performance: The New International Reading Speed Texts IReST**. *Investigative Ophthalmology & Visual Science*, v. 53, n. 9, p. 5452–5461, 2012. DOI: 10.1167/iovs.11-8284.
3. ZIEFLE, Martina. **Effects of display resolution on visual performance**. *Human Factors*, v. 40, n. 4, p. 554–568, 1998. DOI: 10.1518/001872098779649355.
4. KOMENO, Eliana Matiko; ÁVILA, Clara Regina Brandão de; et al. **Velocidade de leitura e desempenho escolar na última série do ensino fundamental**. *Estudos de Psicologia (Campinas)*, v. 32, n. 3, 2015. DOI: 10.1590/0103-166x2015000300009.
5. CHEN, Ouhao; et al. **The effects of lecture speed and note-taking on memory for educational material**. *Applied Cognitive Psychology*, 2024. DOI: 10.1002/acp.4166.
6. BIWER, Felicitas; et al. **Understanding effort regulation: Comparing 'Pomodoro' breaks and self-regulated breaks**. *British Journal of Educational Psychology*, v. 93, n. S2, p. 353–367, 2023. DOI: 10.1111/bjep.12593.
7. OGUT, Eren. **Assessing the efficacy of the Pomodoro technique in enhancing anatomy lesson retention during study sessions: a scoping review**. *BMC Medical Education*, v. 25, art. 1440, 2025. DOI: 10.1186/s12909-025-08001-0.

**Benchmarks e âncoras**

8. UNIVERSITY OF ALBERTA. Centre for Teaching and Learning. **FAQs about Assessment** — "≈ 60 segundos por questão de múltipla escolha". Disponível em: https://www.ualberta.ca/en/centre-for-teaching-and-learning/teaching-support/assessment/faqs.html.
9. PDFQUIZ. **How Long Should a Quiz Be? Ideal Question Count** — 30–60 s (MC/V-F); 1–2 min (resposta curta). Disponível em: https://pdfquiz.com.
10. CIRILLO, Francesco. **The Pomodoro Technique** — 25 min de foco + 5 min de pausa.
11. VAGA LUME (curso). **"Dicas para se organizar"** — página-âncora interna (`templates/pages/Boas-vindas/Boas-vindas_Dicas_para_se_organizar.html`).

## §10 — Histórico

| Data | Mudança |
|---|---|
| **14/10/2026** | **Ciclo 2** — criação do documento: tabela-mestra de parâmetros (§4), fundamentação e fontes citadas (§5), as 4 decisões do mestre (§6), regras anti-dupla-contagem (§7), lacunas (§8) e referências (§9). Pesquisa na internet autorizada pelo mestre (14/10/2026). |
