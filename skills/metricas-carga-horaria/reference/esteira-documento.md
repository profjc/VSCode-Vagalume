# Esteira de documento imprimível (.md → PDF A4 + DOCX + XLSX)

> A esteira **comprovada** para gerar os entregáveis do Passo 5 sem montar nada à mão.
> **Versão 1.2 (15/10/2026)** — projeto de origem: Vaga Lume. Lições do Ciclo 5 (relatório) e do Ciclo 6
> (resumo executivo). O **entregável de impressão é o PDF A4**; o DOCX é o **editável** em fluxo natural.

## 1 — Fluxo geral

```
fonte .md  ──pandoc -t html5──►  fragmento HTML
                                     │  (injeta no marcador <!-- CONTEUDO --> do espelho A4)
                                     ▼
                            espelho-HTML-A4  ──Chrome headless --print-to-pdf──►  PDF A4
fonte .md  ──pandoc --reference-doc──►  DOCX  ──pós-processadores──►  DOCX final
planilha .csv  ──soffice --convert-to xlsx──►  XLSX
```

**Princípio:** a **fonte é o `.md`** (front-matter com `title`/`subtitle`/`author`/`date`/`lang`); o
**visual é o espelho** (`templates/documentos/espelho-*.html`, que **não** vai ao Moodle — é a versão
imprimível). O script injeta o corpo no espelho com `awk` no marcador `<!-- CONTEUDO -->`.

## 2 — PDF por Chrome headless (o entregável de impressão)

```bash
pandoc <fonte>.md -t html5 -o /tmp/corpo.html
sed -i 's|src="assets/|src="../../assets/|g' /tmp/corpo.html     # ajusta os caminhos à profundidade do espelho
awk -v corpo=/tmp/corpo.html '/<!-- CONTEUDO -->/{while((getline l<corpo)>0)print l;close(corpo);next}{print}' \
    templates/documentos/<espelho>.html > /tmp/doc.html
perfil="$(mktemp -d)"
google-chrome --headless=new --disable-gpu --no-sandbox --user-data-dir="$perfil" \
  --no-pdf-header-footer --run-all-compositor-stages-before-draw --virtual-time-budget=15000 \
  --print-to-pdf="<saida>.pdf" "file:///tmp/doc.html"
```

- O espelho define `@page { size:A4; margin:20mm 16mm 18mm; }` e
  `* { -webkit-print-color-adjust:exact !important; }` (sem isso o Chrome **descarta as cores** de fundo).
- **Cabeçalho/rodapé do Chrome: desligados** (`--no-pdf-header-footer`) — o cabeçalho e os logos são do espelho.

## 3 — DOCX editável (pandoc + 3 pós-processadores)

```bash
python3 <...>/gerar-reference-docx.py                 # 1) reference-docx com a marca (fonte + cores dos títulos)
pandoc <fonte>.md --reference-doc=referencia.docx -o <saida>.docx
python3 <...>/ajustar-tabelas-docx.py <saida>.docx    # 2) conserta o <w:tblGrid /> vazio (ver §4)
python3 <...>/adicionar-logos-docx.py <saida>.docx    # 3) insere os logos no topo
```

- Os **pós-processadores** reescrevem o `.docx` (ZIP): `ajustar-tabelas-docx.py` preenche o grid das
  tabelas com larguras iguais; `adicionar-logos-docx.py` insere uma linha com os logos via `word/_rels`.
- **Escopo A:** os scripts são **instâncias** (produto, cores, logos) — revise-os ao exportar.

## 4 — As 3 travas (todas testadas no Ciclo 6)

1. **Quebra de página.** `break-before: page` numa heading (atributo `{ .quebra-pagina }` do pandoc) quebra
   **só no PDF/HTML**. No **DOCX** a classe é **inofensiva e não quebra** — para quebrar ali é preciso um bloco
   raw ```` ```{=openxml} ```` com `<w:p><w:r><w:br w:type="page"/></w:r></w:p>`, que é **descartado em
   silêncio** na saída HTML (logo, pode conviver no mesmo `.md` **sem afetar o PDF**).
2. **Papel.** O `reference-docx` padrão do pandoc sai em **`Letter` (612×792)**, **não A4**. O **entregável de
   impressão é o PDF A4**; o DOCX é **fluxo natural** (decisão do mestre, 15/10/2026). Fixar A4 no
   `gerar-reference-docx.py` obrigaria a **regerar todos os DOCX** da esteira — só com decisão explícita.
3. **`<w:tblGrid />` vazio (pandoc 2.9).** Sem larguras, o LibreOffice **colapsa as colunas** numa só. Por isso
   o `ajustar-tabelas-docx.py` roda **sempre** depois do pandoc.

## 5 — Níveis de confiança no imprimível (badges, não emojis)

Os emojis 🟢🟡🔴 **saem pretos** no PDF e no DOCX. No entregável use **badges coloridos + rótulo textual**:

```markdown
[Científico]{.cg}   [Benchmark]{.cb}   [Heurística]{.ch}
```

O espelho define as classes com um **ponto colorido** via `::before` e cor por classe (ex.: `.cg` verde,
`.cb` dourado, `.ch` vermelho). No **DOCX**, o pandoc **preserva o texto** do span (a cor se perde, o rótulo
fica) — é a única forma de funcionar nos **dois** entregáveis.

## 6 — Gráficos e planilha

- **Gráficos** (`.png`) por `matplotlib` (cores da marca), lidos do `.csv` de cálculo; salvos em
  `assets/images/relatorios/`. Nome referenciado no `.md` com caminho relativo.
- **XLSX**: `soffice --headless "-env:UserInstallation=file://$perfil" --convert-to xlsx --outdir <pasta> <csv>`.

## 7 — Checklist da esteira

- [ ] Fonte `.md` com **front-matter** completo; corpo injetado no espelho (`<!-- CONTEUDO -->`).
- [ ] **PDF A4** gerado por Chrome headless; **contagem de páginas** conferida (`pdfinfo`).
- [ ] **DOCX** gerado com `reference-docx` **+ os 3 pós-processadores** (tabelas e logos).
- [ ] **XLSX** a partir do `.csv` de cálculo (quando houver planilha).
- [ ] **Nomes de arquivo** padronizados (`Relatorio-<tema>-<curso>.{pdf,docx}` · `Resumo-executivo-<tema>-<curso>.{pdf,docx}`).
- [ ] **Nenhum arquivo de relatório aberto com `code`** — a entrega na janela ativa fica restrita às páginas HTML do curso.
