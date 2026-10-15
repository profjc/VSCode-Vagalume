# Armadilhas e lições aprendidas

> O que costuma dar errado nestas métricas — e como evitar. **Versão 1.2 (15/10/2026)** —
> origem: projeto Vaga Lume.

1. **Apresentar heurística como ciência.** Sempre rotular 🟢/🟡/🔴. Um número sem fonte **é
   aceitável**, desde que declarado **"heurística do projeto"** com a derivação explícita.
2. **Dupla contagem.** Aplique as 7 regras de `metodo-e-cenarios.md` §4. É o erro mais frequente e
   o que mais distorce o total.
3. **Estimar duração "no escuro".** Se a duração de um vídeo não foi localizada, marcar
   **"duração não localizada"** — não inventar.
4. **Esquecer o bucket opcional.** Sem separar obrigatório × opcional, o número principal infla e o
   relatório perde credibilidade.
5. **Contar fórum por postagem.** É **por fórum**, com o **ciclo completo** (ler · escrever · ler
   colegas · responder).
6. **Contar vídeo sugerido.** "Quer saber mais?" / itens de bibliografia **não** entram no tempo efetivo.
7. **Abrir arquivo de relatório no editor com o comando que rouba o foco (lição de 14/10/2026).**
   Abrir `.md`/`.csv` de relatório com `code` **reativa a aba e puxa o foco do teclado** — já fez o
   usuário digitar num arquivo errado. **Regra:** relatórios ficam no disco; a entrega na janela
   ativa fica restrita às **páginas HTML do curso**. Se abrir por engano: conferir a integridade em
   disco (`diff`/`md5sum`) e **descartar a aba** (nunca salvar).
8. **Não versionar as decisões do cliente.** Registre numa tabela (fórum = X min, overhead = Y %,
   leitura = Z ppm...); sem isso, **a discussão se repete** em cada reexecução.
9. **Curso mudou e o relatório não.** Reexecute o inventário e recalcule quando entrar módulo/atividade nova.
10. **Contar labels/rótulos como leitura de conteúdo.** Não são — entram só na navegação.
11. **Esquecer de declarar "estimativa, não medição".** O relatório precisa dizer o que é e o que não é.
12. **Confundir parâmetro com quantidade.** Quantidades são **exatas** (contadas); parâmetros são
    **escolhas metodológicas** (com fonte/confiança).
13. **Apresentar só um número.** Sempre dar **cenários** (mín/referência/máx/recomendado) — um único
    número finge precisão que a estimativa não tem.

14. **Rodar o script SEM o config do projeto.** O script roda e devolve números — mas com
    `modulos`/`ref_paginas`/`duracoes` **vazios**: o módulo vira o **nome da pasta**, a seção de
    bibliografia sai **vazia** e os vídeos sem crédito ficam sem duração. O total **menor** parece “bom”.
    **Sempre use `--config`** e confira o cabeçalho da saída.
15. **Padrões de tipo de página de outro projeto (`padroes`).** Se os títulos das páginas não forem os do
    default, **tudo** cai como `conteudo` — **falha silenciosa**, sem erro no console. Confira a tabela
    “Distribuição das páginas por tipo” na saída (nasceu no episódio de 14/10/2026: 4 sínteses + 4
    aberturas sumiram até o padrão ser corrigido).
16. **Multiplicar por 60 o trecho do vídeo.** `MM:SS` **já é** minutos:segundos — `34:29 → 54:15` são
    **1186 s = 19min46s**, e o erro de multiplicar por 60 produziu “**19h46**” na primeira versão do
    script. Ver `duracoes-e-cruzamento.md` §3.
17. **Confiar no primeiro resultado do cruzamento bibliografia × curso.** Há **falso positivo por canal**
    (vários vídeos da mesma fundação casam por canal, com título diferente) e **por título genérico**
    (dois vídeos com “mediação de leitura”). Confirme **canal + título** antes de dar o item como
    “já contado”. Ver `duracoes-e-cruzamento.md` §4.
18. **Tratar `n/d` do H5P como zero.** Quando o `content.json` não é lido, a atividade entra com **0 item**
    e o tempo dela **desaparece** do relatório. É o caso de **mostrar `n/d` no relatório** e contar à mão
    pelo conteúdo publicado (ver `h5p-tipos.md`).
19. **Rodar o script de teste sem `--md`.** O `--md` **tem** default (o inventário oficial do projeto): rodar
    só com `--csv /tmp/...` **grava por cima** do `inventario-recursos.md` do projeto — aconteceu em
    **14/10/2026** durante a auditoria da skill. Ao testar, passe **sempre** `--csv` **e** `--md` para `/tmp`;
    se sobrescrever, **regenere com o script do projeto** e confirme com `git status`.

20. **Página que bloqueia o acesso direto ou não tem `<article>`.** Sites de fundação às vezes devolvem
    **“Access Denied”** (bloqueio) e portais de notícia montam a matéria em `<div>`s (a contagem crua pega
    **menu + rodapé + “Mais lidas”**). **Extraia por um leitor que devolve texto limpo** (ex.: `r.jina.ai`)
    e **delimite o corpo** do texto: exclua título, linha de apoio, data, “tempo de leitura”, categoria,
    compartilhamento, blocos de relacionados e legendas. *Contraprova útil:* a própria página pode declarar
    “tempo de leitura: N minutos” — se a estimativa cair na faixa, o corpo está bem delimitado.
21. **Medir PDF com `wc -w`.** Para anexos em PDF, use **`pdftotext` + a MESMA expressão de contagem do
    inventário** (`[A-Za-zÀ-ÿ0-9]+`) — não `wc -w` (tokeniza hífen/pontuação diferente e dá outro número:
    3.608 × 3.678 no projeto de origem). E meça **em tempo de execução** (não fixe o número à mão).
22. **Confiar em revalidar duração de vídeo por `curl` offline.** O `oEmbed` identifica o vídeo, mas o
    `lengthSeconds` vem do **HTML da página do YouTube**, que **não** responde neste ambiente. Resultado:
    as durações que não estão nos créditos ficam **fixadas no config/script, com comentário** declarando a
    origem — é a fonte **offline e reproduzível**.
23. **Dupla contagem cruzada.** Vigie **sempre** os dois pares: **(a)** vídeo **no corpo** × **na
    bibliografia** (contar uma vez) e **(b)** **página** da Sequência Didática × **PDF** da SD (página no A,
    PDF no B). São as duas duplas que mais inflam o total.
24. **Interpretar o parâmetro H5P sem declarar.** Há **duas leituras**: **1,5 min/questão** (múltipla/V-F) ×
    **3 min/atividade** (associação/arrastar/desafio) — a adotada — ou **3 min por item** nos tipos complexos.
    **Declare** a interpretação no relatório e registre a alternativa no código.
25. **As 3 travas da esteira de documento.** (i) **Quebra de página**: a classe na heading quebra **só no
    PDF**; o DOCX exigiria `{=openxml}` com `<w:br w:type="page"/>` (descartado em silêncio no HTML);
    (ii) **`reference-docx` sai em LETTER** (não A4) — o entregável de impressão é o **PDF A4**;
    (iii) **pandoc 2.9 emite `<w:tblGrid />` vazio** → colunas colapsam; rode o pós-processador de tabelas.
26. **Script da esteira que ESCREVE arquivo.** Generaliza a nº 19: todo script que grava (inventário,
    cálculo, DOCX, PDF, XLSX) tem **caminho padrão = arquivo oficial do projeto**. Em **teste**, redirecione
    **todas** as saídas para fora do repositório (`/tmp`) e confirme com `git status`. Sobrescrever o oficial
    por acidente só se desfaz **regerando** com o script do projeto e conferindo `diff`/`md5sum`.

## Checklist final antes de publicar

- [ ] Inventário rastreável (uma linha por página; totais conferidos).
- [ ] Cada parâmetro com **valor + faixa + nível de confiança + fonte**.
- [ ] **Buckets** A/B separados.
- [ ] **Cenários** + overhead (com justificativa e decisão registrada).
- [ ] Regras **anti-dupla-contagem** aplicadas.
- [ ] Declaração de **natureza** (estimativa), **limitações** e **pendências**.
- [ ] Fontes citadas no relatório.
- [ ] **Validação de paridade** feita (quando a skill foi exportada/atualizada): CSV do script × inventário
      oficial — idênticos, ou divergência investigada e explicada.
- [ ] **Estimativas por analogia** declaradas — e a **reexecução** prevista para substituí-las pela medição.
- [ ] **Resumo executivo** fechado em ≤ 2 páginas A4 (`pdfinfo`) e **DOCX** gerado pela esteira.
- [ ] **Nenhum arquivo de relatório aberto com `code`**; saídas de teste **fora** do projeto (`/tmp`).
