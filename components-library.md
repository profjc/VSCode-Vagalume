# 🧩 Biblioteca de Templates — Vaga Lume

> Componentes HTML reutilizáveis para páginas do curso Moodle 4.5 (tema Trema).
> **Reorganizada em 22/08/2026** conforme auditoria dos módulos Boas-vindas, M1 e M2 (`docs/relatorio-galeria-templates.md`).
> **Livro visual do autor:** `docs/templates-galeria/` (4 capítulos).
> **Sempre usar dentro de:** `<div class="container py-4 vagalume-pagina">...</div>`
>
> **Como o autor pede no DI:** escrever o **nome simples do template entre colchetes** (ex.: `[caixa de destaque]`) ou descrever o conteúdo — quando o template tem etiqueta "não precisa explicitar", o contexto basta.

---

# Capítulo 1 — Texto e Destaques

## 1. Caixa de Destaque
> **Status:** 🟢 Em uso (~60 páginas — o mais usado do curso)
> **Onde é usado:** praticamente todas as lições (sinopses, resumos, instruções, avisos)
> **Como pedir no DI:** `[caixa de destaque]` + texto — ou apenas descreva o conteúdo destacado

```html
<div class="vagalume-destaque-bloco mb-4">
  <p class="mb-0">Texto de destaque aqui.</p>
</div>
```

---

## 2. Citação com Autoria
> **Status:** 🟢 Em uso (4 páginas: M1P1L1p1, M1P2L1p1, M1P2L1p3, M1P4L1p1)
> **Onde é usado:** citações de autores/livros com crédito
> **Como pedir no DI:** `[citação com autoria]` + texto da citação + nome do autor

```html
<div class="vagalume-jumbotron">
  <p class="vagalume-citacao">"Texto da citação aqui."</p>
  <p class="vagalume-autora">— Autor(a)</p>
</div>
```

---

## 3. Aviso Importante
> **Status:** 🟢 Em uso (raro — variação da Caixa de Destaque)
> **Onde é usado:** alertas pontuais em lições
> **Como pedir no DI:** `[aviso importante]` + texto

```html
<div class="vagalume-sinopse">
  <p style="margin: 0;"><strong>💡 Importante:</strong> Texto do aviso ou nota aqui.</p>
</div>
```

---

## 4. Palavra em Destaque
> **Status:** 🟢 Em uso (~35 páginas — títulos e parágrafos)
> **Onde é usado:** destacar conceito-chave em título (`h*`) ou dentro de parágrafo. **ATENÇÃO (§6.2, 04/09/2026):** o `.vagalume-destaque` (verde) foi **DESCONTINUADO** como ênfase. O destaque agora é feito com **negrito puro `<strong>`** (herda a cor do contexto — `#261810` no branco, `#5B3925` em caixas creme). **Nunca** usar `<strong class="vagalume-destaque">`; **nunca** colar herança do verde.
> **Como pedir no DI:** negrito no termo — o DI aplica automaticamente

Título:
```html
<h1>Palavra <strong>Destacada</strong> no Título</h1>
```
Parágrafo:
```html
<p>Texto normal com uma <strong>palavra em destaque</strong>.</p>
```

---

## 5. Caixa de Destaque ao Lado de Imagem
> **Status:** 🟢 Em uso (~10 páginas com imagem flutuante)
> **Onde é usado:** bloco colorido no fluxo ao lado de imagem flutuante (impede quebra de layout)
> **Como pedir no DI:** `[caixa de destaque ao lado de imagem]` + texto

```html
<div class="card mb-4 border-0 bg-transparent">
  <div class="card-body vagalume-destaque-bloco mb-0">
    <p class="mb-0">Texto do bloco ao lado da imagem flutuante.</p>
  </div>
</div>
```
> O container pai da página deve ter `style="display: flow-root;"`.

---

## 6. Bloco de Orientação com Ícone
> **Status:** 🟢 Em uso (~20 páginas — dicas, orientações passo a passo)
> **Onde é usado:** Dicas Boas-vindas (8×), etapas do desenvolvimento M1P2 (6×), M1P4, M2P4L3p2, M2P5L1p3 etc.
> **Como pedir no DI:** `[bloco de orientação]` + ícone desejado (ou escolha automática) + título + texto

```html
<div class="vagalume-destaque-bloco mb-4">
  <div class="d-flex align-items-center mb-2">
    <i class="fa fa-lightbulb-o mr-3" aria-hidden="true" style="font-size: 2rem; color: #5b3925;">&nbsp;</i>
    <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">Título da orientação</p>
  </div>
  <p class="mb-0">Texto da orientação.</p>
</div>
```
> Variação para textos longos: ícone `fa-lg` + `padding-left: 36px` no texto (N3.2.10).

---

## 7. Caixa Para Refletir
> **Status:** 🟢 Em uso (3 páginas: M1P1F1, M1P4F1, M2P3L2p2)
> **Onde é usado:** chamadas finais de reflexão, fechamento de lição, sínteses reflexivas
> **Como pedir no DI:** `[para refletir]` + texto — visual distinto da instrução (card branco borda laranja)

```html
<div class="card vagalume-h5p-card">
  <div class="card-body">
    <div class="d-flex align-items-center mb-2">
      <i class="fa fa-lightbulb-o mr-3" aria-hidden="true" style="font-size: 1.5rem; color: #d96f1a;"></i>
      <p class="h6 font-weight-bold mb-0" style="color: #5b3925;">Para refletir</p>
    </div>
    <p class="mb-0">[TEXTO_DE_REFLEXÃO_DO_AUTOR]</p>
  </div>
</div>
```

---

## 8. Caixa de Convite
> **Status:** 🟢 Em uso (1 página: BV_Forum_Apresentacao)
> **Onde é usado:** convite final de fórum sem caráter reflexivo (ex.: "A apresentação é livre!")
> **Como pedir no DI:** `[caixa de convite]` + texto curto centralizado

```html
<div class="card vagalume-h5p-card">
  <div class="card-body text-center">
    <p class="h5 font-weight-bold mb-0" style="color: #5b3925;">[TEXTO_DE_CONVITE]</p>
  </div>
</div>
```

---

# Capítulo 2 — Imagens e Vídeos

## 9. Imagem ao Lado do Texto
> **Status:** 🟢 Em uso (8 páginas)
> **Onde é usado:** M1P3L2p1, M2P1L1p1, M2P1L1p2, M2P3L2p1, M2P4L3p1, M2P4L4p1, M2P4L4p2, M2P5L2p1
> **Como pedir no DI:** `[imagem ao lado do texto]` + lado (esquerda/direita) + legenda opcional

Flutuante à direita:
```html
<figure class="figure float-md-right ml-md-4 mb-3" style="max-width: 300px; border-radius: 8px; overflow: hidden;">
  <img src="" alt="" class="img-fluid" style="border-radius: 8px;" loading="lazy" width="300" height="200">
</figure>
```
Flutuante à esquerda:
```html
<figure class="figure float-md-left mr-md-4 mb-3" style="max-width: 300px; border-radius: 8px; overflow: hidden;">
  <img src="" alt="" class="img-fluid" style="border-radius: 8px;" loading="lazy" width="300" height="200">
</figure>
```
> O container pai da página deve ter `style="display: flow-root;"`.

---

## 10. Imagem Centralizada com Legenda
> **Status:** 🟢 Em uso (~8 páginas — padrão dominante do M2)
> **Onde é usado:** tirinhas e ilustrações centradas (Magali, Canuto, May, Kaio etc.)
> **Como pedir no DI:** `[imagem centralizada com legenda]` + imagem + legenda ("Fonte: ...")

```html
<figure class="figure text-center w-100 my-4">
  <img src="" alt="" class="img-fluid" style="border-radius: 8px;" loading="lazy" width="600" height="400">
  <figcaption class="figure-caption text-center mt-2">Fonte: origem da imagem.</figcaption>
</figure>
```

---

## 11. Imagem com Descrição Longa
> **Status:** 🟢 Em uso (7 páginas — acessibilidade N2.4.7)
> **Onde é usado:** imagens complexas que exigem descrição detalhada para leitores de tela
> **Como pedir no DI:** `[imagem com descrição longa]` + imagem + descrição detalhada

```html
<p class="sr-only" id="fig1-desc">Descrição detalhada da imagem para leitores de tela.</p>

<img src="" alt="" role="presentation" aria-labelledby="fig1-desc"
     class="img-fluid" style="border-radius: 8px;" loading="lazy" width="800" height="500">
```
> O `alt` fica vazio quando há `sr-only` (sem duplicidade). O ID deve ser único na página.

---

## 12. Faixa Fluida de Imagens
> **Status:** 🟢 Em uso (1 página: M1P1L1p5 — "Pensando juntos")
> **Onde é usado:** várias imagens lado a lado em faixa fluida (exceção N2.1.1.4: pode omitir dimensões)
> **Como pedir no DI:** `[faixa fluida de imagens]` + imagens

```html
<div class="row justify-content-center">
  <div class="col-4 col-sm px-0">
    <img src="" alt="" class="img-fluid w-100" loading="lazy">
  </div>
  <!-- repetir o bloco acima para cada imagem -->
</div>
```

---

## 13. Vídeo
> **Status:** 🟢 Em uso (5 páginas com vídeo — variante SEM sinopse)
> **Onde é usado:** vídeos do YouTube com créditos, sem caixa de sinopse (regra: nenhum vídeo terá sinopse obrigatória)
> **Como pedir no DI:** `[vídeo]` + URL embed + créditos
> **Legenda (04/09/2026):** formatar no padrão `Título (minutagem); canal: [nome do canal]` — sem "(YouTube)" e sem ":" após o título (regra 4.14).

```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div style="max-width: 560px; margin: 0 auto;">
      <div class="d-flex justify-content-center mb-2">
        <iframe class="vagalume-video" style="width: 100%; height: 315px; display: block;"
                title="Título do Vídeo" src="URL_EMBED"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen="allowfullscreen"></iframe>
      </div>
      <p class="small text-muted mb-0" style="font-size: 0.85rem; line-height: 1.4;">
        Título (minutagem); canal: nome do canal
      </p>
    </div>
  </div>
</div>
```

---

## 14. Vídeo com Sinopse
> **Status:** 🟢 Em uso (variação do Vídeo — quando o autor fornecer sinopse)
> **Onde é usado:** vídeo + créditos + bloco de sinopse com ícone `fa-file-text`
> **Como pedir no DI:** `[vídeo com sinopse]` + URL embed + créditos + texto da sinopse
> **Legenda (04/09/2026):** formatar no padrão `Título (minutagem); canal: [nome do canal]` — sem "(YouTube)" e sem ":" após o título (regra 4.14).

```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div style="max-width: 560px; margin: 0 auto;">
      <div class="d-flex justify-content-center mb-2">
        <iframe class="vagalume-video" style="width: 100%; height: 315px; display: block;"
                title="Título do Vídeo" src="URL_EMBED"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen="allowfullscreen"></iframe>
      </div>
      <p class="small text-muted mb-4" style="font-size: 0.85rem; line-height: 1.4;">
        Título (minutagem); canal: nome do canal
      </p>
      <div class="vagalume-sinopse">
        <div class="d-flex align-items-center mb-2">
          <i class="fa fa-file-text mr-3" aria-hidden="true" style="font-size: 1.5rem; color: #5b3925;"></i>
          <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">Sinopse</p>
        </div>
        <p class="mb-0">Texto descritivo do vídeo.</p>
      </div>
    </div>
  </div>
</div>
```

---

# Capítulo 3 — Atividades e Interação

## 15. Atividade H5P com Título
> **Status:** 🟢 Em uso (1 página: M1P3L2p4 — DragDrop)
> **Onde é usado:** atividade H5P intermediária com título no cabeçalho laranja do card
> **Como pedir no DI:** `[atividade h5p com título]` + título + placeholder do arquivo

```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-header">
        <i class="fa fa-puzzle-piece" aria-hidden="true"></i> Título da Atividade
      </div>
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[ARQUIVO_H5P: nome-do-arquivo.h5p]</div>
      </div>
    </div>
  </div>
</div>
```

---

## 16. Atividade H5P sem Título
> **Status:** 🟢 Em uso (11 páginas de atividade)
> **Onde é usado:** cards H5P sem cabeçalho (padrão predominante desde 08/08/2026)
> **Como pedir no DI:** `[atividade h5p]` + placeholder do arquivo

```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[ARQUIVO_H5P: nome-do-arquivo.h5p]</div>
      </div>
    </div>
  </div>
</div>
```

---

## 17. Atividade Final de Lição
> **Status:** 🟢 Em uso (12 páginas — última página de cada lição)
> **Onde é usado:** fechamento de lição: texto introdutório/celebração + instrução + H5P sem cabeçalho como último elemento
> **Como pedir no DI:** `[atividade final de lição]` + texto introdutório + instrução + arquivo H5P

```html
<div class="container py-4 vagalume-pagina">
  <!-- Texto introdutório (conteúdo do autor) -->
  <div class="mb-4">
    <p>Parágrafo 1 do texto introdutório.</p>
    <p class="mb-0">Último parágrafo — sem margem inferior.</p>
  </div>

  <!-- Instrução da atividade -->
  <div class="vagalume-destaque-bloco mb-4">
    <p class="mb-0"><strong>Instrução da Atividade:</strong> Texto com as instruções.</p>
  </div>

  <!-- Container H5P (sem cabeçalho) -->
  <div class="row justify-content-center">
    <div class="col-lg-8">
      <div class="vagalume-h5p-card">
        <div class="vagalume-h5p-body">
          <div class="h5p-placeholder" contenteditable="false">[ARQUIVO_H5P: nome-do-arquivo.h5p]</div>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 18. Galeria Interativa
> **Status:** 🟢 Em uso (1 página: M1P1L1p4 — 5 slides)
> **Onde é usado:** carrossel Bootstrap com imagens, botão "Clique para obter mais informações" (collapse) e navegação Anterior/Próximo
> **Como pedir no DI:** `[galeria interativa]` + imagens + análises por slide

```html
<div id="carouselExemplo" class="carousel slide mb-3" data-ride="carousel" data-interval="false">
  <ol class="carousel-indicators" style="bottom: -15px;">
    <li class="active" style="background-color: #5b3925; width: 8px; height: 8px; border-radius: 50%;" data-target="#carouselExemplo" data-slide-to="0" aria-label="Ir para o slide 1"></li>
  </ol>
  <div class="carousel-inner shadow-sm rounded border bg-white">
    <div class="carousel-item active p-3">
      <div class="card border-0 bg-white m-0 p-0">
        <figure class="figure d-block text-center w-100 mb-0">
          <img class="img-fluid rounded mx-auto d-block" style="max-height: 380px; object-fit: contain;"
               src="" alt="" width="800" height="450" loading="lazy">
          <figcaption class="figure-caption text-center mt-3 px-3">Legenda da imagem.</figcaption>
        </figure>
        <div class="card-body bg-light text-center px-4 rounded-bottom mt-3 pt-0">
          <div id="collapseEx1" class="collapse text-left mt-3 mb-3">
            <div class="vagalume-destaque-bloco p-3 m-0">
              <p class="mb-0">Análise detalhada da imagem.</p>
            </div>
          </div>
          <div class="d-flex flex-wrap justify-content-center align-items-center mb-2 mt-2" style="gap: 10px;">
            <button class="btn btn-secondary btn-sm" type="button" data-target="#carouselExemplo" data-slide="prev" aria-label="Exibir imagem anterior">
              <i class="fa fa-arrow-left mr-1" aria-hidden="true"></i> Anterior
            </button>
            <button class="btn btn-primary btn-sm px-4" type="button" data-toggle="collapse" data-target="#collapseEx1" aria-expanded="false" aria-controls="collapseEx1">
              Clique para obter mais informações
            </button>
            <button class="btn btn-secondary btn-sm" type="button" data-target="#carouselExemplo" data-slide="next" aria-label="Exibir próxima imagem">
              Próximo <i class="fa fa-arrow-right ml-1" aria-hidden="true"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
> IDs únicos por slide/collapse; container pai com `display: flow-root;`. Snippet completo multi-slide na versão anterior (`docs/backups/components-library-v2-antes-reorganizacao.md`, comp. 19).

---

## 19. Linha do Tempo Interativa
> **Status:** 🟢 Em uso (1 página: M1P3L2p3 — Políticas de Proteção)
> **Onde é usado:** sequência cronológica expansível (accordion vertical com eixo marrom, pontos e cards bege clicáveis)
> **Como pedir no DI:** `[linha do tempo interativa]` + itens (ano/data + título + texto + link opcional)

```html
<div id="timelineAccordion" class="accordion my-4">
  <div class="d-flex align-items-stretch">
    <div class="position-relative d-flex justify-content-center" style="width: 40px; flex-shrink: 0;" aria-hidden="true">
      <div style="position: absolute; top: 26px; bottom: 0; width: 3px; background-color: #5b3925;">&nbsp;</div>
      <div style="position: relative; width: 14px; height: 14px; background-color: #5b3925; border-radius: 50%; z-index: 2; margin-top: 22px;">&nbsp;</div>
    </div>
    <div class="flex-grow-1 pb-3">
      <div class="card mb-0" style="background-color: #faebdd; border-radius: 12px !important; border: 1.5px solid #5b3925 !important;">
        <div id="headingItem1" class="card-header p-0 border-0" style="background-color: transparent;">
          <button class="btn btn-block text-left p-3 font-weight-bold collapsed" style="color: #5b3925; background: none; border: none; box-shadow: none;" type="button" data-toggle="collapse" data-target="#collapseItem1" aria-expanded="false" aria-controls="collapseItem1">
            <strong>[ANO]</strong> &ndash; [Título do item]
          </button>
        </div>
        <div id="collapseItem1" class="collapse" aria-labelledby="headingItem1" data-parent="#timelineAccordion">
          <div class="card-body pt-3 px-3 pb-3" style="background-color: #ffffff; color: #261810; border-top: 1px solid rgba(217, 111, 26, 0.15); border-bottom-left-radius: 10px; border-bottom-right-radius: 10px;">
            <p class="mb-0">[Texto do item.]</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Repetir para cada item; no ÚLTIMO item: linha do eixo termina no ponto (top: 0; height: 28px) e remover pb-3 -->
</div>
```
> Snippet completo com primeiro/meio/último item na versão anterior (`docs/backups/components-library-v2-antes-reorganizacao.md`).

---

# Capítulo 4 — Estrutura de Página

## 20. Abertura de Módulo
> **Status:** 🟢 Em uso (2 páginas: M1-Apresentacao, M2-Apresentacao)
> **Onde é usado:** primeira página de cada módulo (apresentação geral + objetivo + expectativas)
> **Como pedir no DI:** `[abertura de módulo]` + textos de apresentação, objetivo e expectativas

```html
<div class="container py-4 vagalume-pagina">
  <!-- Apresentação geral -->
  <div class="vagalume-jumbotron">
    <h2 class="h5 font-weight-bold mb-3">Apresentação geral</h2>
    <p>Texto de apresentação do módulo — parágrafo 1.</p>
    <p class="mb-0">Texto de apresentação — parágrafo final.</p>
  </div>

  <!-- Grid Objetivo + Expectativas -->
  <div class="row">
    <div class="col-md-5 col-12 mb-4">
      <div class="vagalume-destaque-bloco h-100">
        <h3 class="h5 font-weight-bold mb-3"><i class="fa fa-bullseye mr-2" aria-hidden="true"></i>Objetivo</h3>
        <p class="mb-0">Texto do objetivo do módulo.</p>
      </div>
    </div>
    <div class="col-md-7 col-12 mb-4">
      <div class="vagalume-destaque-bloco h-100">
        <h3 class="h5 font-weight-bold mb-3"><i class="fa fa-graduation-cap mr-2" aria-hidden="true"></i>Expectativas de aprendizagem</h3>
        <ul class="pl-3 mb-0">
          <li class="mb-2">Primeira expectativa.</li>
          <li class="mb-0">Última expectativa.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

---

## 21. Cards de Síntese
> **Status:** 🟢 Em uso (2 páginas: M1P5P1, M2P6P1)
> **Onde é usado:** fechamento de módulo — grid de cards bege com ícone grande + título negrito + texto; encerra com celebração (troféu)
> **Como pedir no DI:** `[cards de síntese]` + lista de itens (título + texto + ícone opcional)

```html
<div class="row"><!-- Card N -->
  <div class="col-md-6 mb-4">
    <div class="vagalume-destaque-bloco h-100 mb-0">
      <div class="d-flex align-items-start"><i class="fa fa-star mr-3 mt-1" style="font-size: 1.8rem; color: #5b3925;" aria-hidden="true"></i>
        <div>
          <p class="mb-2" style="color: #5b3925;"><strong>Título do card</strong></p>
          <p class="mb-0" style="font-size: 0.95rem;">Texto do card.</p>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- Celebração de Fechamento (sub-bloco) -->
<div class="text-center mt-3 py-2">
  <p class="h5 mb-0" style="color: #5b3925; font-weight: bold;"><i class="fa fa-trophy mr-2" style="color: #d96f1a;" aria-hidden="true"></i>Parabéns, você acaba de finalizar o módulo!</p>
</div>
```

---

## 22. Referências Bibliográficas
> **Status:** 🟢 Em uso (2 páginas: M1P5P2, M2P6P2)
> **Onde é usado:** página final de cada módulo com as referências em ABNT
> **Como pedir no DI:** `[referências bibliográficas]` + lista de referências

```html
<div class="container py-4 vagalume-pagina" style="display: flow-root;">
  <h2 class="mb-4 pb-2 h4 font-weight-bold" style="color: #5b3925; border-bottom: 2px solid rgba(91, 57, 37, 0.15);">Referências Bibliográficas — Módulo N</h2>
  <div style="color: #261810; font-size: 0.95rem;">
    <p class="mb-3" style="padding-left: 20px; text-indent: -20px;">SOBRENOME, Nome. <strong>Título da obra</strong>. Cidade: Editora, ano.</p>
    <p class="mb-0" style="padding-left: 20px; text-indent: -20px;">Última referência (sem margem inferior).</p>
  </div>
</div>
```

---

## 23. Página de Fórum
> **Status:** 🟢 Em uso (8 fóruns)
> **Onde é usado:** todas as atividades de fórum ("Compartilhando Ideias" no Moodle). Template base: `templates/components/forum.html`
> **Como pedir no DI:** `[fórum]` + título completo + conteúdo livre + texto central da caixa "Para participar"

```html
<!-- Módulo X - Parte Y - Fórum Z - Fórum: [TÍTULO_COMPLETO] -->
<div class="container py-4 vagalume-pagina" style="display: flow-root;">
  <p class="h5 font-weight-bold mb-4"><span class="vagalume-destaque">Fórum: [TÍTULO_COMPLETO]</span></p>

  [CONTEÚDO_LIVRE_DO_AUTOR]

  <div class="card mb-4 border-0 bg-transparent">
    <div class="card-body vagalume-destaque-bloco mb-0">
      <div class="d-flex align-items-center mb-2"><i class="fa fa-comments mr-2" aria-hidden="true" style="font-size: 1.3rem; color: #5b3925;">&nbsp;</i> <span class="h5 font-weight-bold mb-0" style="color: #5b3925;">Para participar</span></div>
      [TEXTO_CENTRAL_VARIÁVEL]
      <hr style="border-top: 1px dashed rgba(91, 57, 37, 0.2);">
      <p class="mb-0 font-italic text-center" style="font-size: 0.95rem;"><i class="fa fa-users mr-1" aria-hidden="true" style="color: #2e7d32;">&nbsp;</i> Após <strong>sua postagem</strong>, comente em <strong>pelo menos duas participações</strong> de colegas para fortalecermos nossa própria rede de aprendizagem!</p>
    </div>
  </div>
</div>
<!-- FIM: Módulo X - Parte Y - Fórum Z - Fórum: [TÍTULO_COMPLETO] -->
```
> Exceções documentadas: fórum de apresentação das Boas-vindas usa nome próprio no Moodle e mensagem final adaptada.

---

## 24. Etiqueta de Parte (Label)
> **Status:** 🟢 Em uso (11 labels). Template base: `templates/pages/labels/ModuloN_Label_ParteN_titulo.html`
> **Onde é usado:** rótulos que demarcam o início de cada Parte na página principal do curso
> **Como pedir no DI:** `[etiqueta de parte]` + número da parte + título

Verde institucional (padrão):
```html
<!-- Módulo N - Label - Parte N - Título da Parte -->
<div style="border-left: 5px solid #587C41; padding: 10px 15px; margin: 30px 0 15px 0; background-color: #FAEBDD; border-radius: 0 8px 8px 0; font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;">
  <span style="display: block; font-size: 13px; text-transform: uppercase; color: #587C41; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px;">&nbsp;Parte N</span>
  <h2 style="margin: 0; padding: 0; font-size: 18px; color: #5B3925; font-weight: 700; border: none; line-height: 1.3;">Título da Parte</h2>
</div>
<!-- FIM: Módulo N - Label - Parte N - Título da Parte -->
```
> Variação laranja: substituir `#587C41` por `#D96F1A`.

---

## 25. Cards de Módulos
> **Status:** 🟢 Em uso (1 página: BV_Apresentacao)
> **Onde é usado:** lista dos módulos do curso em cards (`course-card`) com título negrito + descrição
> **Como pedir no DI:** `[cards de módulos]` + lista de módulos (título + descrição)

```html
<div class="card course-card mb-3">
  <div class="card-body"><strong>Módulo N -- Título do Módulo</strong> -- Descrição do módulo.</div>
</div>
```

---

# Reserva (templates disponíveis, sem uso até agora)

## R1. Botão Primário (CTA)
> **Status:** 🟡 Reserva — para links de download/materiais complementares em páginas futuras
> **Como pedir no DI:** `[botão]` + texto + URL

```html
<a href="#" target="_blank" rel="noopener noreferrer"
   class="btn btn-primary"
   style="background-color: #D96F1A; border-color: #D96F1A; color: #ffffff; border-radius: 8px; padding: 0.5rem 1.5rem; font-weight: 600;"
   aria-label="Descrição do link">
  Texto do Botão
</a>
```

---

## R2. Galeria de Imagens 2/3 Colunas
> **Status:** 🟡 Reserva — alternativa à Faixa Fluida quando as imagens precisarem de legendas individuais
> **Como pedir no DI:** `[galeria de imagens]` + imagens

```html
<div class="row">
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt="" class="img-fluid w-100" style="border-radius: 8px;" loading="lazy" width="600" height="400">
    </figure>
  </div>
  <!-- repetir por imagem; para 3 colunas usar col-md-4 -->
</div>
```

---

## R3. Grid de Texto 2 Colunas
> **Status:** 🟡 Reserva — opção para comparar conceitos lado a lado
> **Como pedir no DI:** `[grid de texto 2 colunas]` + textos

```html
<div class="row">
  <div class="col-12 col-md-6"><p>Texto da coluna esquerda...</p></div>
  <div class="col-12 col-md-6"><p>Texto da coluna direita...</p></div>
</div>
```

---

# Elementos de Sistema (regras transversais — não são templates visuais)

## S1. Encerramento de Página (economia de espaço)
Último elemento visível da página SEMPRE sem margem inferior (`mb-0`); bloco de destaque final usa `mb-4` no bloco e `mb-0` no parágrafo interno.

## S2. Links Externos (regra 6.1)
Todo link externo/e-mail: `target="_blank"` + `rel="noopener noreferrer"` + `class="nomediaplugin"` + estilização **negrito + sublinhado + colorido** na cor única **laranja-escuro `#944b11`** — válida sobre fundo branco e caixas creme. Links-botão (`.btn btn-primary`) seguem laranja `#D96F1A` com texto branco (não mudam).
```html
<a class="nomediaplugin font-weight-bold" style="color: #944b11; text-decoration: underline;" href="URL" target="_blank" rel="noopener noreferrer">Texto descritivo do link</a>
```

> **Atenção (04/09/2026):** a regra de **negrito** (S5) é distinta da de **links**. Negritos **nunca** usam a estilização colorida dos links — herdam a cor do contexto. Os snippets de link acima referem-se APENAS a `<a>` (links), jamais a `<strong>`.

## S3. Placeholder de Imagem (método padrão)
Imagem temporária com URL fixa do placeholder único + marcador textual "⚠️ APAGAR ESTE BLOCO" + imagem oficial com `src="[cole a imagem aqui]"`. Detalhes: `docs/regras-html-moodle.md` §1.1.3.

## S4. Placeholder H5P nominal
Sempre `[ARQUIVO_H5P: nome-do-arquivo.h5p]` — nunca URLs draft do Moodle.
## S5. Negritos (regra 6.2 — padronização de ênfase)
`<strong>` **nunca tem cor manual** — herda a cor do contexto: marrom escuro `#261810` sobre fundo branco/cards; marrom institucional `#5B3925` dentro de caixas creme. `.vagalume-destaque` (verde) está **descontinuado** como ênfase — migrar para `<strong>`. Página de referência: `Boas-vindas_Apresentacao.html`. Detalhes: `docs/regras-html-moodle.md` §6.2.
</content>
