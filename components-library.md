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

> 📝 **Para adicionar novo componente:** Edite este arquivo seguindo o padrão dos exemplos acima.
