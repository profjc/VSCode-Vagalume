# 🚀 Roteiro de Inicialização de Módulo — Vaga Lume

> **Para o Cline.** Documento operacional: roteiro validado para iniciar um módulo novo do curso Vaga Lume no Moodle 4.5 (tema Trema), do recebimento do material do autor até o estado pronto para gerar páginas.
>
> **Fontes de verdade:** `.clinerules` (regras N1–N3) · este roteiro (procedimento) · `Onde-paramos.md` (progresso).
>
> **Última aplicação real:** Módulo 3 — Bibliotecas Comunitárias (17/09/2026) — exemplo preenchido no fim do arquivo.

---

## Parte 1 — Recebimento e preparação do DI

### 1.1 Local e nomeação

- Pasta: `content/MN/` (N = número do módulo: M0=Boas-vindas, M1=Primeira Infância, M2=Leitura e Primeira Infância, M3=Bibliotecas Comunitárias, M4=Mão na massa, Encerramento=Certificação e Avaliação)
- Arquivos de DI: nome padronizado `DI-ModuloN.docx` + `DI-ModuloN.md`
- O mestre coloca o `.docx` original na pasta `temp/` — de lá o Cline move para `content/MN/`

### 1.2 Download (se o mestre fornecer link do Drive)

```bash
curl -sL "https://docs.google.com/document/d/{ID}/export?format=docx" \e
  -o "content/MN/DI-ModuloN.docx"
file "content/MN/DI-ModuloN.docx"   # Microsoft Word 2007+ / Zip archive
```

### 1.3 Conversão pandoc + extração de mídias

```bash
cd content/MN
pandoc "DI-ModuloN.docx" -t gfm --wrap=none --extract-media=. -o "DI-ModuloN.md"
file "DI-ModuloN.md"          # UTF-8
wc -l "DI-ModuloN.md"         # nº de linhas
ls media/ | wc -l             # nº de imagens extraídas (prévias — NÃO usar no Moodle)
```

- ⚠️ **Mídias em `media/` = referência interna APENAS** (comparação visual, verificar se batem com imagens oficiais). As imagens reais vêm dos links do SharePoint, baixadas pelo mestre e fornecidas em `temp/Imagens para Módulo N/` para processamento na **Parte 2**.
- ⚠️ **A conversão regrava o `.md` inteiro** — qualquer anotação ou correção anterior é PERDIDA. Ordem: converter primeiro, editar depois.
- ⚠️ **Caixas de texto do Word (`w:txbxContent`) são descartadas pelo pandoc.** Recuperação via script Python.

### 1.4 Verificação de integridade

- [ ] `.docx` + `.md` em `content/MN/` com nomes padronizados
- [ ] `file` OK; `.md` UTF-8; `media/` extraída
- [ ] `code -r` no `.md` para consulta do mestre
- [ ] Commit parcial (autorização do mestre)

---

## Parte 2 — Processamento das imagens do módulo

### 2.1 Recebimento

- O mestre coloca as imagens oficiais em `temp/Imagens para Módulo N/`
- As imagens da temp são a **fonte oficial** — as mídias em `content/MN/media/` (pandoc) servem **apenas para comparação visual** e **nunca** entram nos assets ou no Moodle
- Regra firmada: as mídias do pandoc são prévies de baixa qualidade (~350 px); usar sempre as que o mestre fornece

> **Nota importante sobre regra das imagens:** as imagens extraídas pelo pandoc em `content/MN/media/` servem **apenas como orientação visual** (comparar conteúdo, verificar o que a ilustração retrata). As imagens **reais** do módulo são as fornecidas pelo mestre em `temp/Imagens para Módulo N/` — são essas que **devem ser renomeadas, armazenadas nos assets e usadas no Moodle**. Nenhuma imagem do `media/` sobe para o Moodle.

### 2.2 Comparação visual

- Em **Plan mode**, ler as imagens da `temp/` e do `media/` via `read_files` (em Act mode a leitura de imagens é perdida — trocar para Plan, ler, depois voltar ao Act para editar)
- Verificar correspondência: a imagem temp bate com a prévia do pandoc (mesmo conteúdo visual)?
- Mapear cada imagem ao seu contexto no DI (qual lição/página/card ela pertence)
- Reportar discrepâncias ao mestre

### 2.3 Padronização de nomes

```
M{modulo}P{parte}L{licao}p{pagina}[-imgN]-{slug}.{ext}
```

Onde `{slug}` é uma descrição curta do conteúdo visual, em português, minúsculo, com underscores. Exemplo: `M3P2L7p1img1-canoa.png`.

### 2.4 Criação da galeria de descrições

- Arquivo: `assets/images/ilustracoes/MN/descricoes.md`
- Formato: tabela markdown (colunas: `# | Arquivo | Dimensões | Tamanho | Origem | Contexto no DI | Alt proposto | Status`)
- **Alt propostos:** redigidos pelo Cline com base na leitura visual (em Plan mode). Status inicial: `em rascunho`. Validar com o mestre.

### 2.5 Referência cruzada no DI

- Em cada ocorrência de link de imagem no `DI-ModuloN.md`, inserir comentário HTML com: caminho do arquivo final, dimensões e texto alternativo
- Exemplo: `<!-- --> ''assets/images/.../M3P1L1p1-tirinha-quino.png'' (404x306) . alt: "..." -->`

### 2.6 Limpeza

- Após processadas, a pasta `temp/Imagens para Módulo N/` é removida (imagens estão nos assets + backup no DI via links SharePoint)

### 2.7 Checklist de saída da Parte 2

- [ ] Todas as imagens em `assets/images/ilustracoes/MN/` com nomes padronizados
- [ ] Galeria `descricoes.md` criada com todas as entradas
- [ ] DI anotado com referências cruzadas (comentário HTML)
- [ ] `temp/` limpa
- [ ] `code -r` na galeria como última ação

---

## Parte 3 — Verificação de links e pendências do DI

### 3.1 Extrair todos os links do DI

```bash
grep -oE 'https?://[^ )>]+' content/MN/DI-ModuloN.md | sed 's/[.,;]$//' | sort -u
```

### 3.2 Testar links externos

- **YouTube:** via oEmbed API
  ```bash
  for id in ...; do
    resp=$(curl -s "https://www.youtube.com/oembed?url=https%3A//www.youtube.com/watch%3Fv%3D$id")
    echo "$id | $(python3 -c '...')"   # exibe título do vídeo
  done
  ```
- **SharePoint:** imagens já baixadas pelo mestre; testar apenas se o link é acessível (pode exigir autenticação — registrar como "protegido, não testável")
- **Outros domínios** (artigos, notícias, etc.): testar com `curl -sI`

### 3.3 Varrer pendências de arquivos sem entrega

Buscar no DI por marcadores de conteúdo pendente:

```bash
grep -n -i '\[inserir\|\[Inserir\|\[Embedar\|\[embedar\|\[LINK_DO_ARQUIVO\|sem link\|pendência\|créditos' content/MN/DI-ModuloN.md
```

Os marcadores comuns no Vaga Lume que indicam pendências do autor:
- `[Inserir foto do acervo Vaga Lume]` — imagem a ser enviada
- `[Embedar vídeo]` — vídeo embedado (se já tem link, OK; se só marcador, pendente)
- `[Inserir box com crédito]` — créditos a inserir
- `[inserir imagem da carteirinha]` — arquivo a disponibilizar

### 3.4 Relatório de saída

Gerar checklist com:
- [ ] Todos os links de YouTube testados e válidos (título obtido via oEmbed)
- [ ] Imagens/arquivos pendentes do autor listados (item por linha)
- [ ] Pendências registradas na galeria `descricoes.md` ou no início do `.md` de trabalho
- [ ] Reportado ao mestre antes de iniciar a geração de páginas

---

## Exemplo real de aplicação — Módulo 3 (17/09/2026)

- **DI:** `content/M3/DI-Modulo3.docx` (713 KB) + `DI-Modulo3.md` (1.271 linhas, 5 mídias `media/`)
- **Imagens:** 6 arquivos em `temp/Imagens para Módulo III/` (nomes com mojibake — corrigidos)
- **Assets:** 6 imagens em `assets/images/ilustracoes/M3/` (556 KB total)
  - `M3P1L1p1-tirinha-quino.png` (404x306)
  - `M3P2L7p1img1-canoa.png` (1920x1080)
  - `M3P2L7p1img2-livros_sobre_mesa.png` (1920x1080)
  - `M3P2L7p1img3-criancas_bananeira.png` (1920x1080)
  - `M3P2L7p1img4-livro_sobre_cabeca.png` (1920x1080)
  - `M3P3L10p1-tirinha-stahler.png` (404x306)
- **Galeria:** `assets/images/ilustracoes/M3/descricoes.md` (6 entradas)
- **DI anotado:** 6 referências cruzadas inseridas como comentários HTML
- **Links testados:** 10 YouTube válidos (títulos verificados) + 6 SharePoint (protegidos, imagens já processadas)
- **Pendências do autor reportadas (11 itens):**
  - 7× `[Inserir foto do acervo Vaga Lume]` (linhas 148, 258, 268, 278, 288, 298, 1171)
  - 1× Carteirinha de leitora (linha 967)
  - 1× Caderno de Memórias (linha 1013)
  - 1× Modelo de Regimento (linha 1029)
  - 1× Modelo de Plano de Ação (linha 1063)
- **Lições aprendidas:** (a) leitura de imagens só em Plan mode; (b) mojibake requer Python em lote; (c) imagens `media/` do pandoc são prévies baixa resolução, usar sempre as fornecidas pelo mestre
