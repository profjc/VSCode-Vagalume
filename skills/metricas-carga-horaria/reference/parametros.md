# Parâmetros de tempo — tabela de referência (com fontes)

> Tabela **reutilizável** de parâmetros de tempo para estimar carga horária. Cada linha traz
> **valor de referência**, **faixa (mín ↔ máx, em tempo)**, **nível de confiança** e **fonte**.
> Ajuste ao projeto (idioma, público, mídia) **mantendo o rótulo de confiança**.
> **Versão 1.1 (14/10/2026)** — projeto de origem: Vaga Lume.
> **Governança:** este arquivo é o **MÉTODO genérico** (a skill). Cada projeto mantém a sua **instanciação**
> — com as **decisões do cliente** — e cita a versão da skill usada. Mudou uma regra geral aqui?
> **Revalide a paridade** do script (`SKILL.md` → “Validação de paridade”).

## Convenções

| Símbolo | Significado |
|---|---|
| **ppm** | palavras por minuto (velocidade de leitura) |
| **ref.** | valor de **referência** (base do cenário "referência") |
| **mín ↔ máx** | faixa de **tempo**: *mín* = cenário mais rápido; *máx* = cenário mais lento |
| 🟢 / 🟡 / 🔴 | **científico** (com DOI) · **benchmark** · **heurística do projeto** |

## Tabela-mestra

| # | Categoria | Como medir (inventário) | **Referência** | Faixa mín ↔ máx | Conf. | Fonte |
|---|---|---|---|---|---|---|
| 1 | **Leitura de textos** | palavras visíveis | **200 ppm** | 250 ↔ 150 ppm | 🟢🟡 | F1–F4 |
| 2 | **Estudo ativo** (anotar, reler) | fator sobre a leitura | **×1,3** | ×1,0 ↔ ×1,5 | 🔴 | heurística |
| 3 | **Imagens** | nº de imagens, **por tipo** | simples **15 s** · tirinha/charge/cartaz **45 s** · gráfico/infográfico **90 s** · carrossel **20 s/imagem** | −50 % ↔ +50 % | 🔴 | heurística |
| 4 | **Vídeos de conteúdo** | duração real | **×1,0** | ×1,0 ↔ ×1,25 | 🟡🔴 | F5 |
| 5 | **Vídeos da bibliografia** | duração real | **×1,0** | — | 🟡 | F5 |
| 6 | **Atividades (quiz/H5P)** | nº de atividades + **nº de itens/questões** | escolha única/múltipla/V-F **1,5 min/questão** · associação/arrastar/desafio **3 min** · virar cartões **20 s/carta** · caça-palavras **5 min** | −50 % ↔ +50 % | 🟡 | F6–F7 |
| 7 | **Fóruns** | nº de fóruns (ciclo completo) | **35 min/fórum** | 20 ↔ 45 min | 🟡 | decisão do cliente |
| 8 | **Bibliografia** | nº de itens (**texto**) | **1,5 min/item** | 0,5 ↔ 3 min/item | 🔴 | heurística |
| 9 | **Navegação** | nº de páginas novas | **30 s/página** | 15 ↔ 45 s | 🔴 | heurística |
| 10 | **Encontros síncronos** | nº de encontros | **1h30/encontro** | — | 🟡 | duração prevista |
| 11 | **Gravações** (opcional) | duração | **×1,0** | — | 🟡 | — |
| 12 | **Anexos (PDF)** | nº de páginas | leitura a **200 ppm** | — | 🟢🔴 | F1–F4 |
| 13 | **Overhead** (cenário recomendado) | % sobre o total | **+10 %** | 0 ↔ +20 % | 🔴🟡 | F8 |

> **Nota:** a faixa "mín ↔ máx" é **de tempo**. Em leitura, **250 ppm** dá o **mínimo** de tempo e
> **150 ppm**, o **máximo**. Cálculo: `minutos = palavras ÷ ppm`.

---

## Classificação de imagens por tipo (como decidir)

O parâmetro de imagens depende do **tipo**, não só da quantidade. Classifique **olhando a imagem**
(nunca pelo nome do arquivo) e registre a contagem **por tipo** na planilha:

| Tipo | Como reconhecer | Tempo (ref.) | Exemplos do projeto de origem |
|---|---|---|---|
| **Foto / ilustração simples** | uma cena, sem texto a ler | **15 s** | fotografia de acervo, retrato de autor, cena de leitura |
| **Tirinha / charge / cartaz** | exige **ler a peça** (quadros, legenda, piada) | **45 s** | tirinhas da Magali, do Quino, da Stahler; cartaz de divulgação |
| **Gráfico / infográfico / linha do tempo** | há dados ou hierarquia a interpretar | **90 s** | gráficos, infográficos, esquemas com etapas |
| **Carrossel / imagem sequencial** | várias imagens no mesmo bloco | **20 s por imagem** | carrossel de 5 retratos (`M1P1L1p4`) |

**Regras de decisão:**

1. **Tirinha e cartaz contam mais que uma foto** — ler a peça faz parte do conteúdo; é o tipo mais subestimado.
2. **Imagem dentro de H5P** (ex.: cartas de arrastar, imagens de quiz) já está coberta pelo **item da
   atividade** — **não** conte de novo como imagem de página (anti-dupla-contagem nº 1).
3. **Ícones de interface, logos, tiles e banners de navegação** **não** são conteúdo.
4. **Na dúvida entre dois tipos, adote o mais lento** (regra de segurança do Passo 2).
5. Registre a classificação (mesmo que só na planilha): sem isso, **a próxima reexecução classifica
   diferente** e o número muda sem o curso ter mudado.

## Fontes

**F1. Brysbaert (2019)** — leitura **silenciosa ≈ 238 ppm** (não ficção) e **260 ppm** (ficção);
faixa **175–300 ppm**; em voz alta ≈ 183 ppm.
BRYSBAERT, Marc. *How many words do we read per minute? A review and meta-analysis of reading rate*.
Journal of Memory and Language, v. 109, art. 104047, 2019. DOI: 10.1016/j.jml.2019.104047.

**F2. Ziefle (1998)** — **200 ppm no papel × 180 ppm no monitor**.
ZIEFLE, Martina. *Effects of display resolution on visual performance*. Human Factors, v. 40, n. 4,
p. 554–568, 1998. DOI: 10.1518/001872098779649355.

**F3. IReST (2012)** — leitura **em voz alta: 184 ± 29 ppm** em 17 idiomas.
TRAUZETTEL-KLOSINSKI, Susanne; DIETZ, Klaus; IReST Study Group. *Standardized Assessment of Reading
Performance: The New International Reading Speed Texts IReST*. IOVS, v. 53, n. 9, p. 5452–5461, 2012.
DOI: 10.1167/iovs.11-8284.

**F4. Komeno & Ávila et al. (2015) — estudo brasileiro (português)** — leitura **oral** de alunos do
9º ano variou **~96–219 ppm**; a **silenciosa foi maior** que a oral; os autores pedem parâmetros
brasileiros por idade/escolaridade.
KOMENO, Eliana Matiko; ÁVILA, Clara Regina Brandão de; et al. *Velocidade de leitura e desempenho
escolar na última série do ensino fundamental*. Estudos de Psicologia (Campinas), v. 32, n. 3, 2015.
DOI: 10.1590/0103-166x2015000300009.

**F5. Chen et al. (2024)** — **assistir × assistir anotando**: anotar durante o vídeo afeta o
processamento, mas **não há multiplicador canônico** → por isso o fator ×1,25 é 🔴 heurística.
CHEN, Ouhao; et al. *The effects of lecture speed and note-taking on memory for educational material*.
Applied Cognitive Psychology, 2024. DOI: 10.1002/acp.4166.

**F6. University of Alberta — Centre for Teaching and Learning** — "**≈ 60 segundos por questão**"
de múltipla escolha (FAQs about Assessment). https://www.ualberta.ca/en/centre-for-teaching-and-learning/

**F7. PDFQuiz (mercado)** — **30–60 s** por questão de MC/V-F; **1–2 min** por resposta curta.
https://pdfquiz.com

**F8. Pomodoro** — **25 min de foco + 5 min de pausa** (Cirillo); Biwer et al. (2023), British Journal
of Educational Psychology, DOI 10.1111/bjep.12593; Ogut (2025), BMC Medical Education, DOI
10.1186/s12909-025-08001-0. **Uso:** justifica o **overhead** (25+5 ≈ 20 % de pausa; adotar **10 %**
é conservador).

---

## Notas de ajuste (ao adaptar a outro projeto)

- **Idioma/ortografia:** a velocidade depende do comprimento médio das palavras; em português,
  **200 ppm** é um referencial conservador para **leitura em tela** por adulto não especialista.
- **Público:** especialistas leem mais rápido; pessoas com menor escolaridade, mais devagar —
  ajuste entre as pontas **150/250 ppm** e **documente**.
- **Fóruns:** decomponha o **ciclo completo** exigido (ler instruções · escrever · ler colegas ·
  responder) e registre a decisão.
- **Atividades:** conte os **itens** lidos do `content.json` do pacote H5P; tipos mais complexos
  valem mais tempo.
- **Vídeos:** use a **duração real**; não estime "no escuro". Trechos contam **só o trecho**.
- **Nunca** use valor sem rótulo de confiança nem sem fonte — 🔴 é aceitável, **desde que declarado**.
