<!-- Registro interno do Ciclo 4 — calculo de carga horaria. Gerado por scripts/calculo-carga-horaria.py -->

# ⏱️ Cálculo de Carga Horária — Curso Vaga Lume

> **O que é:** planilha de cálculo (Ciclo 4) com **uma linha por página** no `.csv` companheiro e as **tabelas-resumo** aqui. Método: `tempo = quantidade × parâmetro × fator de cenário`.
> **Quantidades:** `inventario-recursos.csv` (147 páginas). **Parâmetros:** `parametros-carga-horaria.md` (Ciclo 2). **Ajustes finos:** `ajustes-finos.md` (Ciclo 3).
> **Buckets:** A = carga **obrigatória** · B = **opcional/complementar**. **Overhead de +10%** incide **somente** no cenário **recomendado**.
> **É ESTIMATIVA, não medição** (parâmetros são escolhas metodológicas; as quantidades são exatas).

---

## §1 — Totais gerais (4 cenários)

| Bucket | Mínimo | **Referência** | Máximo | **Recomendado** (+10%) |
|---|---|---|---|---|
| **A — obrigatória** | 15h52min29s | **22h20min42s** | 29h39min53s | **24h34min46s** |
| **B — opcional** | 4h58min45s | 5h23min32s | 6h45min55s | 5h55min53s |
| **A + B** | 20h51min14s | 27h44min14s | 36h25min48s | 30h30min39s |

> O **número principal do relatório é o bucket A** (carga obrigatória) — o B vai separado.

## §2 — Por módulo (cenário de referência)

| Módulo | Linhas | A ref | B ref | Total ref |
|---|---|---|---|---|
| M0 | 3 | 28min01s | 0s | 28min01s |
| M1 | 34 | 3h45min03s | 18min00s | 4h03min03s |
| M2 | 36 | 5h03min14s | 4min30s | 5h07min44s |
| M3 | 42 | 5h25min20s | 0s | 5h25min20s |
| M4 | 31 | 2h25min31s | 23min27s | 2h48min58s |
| Encontros Síncronos (página) | 1 | 3min32s | 3h07min35s | 3h11min07s |
| Encerramento *(estimado = M0)* | 1 | 28min01s | 0s | 28min01s |
| *(ajustes: navegação, encontros, gravação)* | 3 | 4h42min00s | 1h30min00s | 6h12min00s |

> A linha *(ajustes)* reúne o que não pertence a uma página (navegação de interface, encontros síncronos e 3ª gravação). O **Encerramento** é **estimado = M0** (ver §6). Módulos + Encerramento + ajustes fecham com o §1.

## §3 — Por categoria (cenário de referência)

| Categoria | Bucket | Quantidade | Ref | Mín | Máx |
|---|---|---|---|---|---|
| Leitura de textos | A | 26898 palavras | 2h54min45s | 1h47min42s | 4h29min03s |
| Imagens | A | 39 marcadores | 16min40s | 8min18s | 25min02s |
| Vídeos de conteúdo | A | 2h24min52s | 2h24min52s | 2h24min52s | 3h01min06s |
| Atividades H5P | A | 26 atividades | 2h16min00s | 1h08min00s | 3h24min00s |
| Fóruns | A | 14 fóruns | 7h55min00s | 4h40min00s | 10h30min00s |
| Navegação | A | 147 páginas + 24 interface | 1h25min30s | 42min45s | 2h08min15s |
| Textos externos | A | 1524 palavras | 9min54s | 6min06s | 15min14s |
| Encontros síncronos | A | 3 encontros | 4h30min00s | 4h30min00s | 4h30min00s |
| Bibliografia | B | 15 itens de texto | 22min30s | 7min30s | 45min00s |
| SDs em PDF | B | 3608 palavras | 23min27s | 14min25s | 36min04s |
| Gravações | B | 4h36min05s | 4h36min05s | 4h36min05s | 5h22min36s |
| Imagens (Encontros) | B | 2 cartazes | 1min30s | 45s | 2min15s |
| **Encerramento** *(estimado = M0)* | A | por analogia | 28min01s | 24min46s | 57min17s |
| **Total — bucket A** | A | | **22h20min42s** | **15h52min29s** | **29h39min53s** |

## §4 — Reconciliação com as âncoras do Ciclo 3 (sanidade)

| Âncora (Ciclo 3) | Esperado | Calculado (ref) | Confere? |
|---|---|---|---|
| Imagens (bucket A, M1-M3) | 16min40s | 16min40s | ✅ |
| Fóruns (bucket A, 13x35 + 1x20 min) | 7h55min00s | 7h55min00s | ✅ |
| Bibliografia (bucket B, 15 x 1,5 min) | 22min30s | 22min30s | ✅ |
| Imagens dos Encontros (bucket B) | 1min30s | 1min30s | ✅ |
| Textos externos (leitura pura, p/ ppm) | 7min37s | 7min37s | ✅ |

> O **estudo ativo (×1,3)** eleva os textos externos de 7min37s para 9min54s no cenário de referência (bucket A).

## §5 — Linhas de ajuste (itens que não são página)

| Item | Bucket | Ref | Obs |
|---|---|---|---|
| (ajuste) labels + frontpage | A | 12min00s | 21 labels + 3 frontpage x 30 s (parametros §5.8) |
| (ajuste) encontros sincronos (participacao) | A | 4h30min00s | 3 encontros x 1h30 (3º computado como executado — decisao do mestre) |
| (ajuste) 3ª gravacao do Encontro (declarada) | B | 1h30min00s | 3ª gravacao DECLARADA 1h30 (a confirmar) — as 2 no ar estao na pagina dos Encontros |
| (ajuste) Módulo de Encerramento (estimado = M0) | A | 28min01s | ESTIMADO = Módulo 0 (decisao do mestre, 15/10/2026) — a substituir pela medicao quando o modulo for produzido |

## §6 — Notas, decisões e limitações

1. **Páginas de fórum não entram na leitura** — o "ler instruções" já está dentro dos 35 min (20 no Boas-vindas). Anti-dupla-contagem.
2. **Vídeos da bibliografia** (21) → **18 já contados no bucket A** + 3 sugestões → **0 min** na bibliografia (princípio do Ciclo 3: não contar duas vezes).
3. **SDs em PDF** (bucket B): texto medido por `pdftotext` = 3608 palavras a 200 ppm. A **página** da SD conta no bucket A; o **PDF** no B.
4. **H5P — interpretação do parâmetro**: escolha única/múltipla/V-F = 1,5 min/questão; **associação/arrastar/desafio = 3 min/atividade**; virar cartões = 20 s/carta; caça-palavras = 5 min. A alternativa (3 min **por item** nos tipos complexos) está registrada no script.
5. **ESTUDO ATIVO (×1,3)** aplicado a toda a leitura (conteúdo, textos externos e SDs) no cenário de referência; ×1,0 no mínimo e ×1,5 no máximo.
6. **ENC — bloco novo dos encontros** (texto + imagem + vídeo, computado como executado pela decisão do mestre): **não incluído** por falta de quantidades (não produzido) — reincorporar na reexecução (§8 do `PLANO-carga-horaria.md`).
7. **3ª gravação do Encontro** sem duração publicada → adotada **1h30 (declarada)** para não subestimar; confirmar quando o encontro ocorrer.
8. **Módulo de Encerramento** (Certificação e Avaliação): **não produzido** — estimado **por analogia com o Módulo 0 (Boas-vindas)**, a pedido da coordenação (15/10/2026), para uma carga mais realista; a substituir pela **medição** na reexecução (§8).
9. **Navegação**: contadas as 147 páginas de conteúdo + 21 labels + 3 frontpage a 30 s (a §5.8 previa 146 páginas; a página dos Encontros soma +1).
10. **É estimativa, não medição** — sem relatórios de duração do Moodle (confirmado em 14/10/2026). Parâmetros: `parametros-carga-horaria.md`.
