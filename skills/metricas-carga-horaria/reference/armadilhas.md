# Armadilhas e lições aprendidas

> O que costuma dar errado nestas métricas — e como evitar. **Versão 1.1.1 (14/10/2026)** —
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
