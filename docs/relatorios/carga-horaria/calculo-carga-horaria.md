<!-- Registro interno do Ciclo 4 — calculo de carga horaria. Gerado por scripts/calculo-carga-horaria.py -->

# ⏱️ Cálculo de Carga Horária — Curso Vaga Lume

> **O que é:** planilha de cálculo (Ciclo 4) com **uma linha por página** no `.csv` companheiro e as **tabelas-resumo** aqui. Método: `tempo = quantidade × parâmetro × fator de cenário`.
> **Quantidades:** `inventario-recursos.csv` (todas as páginas do curso, medidas no inventário de 25/11/2026). **Parâmetros:** `parametros-carga-horaria.md` (Ciclo 2). **Ajustes finos:** `ajustes-finos.md` (Ciclo 3 + reexecução de 25/11/2026, inclusive as atividades do M5).
> **Buckets:** A = carga **obrigatória** · B = **opcional/complementar**. **Overhead de +10%** incide **somente** no cenário **recomendado**.
> **É ESTIMATIVA, não medição** (parâmetros são escolhas metodológicas; as quantidades são exatas).

---

## §1 — Totais gerais (4 cenários)

| Bucket | Mínimo | **Referência** | Máximo | **Recomendado** (+10%) |
|---|---|---|---|---|
| **A — obrigatória** | 16h31min41s | **23h19min09s** | 30h37min57s | **25h39min04s** |
| **B — opcional** | 4h56min12s | 5h21min13s | 7h05min37s | 5h53min20s |
| **A + B** | 21h27min53s | 28h40min22s | 37h43min34s | 31h32min24s |

> O **número principal do relatório é o bucket A** (carga obrigatória) — o B vai separado.

## §2 — Por módulo (cenário de referência)

| Módulo | Linhas | A ref | B ref | Total ref |
|---|---|---|---|---|
| M0 | 3 | 28min01s | 0s | 28min01s |
| M1 | 34 | 3h45min03s | 18min00s | 4h03min03s |
| M2 | 36 | 5h03min14s | 4min30s | 5h07min44s |
| M3 | 42 | 5h25min20s | 0s | 5h25min20s |
| M4 | 31 | 2h31min34s | 23min04s | 2h54min38s |
| M5 — Encerramento (medido) | 11 | 47min20s | 0s | 47min20s |
| Encontros Síncronos (página) | 1 | 5min07s | 4h35min39s | 4h40min46s |
| *(ajustes M5: atividades de conclusão)* | 4 | 30min00s | 0s | 30min00s |
| *(ajustes: navegação e encontros)* | 2 | 4h43min30s | 0s | 4h43min30s |

> As linhas *(ajustes)* reúnem o que não pertence a uma página: navegação de interface, encontros síncronos (participação) e as atividades de conclusão do M5 (questionário do Forms, preenchimento do Plano de Ação, envio da Tarefa e Certificado). O **Encerramento agora é MEDIDO** (11 páginas) — a estimativa por analogia com o M0 foi substituída pela medição. Módulos + ajustes fecham com o §1.

## §3 — Por categoria (cenário de referência)

| Categoria | Bucket | Quantidade | Ref | Mín | Máx |
|---|---|---|---|---|---|
| Leitura de textos | A | 32677 palavras | 3h32min20s | 2h10min49s | 5h26min47s |
| Imagens | A | 67 marcadores | 25min40s | 12min50s | 38min30s |
| Vídeos de conteúdo | A | 2h27min45s | 2h27min45s | 2h27min45s | 3h04min42s |
| Atividades H5P | A | 26 atividades | 2h16min00s | 1h08min00s | 3h24min00s |
| Fóruns | A | 14 fóruns | 7h55min00s | 4h40min00s | 10h30min00s |
| Navegação | A | 158 páginas + 27 interface | 1h32min30s | 46min15s | 2h18min45s |
| Textos externos | A | 1524 palavras | 9min54s | 6min06s | 15min14s |
| Encontros síncronos | A | 3 encontros | 4h30min00s | 4h30min00s | 4h30min00s |
| Bibliografia | B | 15 itens de texto | 22min30s | 7min30s | 45min00s |
| SDs em PDF | B | 3548 palavras | 23min04s | 14min10s | 35min29s |
| Gravações | B | 4h33min24s | 4h33min24s | 4h33min24s | 5h41min45s |
| Imagens (Encontros) | B | 3 cartazes | 2min15s | 1min08s | 3min22s |
| Atividades de conclusão do M5 | A | 4 atividades | 30min00s | 30min00s | 30min00s |
| **Total — bucket A** | A | | **23h19min09s** | **16h31min41s** | **30h37min57s** |

## §4 — Reconciliação com as âncoras do Ciclo 3 (sanidade)

| Âncora (Ciclo 3) | Esperado | Calculado (ref) | Confere? |
|---|---|---|---|
| Imagens (bucket A, M1-M5) | 25min40s | 25min40s | ✅ |
| Fóruns (bucket A, 13x35 + 1x20 min) | 7h55min00s | 7h55min00s | ✅ |
| Bibliografia (bucket B, 15 x 1,5 min) | 22min30s | 22min30s | ✅ |
| Imagens dos Encontros (bucket B) | 2min15s | 2min15s | ✅ |
| Textos externos (leitura pura, p/ ppm) | 7min37s | 7min37s | ✅ |

> O **estudo ativo (×1,3)** eleva os textos externos de 7min37s para 9min54s no cenário de referência (bucket A).

## §5 — Linhas de ajuste (itens que não são página)

| Item | Bucket | Ref | Obs |
|---|---|---|---|
| (ajuste) labels + frontpage | A | 13min30s | 24 labels + 3 frontpage x 30 s (parametros §5.8) |
| (ajuste) encontros sincronos (participacao) | A | 4h30min00s | 3 encontros x 1h30 (3º computado como executado — decisao do mestre) |
| (ajuste) M5 - Questionario da Avaliacao do curso (Microsoft Forms) | A | 10min00s | decisao do mestre (25/11/2026): 10 min para o questionario embedado |
| (ajuste) M5 - PDF do Plano de Acao (preenchimento) | A | 15min00s | heuristica declarada: 2 atividades x 6 campos (~75 s/campo) - formulario de 1 pagina |
| (ajuste) M5 - Tarefa: foto do plano + envio | A | 3min00s | heuristica declarada: fotografar e anexar o plano (operacional da Tarefa) |
| (ajuste) M5 - Certificado de Conclusao (emissao/download) | A | 2min00s | heuristica declarada: gerar e baixar o PDF do certificado |

## §6 — Notas, decisões e limitações

1. **Páginas de fórum não entram na leitura** — o "ler instruções" já está dentro dos 35 min (20 no Boas-vindas). Anti-dupla-contagem.
2. **Vídeos da bibliografia** (21) → **18 já contados no bucket A** + 3 sugestões → **0 min** na bibliografia (princípio do Ciclo 3: não contar duas vezes).
3. **SDs em PDF** (bucket B): texto medido por `pdftotext` = 3548 palavras a 200 ppm. A **página** da SD conta no bucket A; o **PDF** no B.
4. **H5P — interpretação do parâmetro**: escolha única/múltipla/V-F = 1,5 min/questão; **associação/arrastar/desafio = 3 min/atividade**; virar cartões = 20 s/carta; caça-palavras = 5 min. A alternativa (3 min **por item** nos tipos complexos) está registrada no script.
5. **ESTUDO ATIVO (×1,3)** aplicado a toda a leitura (conteúdo, textos externos e SDs) no cenário de referência; ×1,0 no mínimo e ×1,5 no máximo.
6. **ENC — bloco dos encontros REINCORPORADO** (25/11/2026): a página dos Encontros tem agora **3 gravações** (4h33min24s reais, bucket B), **3 cartazes** (135 s, bucket B) e 710 palavras de texto (bucket A); as **3 participações** de 1h30 estão na linha de ajuste (bucket A).
7. **3ª gravação do Encontro**: duração **real 1h27min19s**, lida nos créditos da página (não mais a 1h30 declarada) — a antiga linha de ajuste foi removida para não contar duas vezes.
8. **Módulo 5 (Encerramento) agora é MEDIDO**: 11 páginas (1 abertura + 10 de conteúdo), 24 fotos em 4 carrosséis (20 s/imagem) e 1 vídeo de 2min53s; as **4 atividades de conclusão** entram em linhas de ajuste — questionário do Forms 10 min (decisão do mestre, 25/11/2026), preenchimento do PDF do Plano de Ação 15 min, foto + envio da Tarefa 3 min e emissão do Certificado 2 min. A **estimativa por analogia com o M0 foi substituída pela medição**.
9. **Navegação**: 158 páginas de conteúdo + 24 labels (arquivos em `templates/pages/labels/`) + 3 frontpage a 30 s.
10. **É estimativa, não medição** — sem relatórios de duração do Moodle (confirmado em 14/10/2026). Parâmetros: `parametros-carga-horaria.md`.
