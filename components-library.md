# 🧩 Biblioteca de Componentes - Vaga Lume

> Componentes HTML reutilizáveis para páginas do curso Moodle 4.5
> **Sempre usar dentro de:** `<div class="container py-4 vagalume-pagina">...</div>`

---

## 1. Botão Primário (CTA)

### Simples
```html
<a href="#" target="_blank" rel="noopener noreferrer"
   class="btn btn-primary"
   style="background-color: #D96F1A; border-color: #D96F1A; color: #ffffff; border-radius: 8px; padding: 0.5rem 1.5rem; font-weight: 600;"
   aria-label="Descrição do link">
  Texto do Botão
</a>
```

### Centralizado
```html
<div class="text-center">
  <a href="#" target="_blank" rel="noopener noreferrer"
     class="btn btn-primary"
     style="background-color: #D96F1A; border-color: #D96F1A; color: #ffffff; border-radius: 8px; padding: 0.5rem 1.5rem; font-weight: 600;"
     aria-label="Descrição do link">
    Texto do Botão
  </a>
</div>
```

---

## 2. Card de Destaque (Jumbotron)

```html
<div class="vagalume-jumbotron">
  <p class="vagalume-citacao">"Texto da citação aqui."</p>
  <p class="vagalume-autora">— Autor(a)</p>
</div>
```

---

## 3. Bloco de Destaque (Sinopse)

```html
<div class="vagalume-sinopse">
  <p style="margin: 0;">Texto de destaque ou sinopse aqui.</p>
</div>
```

---

## 4. Player H5P (Placeholder Nativo)

> **Importante:** Não utilize iframes manuais ou classes de proporção (embed-responsive) para H5P. Utilize exclusivamente a tag de placeholder nativa `.h5p-placeholder` para que o Moodle aplique o redimensionamento dinâmico.

### Áudio/Podcast
```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-header">
        <i class="fa fa-headphones" aria-hidden="true"></i> Título do Áudio
      </div>
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[LINK_DO_ARQUIVO_.H5P]</div>
      </div>
    </div>
  </div>
</div>
```

### Vídeo
```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-header">
        <i class="fa fa-video-camera" aria-hidden="true"></i> Título do Vídeo
      </div>
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[LINK_DO_ARQUIVO_.H5P]</div>
      </div>
    </div>
  </div>
</div>
```

### Quiz/Atividade
```html
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="vagalume-h5p-card">
      <div class="vagalume-h5p-header">
        <i class="fa fa-puzzle-piece" aria-hidden="true"></i> Título da Atividade
      </div>
      <div class="vagalume-h5p-body">
        <div class="h5p-placeholder" contenteditable="false">[LINK_DO_ARQUIVO_.H5P]</div>
      </div>
    </div>
  </div>
</div>
```

---

## 5. Galeria de Imagens

### 2 colunas (desktop) / 1 coluna (mobile)
```html
<div class="row">
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 8px;"
           loading="lazy"
           width="600" height="400">
    </figure>
  </div>
  <div class="col-12 col-md-6 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 8px;"
           loading="lazy"
           width="600" height="400">
    </figure>
  </div>
</div>
```

### 3 colunas (desktop)
```html
<div class="row">
  <div class="col-12 col-md-4 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 8px;"
           loading="lazy"
           width="400" height="300">
    </figure>
  </div>
  <div class="col-12 col-md-4 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 8px;"
           loading="lazy"
           width="400" height="300">
    </figure>
  </div>
  <div class="col-12 col-md-4 mb-3">
    <figure class="figure w-100" style="border-radius: 8px; overflow: hidden;">
      <img src="" alt=""
           class="img-fluid w-100"
           style="border-radius: 8px;"
           loading="lazy"
           width="400" height="300">
    </figure>
  </div>
</div>
```

---

## 6. Imagem Flutuante com Figure (Padrão Estrito)

> Regras: Toda imagem flutuante deve usar `<figure>` com `border-radius: 8px; overflow: hidden;` tanto na `<figure>` quanto na `<img>`.

### Flutuante à Direita
```html
<figure class="figure float-md-right ml-md-4 mb-3" style="max-width: 300px; border-radius: 8px; overflow: hidden;">
  <img src="" alt=""
       class="img-fluid"
       style="border-radius: 8px;"
       loading="lazy"
       width="300" height="200">
</figure>
```

### Flutuante à Esquerda
```html
<figure class="figure float-md-left mr-md-4 mb-3" style="max-width: 300px; border-radius: 8px; overflow: hidden;">
  <img src="" alt=""
       class="img-fluid"
       style="border-radius: 8px;"
       loading="lazy"
       width="300" height="200">
</figure>
```

---

## 7. Bloco de Destaque Isolado (para uso junto com float)

> Quando um bloco colorido (sinopse, jumbotron) estiver no fluxo ao lado de uma imagem flutuante, encapsular em card do Bootstrap:

```html
<div class="card mb-4 border-0 bg-transparent">
  <div class="card-body vagalume-destaque-bloco mb-0">
    <!-- Conteúdo aqui -->
    <p class="mb-0">Texto do bloco de destaque ao lado de uma imagem flutuante.</p>
  </div>
</div>
```

---

## 8. Imagem Clicável (Modal Pop-up)

```html
<!-- Miniatura clicável -->
<img src="" alt=""
     style="cursor: zoom-in;"
     role="link" tabindex="0"
     data-toggle="modal" data-target="#modalFig1"
     loading="lazy"
     width="600" height="400">

<!-- Modal -->
<div class="modal fade" id="modalFig1" tabindex="-1" role="dialog" aria-labelledby="modalFig1Label" aria-hidden="true">
  <div class="modal-dialog modal-lg modal-dialog-centered" role="document">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="modalFig1Label">Título da Imagem</h5>
        <button type="button" class="close" data-dismiss="modal" aria-label="Fechar">
          <span aria-hidden="true">&times;</span>
        </button>
      </div>
      <div class="modal-body text-center">
        <img src="" alt=""
             class="img-fluid"
             style="border-radius: 8px;"
             loading="lazy">
      </div>
    </div>
  </div>
</div>
```

---

## 9. Imagem com Descrição Longa (Acessibilidade)

```html
<p class="sr-only" id="fig1-desc">Descrição detalhada da imagem para leitores de tela.</p>

<img src="" alt=""
     role="presentation"
     aria-labelledby="fig1-desc"
     class="img-fluid w-100"
     style="border-radius: 8px;"
     loading="lazy"
     width="800" height="500">
```

---

## 10. Vídeo Centralizado no Corpo do Texto

```html
<div class="row justify-content-center">
  <div class="col-lg-8">

    <div class="d-flex justify-content-center mb-2">
      <iframe class="vagalume-video" title="Título do Vídeo" src="URL_EMBED"
              frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
              allowfullscreen="allowfullscreen"></iframe>
    </div>

    <p class="small text-muted mb-4" style="font-size: 0.85rem; line-height: 1.4;">
      <strong>Créditos:</strong> Texto de créditos
    </p>

    <div class="vagalume-sinopse">
      <div class="d-flex align-items-center mb-2">
        <i class="fa fa-file-text mr-3" aria-hidden="true" style="font-size: 1.5rem; color: #5b3925;"></i>
        <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">Sinopse</p>
      </div>
      <p class="mb-0">Texto descritivo do vídeo</p>
    </div>

  </div>
</div>
```

---

## 11. Título com Destaque

```html
<h1>Palavra <span class="vagalume-destaque">Destacada</span> no Texto</h1>
```

---

## 12. Texto com Destaque no Parágrafo

```html
<p>Este é um texto normal com uma <span class="vagalume-destaque">palavra em destaque</span> no meio do parágrafo.</p>
```

---

## 13. Aviso/Nota (utilizando sinopse)

```html
<div class="vagalume-sinopse">
  <p style="margin: 0;"><strong>💡 Importante:</strong> Texto do aviso ou nota aqui.</p>
</div>
```

---

## 14. Grid de Texto 2 Colunas

```html
<div class="row">
  <div class="col-12 col-md-6">
    <p>Texto da coluna esquerda...</p>
  </div>
  <div class="col-12 col-md-6">
    <p>Texto da coluna direita...</p>
  </div>
</div>
```

---

## 15. Imagem Flutuante com Legenda e Descrição Longa (Acessibilidade)

> Figura flutuante à direita com `<figcaption>` visível + `<p class="sr-only">` para descrição longa. A imagem tem `alt=""` e `role="presentation"` para evitar duplicidade com o `sr-only`. Usa `float-md-right` para responsividade e `display: flow-root;` no container pai.

```html
<figure class="figure float-md-right ml-md-4 mb-3" style="max-width: 375px; border-radius: 8px; overflow: hidden;">
  <img src="" alt=""
       role="presentation"
       aria-labelledby="figID-desc"
       class="img-fluid"
       style="border-radius: 8px;"
       loading="lazy"
       width="375" height="500">
  <figcaption class="figure-caption text-center mt-2">Legenda visível da imagem.</figcaption>
</figure>

<p class="sr-only" id="figID-desc">Descrição detalhada da imagem para leitores de tela.</p>
```
> **Regras de uso:** O `alt` deve ficar vazio quando `sr-only` estiver presente. O ID do `sr-only` (ex: `figAries-desc`) deve ser único na página e referenciado em `aria-labelledby`. O container pai deve ter `style="display: flow-root;"`.

---

## 16. Cabeçalho de Módulo (Título H1)

> Padrão para o título principal de qualquer página de módulo. Usa `h1` estilizado como `h3` para escala visual adequada.

```html
<div class="row mb-4">
  <div class="col-12">
    <h1 class="h3 font-weight-bold mb-0">Módulo X - Nome do Módulo</h1>
  </div>
</div>
```

---

## 17. Grid Objetivo + Expectativas de Aprendizagem

> Layout de duas colunas (5/7 no desktop, empilhadas no mobile) usado na página de abertura de cada módulo. Coluna esquerda: objetivo com ícone `fa-bullseye`. Coluna direita: lista de expectativas com ícone `fa-graduation-cap`. Ambas as colunas usam `.vagalume-destaque-bloco` com `h-100` para alturas iguais.

```html
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
        <li class="mb-2">Primeira expectativa de aprendizagem.</li>
        <li class="mb-2">Segunda expectativa de aprendizagem.</li>
        <li class="mb-0">Última expectativa (sem margem inferior).</li>
      </ul>
    </div>
  </div>
</div>
```

---

## 18. Apresentação de Módulo (Template Completo de Abertura)

> Template completo que combina Cabeçalho de Módulo + Jumbotron de Apresentação + Grid Objetivo/Expectativas. Usado na primeira página de cada módulo (M1/Apresentacao, M2/Apresentacao etc.).

```html
<div class="container py-4 vagalume-pagina">
  <!-- Cabeçalho do módulo -->
  <div class="row mb-4">
    <div class="col-12">
      <h1 class="h3 font-weight-bold mb-0">Módulo X - Nome do Módulo</h1>
    </div>
  </div>

  <!-- Apresentação geral -->
  <div class="vagalume-jumbotron">
    <h2 class="h5 font-weight-bold mb-3">Apresentação geral</h2>
    <p>Texto de apresentação do módulo — parágrafo 1.</p>
    <p class="mb-0">Texto de apresentação do módulo — parágrafo 2 (último, sem margem inferior).</p>
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
          <li class="mb-2">Segunda expectativa.</li>
          <li class="mb-0">Última expectativa.</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

---

## 19. Carrossel com Imagens + Collapse (Galeria Interativa)

> Carrossel Bootstrap com cards, imagens centralizadas e botão "Clique para obter mais informações" que expande um collapse com análise detalhada. Cada slide contém: imagem com `max-height: 380px; object-fit: contain;`, legenda via `<figcaption>`, e botões Anterior/Próximo + Collapse. Os indicadores são bolinhas marrons customizadas.

```html
<div id="carouselExemplo" class="carousel slide mb-3" data-ride="carousel" data-interval="false">
  <!-- Indicadores -->
  <ol class="carousel-indicators" style="bottom: -15px;">
    <li class="active" style="background-color: #5b3925; width: 8px; height: 8px; border-radius: 50%;" data-target="#carouselExemplo" data-slide-to="0" aria-label="Ir para o slide 1"></li>
    <li style="background-color: #5b3925; width: 8px; height: 8px; border-radius: 50%;" data-target="#carouselExemplo" data-slide-to="1" aria-label="Ir para o slide 2"></li>
  </ol>

  <div class="carousel-inner shadow-sm rounded border bg-white">
    <!-- Slide 1 -->
    <div class="carousel-item active p-3">
      <div class="card border-0 bg-white m-0 p-0">
        <figure class="figure d-block text-center w-100 mb-0">
          <img class="img-fluid rounded mx-auto d-block" style="max-height: 380px; object-fit: contain;"
               src="" alt="Descrição da imagem 1"
               width="800" height="450" loading="lazy">
          <figcaption class="figure-caption text-center mt-3 px-3">Legenda da imagem 1.</figcaption>
        </figure>

        <div class="card-body bg-light text-center px-4 rounded-bottom mt-3 pt-0">
          <div id="collapseEx1" class="collapse text-left mt-3 mb-3">
            <div class="vagalume-destaque-bloco p-3 m-0">
              <p class="mb-0">Análise detalhada da imagem 1.</p>
            </div>
          </div>

          <div class="d-flex flex-wrap justify-content-center align-items-center mb-2 mt-2" style="gap: 10px;">
            <button class="btn btn-secondary btn-sm" type="button" data-target="#carouselExemplo" data-slide="prev" aria-label="Exibir imagem anterior do carrossel">
              <i class="fa fa-arrow-left mr-1" aria-hidden="true"></i> Anterior
            </button>
            <button class="btn btn-primary btn-sm px-4" type="button" data-toggle="collapse" data-target="#collapseEx1" aria-expanded="false" aria-controls="collapseEx1">
              Clique para obter mais informações
            </button>
            <button class="btn btn-secondary btn-sm" type="button" data-target="#carouselExemplo" data-slide="next" aria-label="Exibir próxima imagem do carrossel">
              Próximo <i class="fa fa-arrow-right ml-1" aria-hidden="true"></i>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Slide 2 (cópia do slide 1 com IDs e conteúdos alterados) -->
    <div class="carousel-item p-3">
      <div class="card border-0 bg-white m-0 p-0">
        <figure class="figure d-block text-center w-100 mb-0">
          <img class="img-fluid rounded mx-auto d-block" style="max-height: 380px; object-fit: contain;"
               src="" alt="Descrição da imagem 2"
               width="800" height="450" loading="lazy">
          <figcaption class="figure-caption text-center mt-3 px-3">Legenda da imagem 2.</figcaption>
        </figure>

        <div class="card-body bg-light text-center px-4 rounded-bottom mt-3 pt-0">
          <div id="collapseEx2" class="collapse text-left mt-3 mb-3">
            <div class="vagalume-destaque-bloco p-3 m-0">
              <p class="mb-0">Análise detalhada da imagem 2.</p>
            </div>
          </div>

          <div class="d-flex flex-wrap justify-content-center align-items-center mb-2 mt-2" style="gap: 10px;">
            <button class="btn btn-secondary btn-sm" type="button" data-target="#carouselExemplo" data-slide="prev" aria-label="Exibir imagem anterior do carrossel">
              <i class="fa fa-arrow-left mr-1" aria-hidden="true"></i> Anterior
            </button>
            <button class="btn btn-primary btn-sm px-4" type="button" data-toggle="collapse" data-target="#collapseEx2" aria-expanded="false" aria-controls="collapseEx2">
              Clique para obter mais informações
            </button>
            <button class="btn btn-secondary btn-sm" type="button" data-target="#carouselExemplo" data-slide="next" aria-label="Exibir próxima imagem do carrossel">
              Próximo <i class="fa fa-arrow-right ml-1" aria-hidden="true"></i>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
> **Regras de uso:** O `id` do carrossel e de cada collapse devem ser únicos na página. Os indicadores têm `bottom: -15px` para compensar o padding. As imagens usam `max-height: 380px; object-fit: contain;` para proporção consistente. Use `data-interval="false"` para evitar rotação automática. O container pai deve usar `style="display: flow-root;"`.

---

## Templates de Página

### Página de Conteúdo Padrão (sem floats)
```html
<div class="container py-4 vagalume-pagina">
  <h1>Título do Módulo</h1>

  <div class="vagalume-sinopse">
    <p style="margin: 0;">Descrição geral do conteúdo desta página.</p>
  </div>

  <!-- Conteúdo principal aqui -->

  <div class="vagalume-jumbotron">
    <p class="vagalume-citacao">"Citação de destaque."</p>
    <p class="vagalume-autora">— Autor(a)</p>
  </div>
</div>
```

### Página com Imagem Flutuante (com `flow-root`)
```html
<div class="container py-4 vagalume-pagina" style="display: flow-root;">
  <h1>Título do Módulo</h1>

  <figure class="figure float-md-right ml-md-4 mb-3" style="max-width: 300px; border-radius: 8px; overflow: hidden;">
    <img src="" alt="" class="img-fluid" style="border-radius: 8px;" loading="lazy" width="300" height="200">
  </figure>

  <p>Texto que flui ao redor da imagem...</p>

  <div class="card mb-4 border-0 bg-transparent">
    <div class="card-body vagalume-destaque-bloco mb-0">
      <p class="mb-0">Bloco de destaque isolado ao lado da imagem flutuante.</p>
    </div>
  </div>
</div>
```

---

---

## 20. Padrão de Encerramento de Lição (Economia de Espaço no Moodle)

> **Contexto:** O Moodle já aplica enquadramento de página automaticamente, então o último elemento de uma página de lição deve usar `mb-0` para evitar espaçamento extra desnecessário.
>
> **Regras:**
> 1. **Bloco de destaque final:** usar `class="vagalume-destaque-bloco mb-4"` (com `mb-4` no bloco e `mb-0` no parágrafo interno)
> 2. **Parágrafo de fechamento (último da lição):** usar `<p class="mb-0">` — sem margem inferior
> 3. **Nunca** usar `mb-4` ou margem inferior no último elemento visível da página

### Exemplo: Página com bloco de destaque como último elemento
```html
<div class="vagalume-destaque-bloco mb-4">
  <div class="d-flex align-items-center mb-2">
    <i class="fa fa-exclamation-triangle mr-3" aria-hidden="true" style="font-size: 2rem; color: #5b3925;"></i>
    <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">É importante nesta fase</p>
  </div>
  <p class="mb-0">Texto do bloco de destaque final.</p>
</div>
```

### Exemplo: Página com parágrafo de fechamento (última da lição)
```html
<div class="vagalume-destaque-bloco mb-4">
  <div class="d-flex align-items-center mb-2">
    <i class="fa fa-exclamation-triangle mr-3" aria-hidden="true" style="font-size: 2rem; color: #5b3925;"></i>
    <p class="font-weight-bold mb-0" style="color: #5b3925; line-height: 1.2;">É importante nesta fase</p>
  </div>
  <p class="mb-0">Texto do bloco de destaque.</p>
</div>

<p class="mb-0">Parágrafo de encerramento da lição — sem margem inferior para economizar espaço no Moodle.</p>
```


---

## 21. Página Final de Lição com Atividade H5P

> **Contexto:** A última página de cada lição geralmente traz uma atividade H5P de quiz/resumo. A estrutura combina: (1) texto introdutório de celebração com `.vagalume-destaque`, (2) contexto/convite para a atividade, (3) bloco de instrução, (4) o player H5P sem cabeçalho (apenas `vagalume-h5p-body` direto no card).

### Características do Padrão:
1. **Texto introdutório:** conteúdo original do autor (pode incluir celebração, contexto, convite para a atividade) — **não é template fixo**
2. **Bloco de instrução:** `.vagalume-destaque-bloco mb-4` com `<strong>Instrução da Atividade:</strong>`
3. **Container H5P:** `.row.justify-content-center > .col-lg-8` com `vagalume-h5p-card` → **sem `vagalume-h5p-header`** (apenas `vagalume-h5p-body` direto)
4. **Placeholder:** `[LINK_DO_ARQUIVO_.H5P]`
5. **Último elemento:** o H5P (container sem margem inferior extra)

```html
<div class="container py-4 vagalume-pagina">
  <!-- Texto introdutório (conteúdo original do autor) -->
  <div class="mb-4">
    <p>Parágrafo 1 do texto introdutório.</p>
    <p>Parágrafo 2 do texto introdutório.</p>
    <p class="mb-0">Último parágrafo — sem margem inferior.</p>
  </div>

  <!-- Instrução da atividade -->
  <div class="vagalume-destaque-bloco mb-4">
    <p class="mb-0"><strong>Instrução da Atividade:</strong> Texto com as instruções para o cursista realizar a atividade.</p>
  </div>

  <!-- Container H5P (sem cabeçalho) -->
  <div class="row justify-content-center">
    <div class="col-lg-8">
      <div class="vagalume-h5p-card">
        <div class="vagalume-h5p-body">
          <div class="h5p-placeholder" contenteditable="false">[LINK_DO_ARQUIVO_.H5P]</div>
        </div>
      </div>
    </div>
  </div>
</div>
```

---

## 23. Vídeo com Legenda e Sinopse (Sub-bloco de 560px)

> **Contexto:** Bloco completo para incorporar vídeo do YouTube/Vimeo com legenda/créditos e sinopse. Utiliza sub-bloco de `max-width: 560px` para evitar que o vídeo fique excessivamente largo em telas grandes. A legenda fica entre o vídeo e a sinopse, dentro do mesmo sub-bloco centralizado.

> **Diferença do componente #10:** Este modelo inclui o sub-bloco `max-width: 560px; margin: 0 auto;` e o wrapper `col-lg-8` para alinhamento unificado de todos os elementos (vídeo, legenda e sinopse).

```html
<div class="row justify-content-center">
  <div class="col-lg-8"><!-- Sub-bloco de largura unificada -->
    <div style="max-width: 560px; margin: 0 auto;">
      <!-- Vídeo centralizado -->
      <div class="d-flex justify-content-center mb-2">
        <iframe class="vagalume-video" style="width: 100%; height: 315px; display: block;"
                title="Título do Vídeo" src="URL_EMBED"
                frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen="allowfullscreen"></iframe>
      </div>
      <!-- Legenda de créditos -->
      <p class="small text-muted mb-4" style="font-size: 0.85rem; line-height: 1.4;">
        <strong>Créditos:</strong> Texto de créditos aqui.
      </p>
      <!-- Bloco de Sinopse -->
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
> **Regras de uso:** A legenda é obrigatória neste modelo. O ícone `fa-file-text` na sinopse segue o padrão dos demais blocos de sinopse. O sub-bloco `max-width: 560px` garante que o vídeo não ultrapasse tamanhos confortáveis de leitura em monitores grandes.

---


---

## 24. Rótulo de Parte (Label de Seção do Moodle)

> **Contexto:** Bloco HTML usado como "Rótulo" (Label) no Moodle para demarcar visualmente o início de cada Parte/Seção de um módulo na página principal do curso. É um elemento isolado (não usa `.vagalume-pagina`) com border-left colorido e fundo bege.

> **Regras de uso:**
> - Sempre incluir comentários de abertura (`<!-- Módulo N - Label - Parte N - Título da Parte -->`) e fechamento (`<!-- FIM: Módulo N - Label - Parte N - Título da Parte -->`)
> - O span usa `text-transform: uppercase` via CSS para exibição visual em caixa alta, mas o texto real deve estar em Capitalize ("Parte 1") para leitores de tela (N2.4.4)
> - A cor padrão da borda e do texto do span é o **verde institucional `#587C41`**. Para variação laranja, substituir `#587C41` por `#D96F1A`
> - Para criar um novo label: copiar o template `ModuloN_Label_ParteN_titulo.html` em `templates/pages/labels/`, renomear para `MN_Label_ParteN_titulo.html`, alterar "Parte N" e o título do `<h2>`
> - **Template base:** `templates/pages/labels/ModuloN_Label_ParteN_titulo.html`

### Verde Institucional (Padrão)
```html
<!-- Módulo N - Label - Parte N - Título da Parte -->
<div style="border-left: 5px solid #587C41; padding: 10px 15px; margin: 30px 0 15px 0; background-color: #FAEBDD; border-radius: 0 8px 8px 0; font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;">
  <span style="display: block; font-size: 13px; text-transform: uppercase; color: #587C41; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px;">&nbsp;Parte N</span>
  <h2 style="margin: 0; padding: 0; font-size: 18px; color: #5B3925; font-weight: 700; border: none; line-height: 1.3;">Título da Parte</h2>
</div>
<!-- FIM: Módulo N - Label - Parte N - Título da Parte -->
```

### Laranja Principal (Alternativo)
```html
<!-- Módulo N - Label - Parte N - Título da Parte -->
<div style="border-left: 5px solid #D96F1A; padding: 10px 15px; margin: 30px 0 15px 0; background-color: #FAEBDD; border-radius: 0 8px 8px 0; font-family: 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;">
  <span style="display: block; font-size: 13px; text-transform: uppercase; color: #D96F1A; font-weight: bold; letter-spacing: 1px; margin-bottom: 5px;">&nbsp;Parte N</span>
  <h2 style="margin: 0; padding: 0; font-size: 18px; color: #5B3925; font-weight: 700; border: none; line-height: 1.3;">Título da Parte</h2>
</div>
<!-- FIM: Módulo N - Label - Parte N - Título da Parte -->
```

---

## 25. Template de Página de Fórum

> **Contexto:** Página completa de fórum do curso (atividade Fórum no Moodle). Todos os fóruns seguem **este mesmo formato**: título fixo com prefixo "Fórum: ", trecho de conteúdo livre do autor, caixa de destaque "Para participar" fixa (com ícone `fa-comments`), linha tracejada e mensagem final fixa (com ícone `fa-users`). Apenas o texto central da caixa e o conteúdo livre mudam entre fóruns.

> **Regras de uso:**
> - **Template base:** `templates/components/forum.html`
> - **Cabeçalho/rodapé:** padrão `Módulo X - Parte Y - Fórum Z - Fórum: [título completo da página]` (numeração decimal) — ver N2.2.2 do `.clinerules`
> - **Título fixo:** começa com "Fórum: ", usando `<span class="vagalume-destaque">` dentro de `<p class="h5 font-weight-bold mb-4">`
> - **Trecho variável:** `[CONTEÚDO_LIVRE_DO_AUTOR]` — pode conter texto, imagens, vídeos etc., seguindo os padrões do projeto (placeholder de imagem, vídeo N3.2.11, galerias N3.2.6)
> - **Caixa de destaque "Para participar":** içone `fa-comments` + título fixo "Para participar"; o **único elemento variável** é o texto central (`[TEXTO_CENTRAL_VARIÁVEL]`)
> - **Mensagem final FIXA:** "Após **sua postagem**, comente em **pelo menos duas participações** de colegas para fortalecermos nossa própria rede de aprendizagem!" com ícone `fa-users`
> - **Recomendado para criação:** copiar o template, substituir `[TÍTULO_COMPLETO]`, `[CONTEÚDO_LIVRE_DO_AUTOR]` e `[TEXTO_CENTRAL_VARIÁVEL]`

```html
<!-- Módulo X - Parte Y - Fórum Z - Fórum: [TÍTULO_COMPLETO] -->
<div class="container py-4 vagalume-pagina" style="display: flow-root;">
  <p class="h5 font-weight-bold mb-4"><span class="vagalume-destaque">Fórum: [TÍTULO_COMPLETO]</span></p>

  [CONTEÚDO_LIVRE_DO_AUTOR]

  <div class="card mb-4 border-0 bg-transparent">
    <div class="card-body vagalume-destaque-bloco mb-0">
      <div class="d-flex align-items-center mb-2"><i class="fa fa-comments mr-2" aria-hidden="true" style="font-size: 1.3rem; color: #5b3925;">&nbsp;</i> <span class="h5 font-weight-bold mb-0" style="color: #261810;">Para participar</span></div>
      [TEXTO_CENTRAL_VARIÁVEL]
      <hr style="border-top: 1px dashed rgba(91, 57, 37, 0.2);">
      <p class="mb-0 font-italic text-center style-italic" style="color: #261810; font-size: 0.95rem;"><i class="fa fa-users mr-1" aria-hidden="true" style="color: #2e7d32;">&nbsp;</i> Após <strong>sua postagem</strong>, comente em <strong>pelo menos duas participações</strong> de colegas para fortalecermos nossa própria rede de aprendizagem!</p>
    </div>
  </div>
</div>
<!-- FIM: Módulo X - Parte Y - Fórum Z - Fórum: [TÍTULO_COMPLETO] -->
```

> **Exemplo real:** `templates/pages/M2/ParteI/M2P1F1.html` (Fórum 1 da Parte 1 do Módulo 2, revisado em 08/08/2026 seguindo este padrão)

---

> 📝 **Para adicionar novo componente:** Edite este arquivo seguindo o padrão dos exemplos acima.
